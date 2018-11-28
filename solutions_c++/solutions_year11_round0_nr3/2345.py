#include<vector>
#include <algorithm>
#include <stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;


int devide(vector<int> nums);
int main()
{
	FILE *fPtr;
	FILE *fOut;
	int line;
	int count;
	vector<int> nums;
	int tmp;

	fstream flie;
	fOut=fopen("cl.out","w");
	if((fPtr=fopen("cl.in","r"))==NULL)
		printf("file can not be open");
	else
	{
		fscanf(fPtr,"%d",&line);
		printf("%d\n",line);
		int count;
		for(int i=0;i<line;i++)
		{
			nums.clear();
			fscanf(fPtr,"%d",&count);
			for(int j=0;j<count;j++)
			{
				fscanf(fPtr,"%d",&tmp);
				nums.push_back(tmp);
			}

//==========================Output==============================

			fprintf(fOut,"Case #%d: ",i+1);
			int result=devide(nums);
			if(result>0) fprintf(fOut,"%d\n",result);
			else fprintf(fOut,"NO\n");
		}
	}
	fclose(fPtr);
	fclose(fOut);
	printf("done");
	getchar();
	return 0;
}

int devide(vector<int> nums)
{
	int count = nums.size();
	int tmp=0;
	for(int i=0;i<count;i++)
	{
		tmp=tmp^nums[i];
	}
	if(tmp!=0) return 0;
	sort(nums.begin(),nums.end());

	int sum=0;
	for(int i=1;i<count;i++)
	{
		sum+=nums[i];
	}
	return sum;
}
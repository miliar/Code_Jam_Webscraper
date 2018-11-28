#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>
#include<set>
using namespace std;
int main()
{
	FILE* input = fopen("abc.in","r"); 
	FILE* output = fopen("output.txt","w+");
	int cases=0;
	fscanf(input,"%d",&cases);
	int count = 1;
	int a =0;
	int b=0;
	char str[10];
	while(cases>0)
	{
		long long unsigned int ans =0; 
		fscanf(input,"%d %d",&a,&b);
		if(b<=9)
		{
			ans =0;
		}
		else 
		{
			for(int i =a;i<b;i++)
			{
				itoa(i,str,10);
				string s(str);
				int length = s.length();
				set<string> ss;
				for(int j=1;j<length;j++)
				{
					string temp = "";
					temp.append(s.substr(j,length-j)).append(s.substr(0,j));
					int t = atoi(temp.c_str());
					if(t > i && t <= b)
					{
						ss.insert(temp);
					}
				}
				ans = ans + ss.size();
			}
		}
		fprintf(output,"Case #%d: %llu\n",count,ans);
		cases--;
		count++;
	}
}
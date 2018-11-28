#include<iostream>
#include<cstring>
#include<vector>
#include<fstream>
#include<cstdlib>

using namespace std;


class rollerCoaster{
	long int R;
	long int k;
	long int N;

public:
    rollerCoaster(long int _R,long int _k, long int _N)
	{
		R = _R;
		k = _k;
		N = _N;
	}
    int RollerCoasterEuro(vector<int> grpSize)
	{
		int eurosMade=0;
		int rcPeoplePerTurn=0;
		int totalPeople=0;
		int count,index;
		int posShift;
		vector<int> dummyArray;
		for(int i=0;i<R;i++)
		{
			count=0;
			rcPeoplePerTurn=0;
			while(rcPeoplePerTurn <= k && count<grpSize.size())
			{
				if((rcPeoplePerTurn + grpSize[count])<=k)
				{
					rcPeoplePerTurn += grpSize[count];
			    }
				else break;
					
				count++;
			}
			totalPeople += rcPeoplePerTurn;			
			posShift = count;
			dummyArray.clear();
			for(int i=0;i<grpSize.size();i++)
			{
				if((posShift+i)<grpSize.size())
					index = posShift+i;
				else
					index = (posShift+i) - grpSize.size();

                 
				dummyArray.push_back(grpSize[index]);
			}
			for(int i=0;i<grpSize.size();i++)
			{
				grpSize[i] = dummyArray[i];
			}
		}
		eurosMade = totalPeople;
		return eurosMade;
	}
	
		
	
};


int main()
{
	    string line;
		vector<int> grpSize;
		vector<int> output;
		int i,num;
		int r,k,n;
		int numOfTestCases;
		FILE *fp;
		fp = fopen("C-small-attempt1.in","r");
		if(fp == NULL)
		{
			printf("file could not be opened\n");
			getchar();
		}
		else{
			fscanf(fp,"%d",&numOfTestCases);
			for(i=0;i<numOfTestCases;i++)
			{
				grpSize.clear();
				fscanf(fp,"%d",&r);
				fscanf(fp,"%d",&k);
				fscanf(fp,"%d",&n);
				for(int j=0;j<n;j++)
				{
					fscanf(fp,"%d",&num);
					grpSize.push_back(num);
				}
				rollerCoaster rc(r,k,n);
				output.push_back(rc.RollerCoasterEuro(grpSize));
			}
			fclose(fp);
		FILE *fp1;
		fp1=fopen("output-small-attempt1.txt","w");
		for(int k=0;k<output.size();k++)
		{
			
			fprintf(fp1,"Case #%d: %d",k+1,output[k]);
			fprintf(fp1,"\n");

		}
		fclose(fp1);		
		}
		
		return 0;
}
	




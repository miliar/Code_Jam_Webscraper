#include <iostream>
#include <fstream>

using namespace std;

int findquery(int queries[],int S, int Q, int number, int firstcheck);

int main()
{
	int N,S,Q,N2;
	int i,j;
	char temp[120];
	char engines[100][120];
	char queries[1000][120];
	int queries2[1000];
	int answer;
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.out");
	if(fin.fail())
	{
		cout<<"error occured when open file!!"<<endl;
		exit(1);
	}
	fin.getline(temp,10);
	N=atoi(temp);
	N2=1;
	while(N!=0)
	{
		fin.getline(temp,10);
		S=atoi(temp);
		for(i=0;i<S;i++)
		{
			fin.getline(temp,110);
			strcpy(engines[i],temp);
		}
		fin.getline(temp,10);
		Q=atoi(temp);
		for(i=0;i<Q;i++)
		{
			fin.getline(temp,110);
			strcpy(queries[i],temp);
		}
		for(i=0;i<S;i++)
		{
			for(j=0;j<Q;j++)
			{
				if(strcmp(engines[i],queries[j])==0)
					queries2[j]=i;
			}
		}
		if(Q!=0)
			answer=findquery(queries2,S,Q,0,0);
		else
			answer=0;
		fout<<"Case #"<<N2<<": "<<answer<<endl;


		N--;
		N2++;

	}

	return 0;
}

int findquery(int queries[],int S, int Q, int number, int firstcheck)
{
	static int count=0;
	int i,j,k;
	int max;
	int check1, check2;
	int enginecounts[100];
	k=0;
	if(firstcheck==0)
		count=0;
	check1=0;
	check2=0;
	for(i=0;i<S;i++)
	{
		for(j=number;j<Q;j++)
		{
			if(queries[j]==i)
			{
				enginecounts[i]=j;
				if(j==Q-1)
				{
					check1++;
					check2++;
				}
				break;
			}
			else if(j==Q-1)
			{
				check1++;
				enginecounts[i]=Q-1;
				break;
			}
		}
	}
	if(check1==check2 && check1!=0)
		count++;
	max=0;
	for(i=0;i<S;i++)
	{
		if(max<=enginecounts[i])
			max=enginecounts[i];
	}
	if(max==Q-1)
		return count;
	else
	{
		count++;
		findquery(queries,S,Q,max,1);
	}
	return count;
}

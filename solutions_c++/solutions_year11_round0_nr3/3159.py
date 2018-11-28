#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>
#include <bitset>

using namespace std;

bool isXOREqual(vector<int> x, vector<int> y)
{
	int x1=x[0];
	for(int j=1;j<x.size();j++)
		x1 = x1^x[j];

	int y1 = y[0];
	for(int j=1;j<y.size();j++)
		y1 = y1^y[j];
	
	return (x1==y1);
}


int doForOne(vector<int> X)
{

	int n= X.size();
	int val=-1;
	for(int i=0;i<(1<<n);i++)
	{
		bitset<15> bits(i);
		vector<int> a, b;
		for(int j=0;j<n;++j)
		{
			if(bits.test(j))
				a.push_back(X[j]);
			else
				b.push_back(X[j]);
		}
		
		if(a.size()>0 && b.size()>0)
		{
			if(isXOREqual(a,b))
			{
				int m1,m2;
				m1=m2=0;
				//printf("\na = ");
				for(int k=0;k<a.size();k++)
				{
					m1 = m1+a[k];
					//printf("%d ",a[k]);
				}
				//printf("\nb = ");
				for(int k=0;k<b.size();k++)
				{
					//printf("%d ",b[k]);
					m2 = m2+b[k];
				}
			
				val = max(val,max(m1,m2));
			}
		}
	}
	return val;
}

int main()
{
	FILE *fp = fopen("trial.in","r");
	if(!fp)
	{
		printf("\nFile not found ... ");
		return 0;
	}
	int T;
	fscanf(fp,"%d",&T);
	for(int i=1;i<=T;i++)
	{
		int N;vector<int> X;
		fscanf(fp,"%d",&N);
		for(int j=0;j<N;j++)
		{
			int temp;
			fscanf(fp,"%d",&temp);
			X.push_back(temp);
		}
		int val = doForOne(X);
		printf("Case #%d: ",i);
		if(val==-1)
			printf("NO\n");
		else
			printf("%d\n",val);
	}
	fclose(fp);
	getchar();
	return 0;
		
}

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

ifstream fin;
ofstream fout;
int N;
int a[900],b[900];
int calc()
{
	int res=0;
	for(int i=0;i<N;i++)
	{
		res+=a[i]*b[i];
	}
	return res;
}
int min=999999999;
void perm(int n)
{
	int i;
	if(n==N)
	{
		int aaa=calc();
		if(aaa<=min)
			min=aaa;
	}
	int temp;
	for(i=n;i<N;i++)
	{
		temp=b[i];
		b[i]=b[n];
		b[n]=temp;
		perm(n+1);
		temp=b[i];
		b[i]=b[n];
		b[n]=temp;
	}
	return;
}

int main(void)
{
	int it,i,j,k,l,T;

	fin.open("input.in");
	FILE *fp=fopen("output.out","w");
	fin>>T;
//	fin>>noskipws;
//	fin>>skipws;

	for(it=1;it<=T;it++)
	{
		min=99999999;
		fin>>N;
		for(i=0;i<N;i++)
		{
			fin>>a[i];
		}
		for(i=0;i<N;i++)
		{
			fin>>b[i];
		}
		perm(0);
		fprintf(fp,"Case #%d: %d\n",it,min);
//		fprintf(fp,"Case #%d: %.6f\n",it,prob);
	}
    fin.close();
	fclose(fp);
	return 0;
}

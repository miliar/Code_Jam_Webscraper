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
int per[5];
string s;
int min;

int calc(int k)
{
	string s2=s;
	int i,j,res=0;
	for(i=0;i<s.length()/k;i++)
	{
		for(j=0;j<k;j++)
		{
			s2[j+i*k]=s[i*k+per[j]];
		}
	}
	for(i=1;i<s2.length();i++)
	{
		if(s2[i]!=s2[i-1])
			res++;
	}
	return res+1;
}

void permute(int n,int k)
{
	int i;
	int tmp;
	if(n==k)
	{
		tmp=calc(k);
		if(tmp<min)
			min=tmp;
		return;
	}
	for(i=n;i<k;i++)
	{
		tmp=per[i];per[i]=per[n];per[n]=tmp;
		permute(n+1,k);
		tmp=per[i];per[i]=per[n];per[n]=tmp;
	}
}


int main(void)
{
	int it,i,j,k,l,N;
	fin.open("input.in");
	FILE *fp=fopen("output.out","w");
	fin>>N;
//	fin>>noskipws;
//	fin>>skipws;

	for(it=1;it<=N;it++)
	{
		fin>>k;
		fin>>s;
		min=9999999;
		per[0]=0;per[1]=1;per[2]=2;per[3]=3;per[4]=4;
		permute(0,k);

		fprintf(fp,"Case #%d: %d\n",it,min);
	}
    fin.close();
	fclose(fp);
	return 0;
}

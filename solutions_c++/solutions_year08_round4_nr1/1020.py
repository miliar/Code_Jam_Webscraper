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
int value[1005],g[1005],c[1005],M,V;
int cg[1005],ncg,minchange;


int init(int m)
{
	if(m>(M-1)/2)
		return value[m];
	int v1=init(m*2);
	int v2=init(m*2+1);
	if(g[m]==1)
		return value[m]=v1&&v2;
	else
		return value[m]=v1||v2;
}
void calc(int pos, int nchange)
{
	int val;
	if(pos==ncg)
	{
		val=init(1);
		if(val==V)
		{
			if(nchange<minchange)
				minchange=nchange;
		}
		return;
	}
	calc(pos+1,nchange);
	if(g[cg[pos+1]]==1) g[cg[pos+1]]=0;
	else g[cg[pos+1]]=1;
	calc(pos+1,nchange+1);
	if(g[cg[pos+1]]==1) g[cg[pos+1]]=0;
	else g[cg[pos+1]]=1;
	return;
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
		fin>>M>>V;
		ncg=0;minchange=999999;
		for(i=1;i<=(M-1)/2;i++)
		{
			fin>>g[i]>>c[i];
			if(c[i]==1)
			{
				ncg++;
				cg[ncg]=i;
			}
		}
		for(i=(M+1)/2;i<=M;i++)
		{
			fin>>value[i];
		}
		calc(0,0);
		if(minchange!=999999)
		{
			fprintf(fp,"Case #%d: %d\n",it,minchange);
		}
		else
			fprintf(fp,"Case #%d: IMPOSSIBLE\n",it);
	}
    fin.close();
	fclose(fp);
	return 0;
}

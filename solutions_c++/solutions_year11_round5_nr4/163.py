#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

#define MAX_N 125
#define MAX_Q 20
#define INF 2000000000

using namespace std;

FILE *fin=fopen("D-small-attempt0.in","r");
FILE *fout=fopen("D-small-attempt0.out","w");

int t,iii;
int n,i,j,k;
long long val;
long long le,ri,mi,tmp;
int pos[MAX_N],enp;
char in[MAX_N];

void findanswer()
{
	for(k=0;k<(1<<enp);k++)
	{
		for(j=0;j<enp;j++)
		{
			if((k&(1<<j))!=0)
			{
				in[pos[j]]='1';
			}
			else
			{
				in[pos[j]]='0';
			}
		}
		val=0;
		for(j=0;j<n;j++)
		{
			val*=2;
			val+=(in[j]-'0');
		}
		//fprintf(fout,"LLL %lld\n",val);
		le=-1;
		ri=INF;
		ri+=INF;
		while(ri>le+1)
		{
			mi=(le+ri)/2;
			tmp=mi*mi;
			if(tmp==val)
			{
				return ;
			}
			else if(tmp>val)
			{
				ri=mi;
			}
			else
			{
				le=mi;
			}
		}
		//fprintf(fout,"OO %lld %lld\n",le,ri);
		if(le*le==val||ri*ri==val)
			return ;
	}
	return ;
}

int main()
{
	fscanf(fin,"%d",&t);
	for(iii=0;iii<t;iii++)
	{
		fscanf(fin,"%s",in);
		n=strlen(in);
		enp=0;
		for(i=0;i<n;i++)
		{
			if(in[i]=='?')
			{
				pos[enp]=i;
				enp++;
			}
		}
		findanswer();
		fprintf(fout,"Case #%d: ",iii+1);
		fprintf(fout,"%s\n",in);
	}
	return 0;
}
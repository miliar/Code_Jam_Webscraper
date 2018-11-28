#include <iostream>
#include <cstdio>

#define MAX_P 1000001

using namespace std;

int t,iii;
int i,j,en;
int answer;
long long n,tmp1,cnt;
long long prime[MAX_P];

FILE *fin=fopen("C-large.in","r");
FILE *fout=fopen("C-large.out","w");

void genprime()
{
	en=0;
	for(i=2;i<MAX_P;i++)
	{
		for(j=0;j<en&&prime[j]*prime[j]<=i;j++)
		{
			if(i%prime[j]==0)
				break;
		}
		if(j==en||prime[j]*prime[j]>i)
		{
			prime[en]=i;
			en++;
		}
	}
	for(i=0;i<en;i++)
	{
		//fprintf(fout,"%d %lld\n",i,prime[i]);
	}
	return ;
}

int main()
{
	fscanf(fin,"%d",&t);
	genprime();
	for(iii=0;iii<t;iii++)
	{
		fscanf(fin,"%lld",&n);
		if(n==1)
		{
			answer=0;
		}
		else
		{
			answer=1;
			for(i=0;i<en&&prime[i]*prime[i]<=n;i++)
			{
				tmp1=n;
				while(tmp1>0)
				{
					tmp1/=prime[i];
					answer++;
				}
				answer--;
				answer--;
			}
		}
		fprintf(fout,"Case #%d: %d\n",iii+1,answer);
	}
	return 0;
}
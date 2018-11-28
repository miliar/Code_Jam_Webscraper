#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int MAXN=1001;
int primeList[MAXN],primeNum;
bool isNotPrime[MAXN];
void prime()
{
	memset(isNotPrime,0,sizeof(isNotPrime));
	int i,j;
	for(i=4;i<MAXN;i+=2) isNotPrime[i]=true;
	primeList[0]=2;
	primeNum=1;
	for(i=3;i<MAXN;i+=2)
	{
		if(!isNotPrime[i])
			primeList[primeNum++]=i;
		for(j=0;j<primeNum&&primeList[j]*i<MAXN;j++)
		{
			isNotPrime[primeList[j]*i]=true;
			if(i%primeList[j]==0) break;
		}
	}
}
int main()
{
	int cas,cnt,i,mmin,mmax,n,j,temp;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	prime();
	scanf("%d",&cas);
	for(cnt=1;cnt<=cas;cnt++)
	{
		scanf("%d",&n);
		if(n==1)
		{
			printf("Case #%d: 0\n",cnt);

		}
		else
		{
		for(i=0;i<primeNum;i++)
		{
			if(primeList[i]>n) break;
		}
		mmin=i;
		mmax=1;
		for(i=0;i<primeNum&&primeList[i]<=n;i++)
		{
			j=primeList[i];
			temp=1;
			while(1)
			{
				j*=primeList[i];
				if(j>n) break;
				temp++;
			}
			mmax+=temp;
		}
		
		printf("Case #%d: %d\n",cnt,mmax-mmin);
		}
	}
}
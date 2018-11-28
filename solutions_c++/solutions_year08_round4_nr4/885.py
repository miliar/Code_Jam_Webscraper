#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
#include<string>
using namespace std;	

#define sq(a) ((a)*(a))
#define pb(a) push_back(a)
#define Min(a,b) (((a)<(b))?(a):(b))
#define Max(a,b) (((a)>(b))?(a):(b))
#define eps 1e-9
#define inf 1<<29
#define pye 2.*acos(0.)
#define SZ(v) ((int)(v).size())
#define For(i,a,b) for(i=(a);i<(b);++i)
#define Fore(i,a,b) for(i=(a);i<=(b);++i)
#define Forc(i,v) For(i,0,SZ(v))
#define Foro(i,a) For(i,0,a)

int *taken,len,k;
int given[10],gen[6][125][6],s[10],fact[6];
void gene(int lev)
{
	int i,flag;
	if(lev==len)
	{
		for(i=0;i<len;i++)
			gen[len][k][i]=s[i];
		k++;
		return;
	}
	for(i=flag=0;i<len;i++)
	{
		if(!taken[i] && !flag)
		{
			s[lev]=given[i];
			lev++;
			taken[i]=1;
			if(given[i]==given[i+1])flag=1;
			gene(lev);
			lev--;
			taken[i]=0;
		}
		else if(given[i]!=given[i+1])
			flag=0;
	}
	return;
}

char ss[1005];
int conv(int p,int now)
{
	int i,j,ln=strlen(ss),l=0,cnt=0;
	char he[1005];
	Foro(i,ln/p)
		Foro(j,p)
		{
			he[l]=ss[gen[p][now][j]-1+i*p];
			l++;
		}
	for(i=0;i<ln;++i)
		if(!i || he[i]!=he[i-1])
			cnt++;
	return cnt;
}

int main()
{
	int i,j,t,cs,p,mn;
	freopen("D.txt","w",stdout);
	fact[0]=1;
	Foro(i,5)
		given[i]=i+1;
	For(i,1,6)
		fact[i]=fact[i-1]*i;
	For(i,1,5)
	{
		taken=(int *)calloc(i+1,sizeof(int));
		len=i+1;
		k=0;
		gene(0);
		free(taken);
	}
	scanf("%d",&t);
	Foro(cs,t)
	{
		scanf("%d%s",&p,ss);
		mn=inf;
		Foro(i,fact[p])
			j=conv(p,i),mn=Min(j,mn);
		printf("Case #%d: %d\n",cs+1,mn);
	}
	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

#define VI vector <int>
#define VVI vector < vector<int> >
#define VS vector <string>
#define rep(i,n) for(int i=0;i<(n);++i)
#define repab(i,a,b) for(int i=(a);i<=(b);++i)
#define PB push_back
#define SORT(v) sort(v.begin(), v.end())

using namespace std;

int pier[1001000];
int pp[1000000];
int ppn;
int liczby[1001000];
long long A,B,P;
int n;

int wez(int i)
{
	int s=i,t,tt;
	while(liczby[s]!=s) s=liczby[s];
	t=i;
	while(t!=s)
	{
		tt = t;
		t = liczby[t];
		liczby[tt]=s;
	}
	return s;
}

void ustaw(int i, int s)
{
	int t,tt;
	t=i;
	while(liczby[t]!=t)
	{
		tt = t;
		t = liczby[t];
		liczby[tt]=s;
	}
	liczby[t]=s;
}

void przejdz(int s, int t)
{
	int se=wez(s);
	int q=s+t;
	while(q<n)
	{
		ustaw(q,se);
		q+=t;
	}
}

void licz(void)
{
	int s;
	long long S;
	scanf("%lld%lld%lld",&A,&B,&P);
	n = B-A+1;
	rep(i,n) liczby[i]=i;
	rep(i,ppn)
	if (pp[i]>=P)
	{
		if (pp[i]>n) break;
		S = A/((long long)pp[i]);
		S-=2;
		S *= pp[i];
		while(S<A) S+=pp[i];
		S -= A;
		s = S;
		przejdz(s, pp[i]);
	}
	int ret=0;
	rep(i,n) if(liczby[i]==i) ret++;
	printf("%d\n",ret);
}

int main(void)
{
	int pom;
	ppn=0;
	pier[0] = pier[1] = 1;
	rep(i,1000010)
		if (pier[i]==0)
		{
			pp[ppn]=i;
			ppn++;
			pom = i+i;
			while(pom<1000100)
			{
				pier[pom]=1;
				pom += i;
			}
		}
	int dd;
	scanf("%d",&dd);
	for(int yy=0;yy<dd;yy++)
	{
		printf("Case #%d: ", yy+1);
		licz();
	}
	return 0;
}

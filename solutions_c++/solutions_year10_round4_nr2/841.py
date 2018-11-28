#include<cstdio>
#include<climits>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<deque>
#include<fstream>
#include<iostream>
#include<bitset>
#include<set>
#include<map>
#include<list>
#include<string>
using namespace std;
#define pb push_back
#define fs first
#define sc second
#define mp make_pair
#define pii pair< int,int >
#define pss pair< short,short >
#define pdd pair< double,double >
#define ll long long
#define N 2048

int v[N];
int n;
int p;
inline void citire()
{
	char c[N]={0};
	scanf("%d",&p);
	n=1<<p;
	for(int i=0; i<n; ++i)
	{
		scanf("%d",&v[i]);
		v[i]=p-v[i];
	}

	for(int i=0; i<=p; ++i)
		fgets(c,N,stdin);
}

inline bool is(int pr,int ul)
{
	for(int i=pr; i<ul; ++i)
	{
		if(v[i]>0)
			return true;
	}
	return false;
}

inline void dec(int pr,int ul)
{
	for(int i=pr; i<ul; ++i)
		--v[i];
}
inline int rezolva()
{
	int rez=0;
	//for(int i=0; i<n; ++i)
	//	printf("%d ",v[i]);
        //printf("\n");
	for(int i=p; i>0; --i)
	{
		for(int j=0,pas=1<<i; j<n; j+=pas)
		{
                	if(is(j,j+pas))
			{
				++rez;
				dec(j,j+pas);
			}
		}
	}

	return rez;
}

int main()
{
	freopen("pb.in","r",stdin);
	freopen("pb.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; ++i)
	{
		citire();
		printf("Case #%d: %d\n",i,rezolva());
	}

	return 0;
}


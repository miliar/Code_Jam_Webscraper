#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <queue>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define rep(i,X,n) for( int (i) = (X) ; (i)<(n) ; (i) ++)
#define repit(it,X,n) for(__typeof((X)) it = (X) ; (it) != (n) ; (it)++)
#define PRINT(...) fprintf(stdout,__VA_ARGS__)
#define ALL(X) (X).begin(),(X).end()

int nn;
int pr[10001];
int A,B,P;
int a1[101];
int a2[101];
int sa1,sa2;


bool isPrime(int x)
{
	if(x==2)
		return true;
	if(x%2==0)
		return false;
	for(int i=3;i*i<=x;i+=2)
		if(x%i==0)
			return false;
	return true;
}

void fact(int x,int a[],int &sa)
{
	rep(i,0,nn)
	{
		if(x%pr[i]==0)
		{
			a[sa++] = pr[i];
		}
	}
}

bool f(int x,int y)
{
	sa1=0;
	sa2=0;
	fact(x,a1,sa1);
	fact(y,a2,sa2);
	rep(i,0,sa1)
	{
		rep(j,0,sa2)
		{
			if(a1[i]==a2[j] && a1[i]>=P)
				return true;
		}
	}
	return false;
}

int p[1000001];
int rank[1000001];
int comp;

int find(int x)
{
	if(x==p[x])
		return x;
	return p[x] = find(p[x]);
}

void join(int x,int y)
{
	int px = find(x);
	int py = find(y);
	if(rank[px] < rank[py])
		p[py] = px,	comp--;
	else
		if(rank[px] >= rank[py])
			p[px] = py,	comp--;
	else
		if( px != py)
			p[y] = px,rank[px]++,comp--;
}


int main()
{
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("out.out","wt",stdout);
	
	int t;
	nn=0;
	rep(i,2,1001)
		if(isPrime(i))
			pr[nn++] = i;
	
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d %d %d",&A,&B,&P);
		memset(rank,0,sizeof(rank));
		rep(i,0,1000001)
			p[i]=i;
		comp = B-A+1;
		rep(i,A,B+1)
			rep(j,i+1,B+1)
				if(f(i,j) && find(i-A)!=find(j-A))
					join(i-A,j-A);
		printf("Case #%d: %d\n",tt+1,comp);
	}
	
	return 0;
}

#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, L,P,C,res;

int mylog(int k)
{
	int r=0,m=1;
	if (k==1) return 0;
	while(m*2<=k)
	{
		m*=2;
		r++;
	}
	return r;
}

void solve()
{
	int k=0;
	long long ll=L;
	while (C*ll<(long long)P)
	{
		k++;
		ll*=C;
	}
	if (k==0) res=0;
	else res = mylog(k)+1;
}

void write(int i)
{
	printf("Case #%d: %d\n",i,res);


}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d",&T);
	

	for (int i=0; i<T; i++)
	{
		scanf("%d%d%d", &L, &P, &C);
		solve();
		write(i+1);
	}
	return 0;
}

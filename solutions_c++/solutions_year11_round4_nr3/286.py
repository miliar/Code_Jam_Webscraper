#include <iostream>
#include <set>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <assert.h>

using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define mp make_pair
#define pnt pair<int,int>
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define LL long long
#define U unsigned
bool f[1000010];
vector<int> pr;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	f[0]=f[1]=false;
	FOR(i,2,1000001)
		f[i]=true;
	for (int i=2; i<=1000000; ++i)
		for (int j=i+i; j<=1000000; j+=i)
			f[j]=false;
	FOR(i,0,1000000)
		if (f[i])
			pr.push_back(i);
	FOR(test,1,t+1)
	{
		LL n;
		scanf("%lld",&n);
		printf("Case #%d: ",test);
		if (n==1)
		{
			printf("0\n");
			continue;
		}
		int res1=1,res2=0;
		FOR(i,0,pr.size())
		{
			LL k=pr[i];
			if (k<=n)
				res2++;
			else
				break;
			while (k<=n)
			{
				res1++;
				k*=pr[i];
			}
		}
		printf("%d\n",res1-res2);
	}
	return 0;
}

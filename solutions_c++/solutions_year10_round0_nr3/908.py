#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#pragma warning(disable : 4996)

#define MAXN	1000
int R, k, N;
int g[MAXN], gaccu[MAXN], gnext[MAXN], gcount[MAXN];
int status[MAXN];
long long accu[MAXN];
void init()
{
	scanf("%d %d %d", &R, &k, &N);
	for (int i=0;i<N;++i)
	{
		scanf("%d", &g[i]);
	}
	int tmpk, tmpi;
	
	for (int i=0;i<N;++i)
	{
		if (i==0)
		{
			tmpk=g[i]; tmpi=1; gcount[i]=tmpi-i;
		}
		else
		{
			tmpk=gaccu[i-1]-g[i-1];
			tmpi=gnext[i-1];
			gcount[i]=gcount[i-1]-1;
		}
		tmpi%=N;
		while(tmpk+g[tmpi]<=k && gcount[i]<N)
		{
			tmpk+=g[tmpi];
			tmpi++;
			tmpi%=N;
			gcount[i]++;
		}
		gnext[i]=tmpi%=N;
		gaccu[i]=tmpk;
	}
}

long long solve()
{
	long long ep(0);
	memset(status, 0, sizeof(status));
	memset(accu, 0, sizeof(accu));
	int i(0), idx(0);
	while (i<R)
	{
		if (!status[idx])
		{
			i++;
			accu[idx]=ep;
			ep+=gaccu[idx];
			status[idx]=i;
			idx=gnext[idx];
		}
		else
		{
			int loop_len=i-status[idx]+1;
			//enter loop
			int loop=(R-i)/loop_len;
			long long loop_e=ep-accu[idx];
			ep += loop_e*loop;
			i += loop_len*loop;
			//memset(status,0,sizeof(status));
			break;
		}
	}
	while (i<R)
	{
		i++;
		ep+=gaccu[idx];
		idx=gnext[idx];
	}
	return ep;
}

int main()
{
//	freopen("..\\C-sample.in","r",stdin);freopen("..\\C.out","w",stdout);
//	freopen("..\\C-small-attempt1.in","r",stdin);freopen("..\\C-small.out","w",stdout);
	freopen("..\\C-large.in","r",stdin);freopen("..\\C-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		init();
		long long ret=solve();
		printf("%lld\n",ret);
		
		fflush(stdout);
	}
	return 0;
}


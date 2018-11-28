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
const int maxn = 1000+5;
int q[maxn];
int c[maxn];
int n[maxn];
int R,K,N;

int r;
void init()
{
	r = 0;
	memset(c,0,sizeof(c));
	memset(n,0,sizeof n);
	for(int i=0;i<N;i++)
	{
		int p = q[i];
		int j = i;
		int len = 1;
		int find = 0;
		while(p < K)
		{
			j++;
			j%=N; 
			len++;
			p+=q[j];
			if(len >N)
			{
				find =1;
			}
			
			if(p > K)
			{
				find = 1;
			}
			else if(p==K && len <= N)
			{
				break;
			}
			if(find ==1)
			{
				p -=q[j];
				if(j > 0)
					j--;
				else
					j = N-1;
				break;
			}
			
		}
		c[i] = p;
		n[i] = (j+1)%N;
	}
}
int solve()
{
	int start = 0;
	for(int i=0;i<R;i++)
	{
		r += c[start];
		start = n[start];
	}
	return r;
}

int main()
{
//	freopen("c-test.in","r",stdin);//freopen("c-test.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);freopen("c-small.out","w",stdout);
//	freopen("c-large.in","r",stdin);freopen("c-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for(int i=0;i<N;i++)scanf("%d",&q[i]);
		init();
		solve();
	
		printf("Case #%d: %d\n",caseId,r);
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}
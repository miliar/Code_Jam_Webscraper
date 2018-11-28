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

#define SIZE(X) ((int)(X.size()))

int n,m;
int A[10000],R[10000];
vector<int> S[10000];

void solve()
{
	memset(R,0,sizeof(R));
	while (1)
	{
		bool ok=true;
		for (int i=0;i<m;i++)
		{
			if (A[i]>=0 && R[A[i]]==1) continue;
			bool fd=false;
			for (int k=SIZE(S[i])-1;!fd && k>=0;k--)
				if (R[S[i][k]]==0)
					fd=true;
			if (!fd)
			{
				if (A[i]<0)
				{
					printf(" IMPOSSIBLE\n");
					return;
				}
				R[A[i]]=1;
				ok=false;
				break;
			}
		}
		if (ok) break;
	}
	for (int i=0;i<n;i++) 
		printf(" %d",R[i]);
	printf("\n");
}
int main()
{
//	freopen("..\\input.txt","r",stdin);
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<m;i++)
		{
			int cnt,key,type;
			A[i]=-1;
			S[i].clear();
			for (scanf("%d",&cnt);cnt>0;cnt--)
			{
				scanf("%d%d",&key,&type);
				key--;
				if (type==1) A[i]=key;
				else S[i].push_back(key);
			}
		}
		printf("Case #%d:",caseId);
		solve();
	}
	return 0;
}


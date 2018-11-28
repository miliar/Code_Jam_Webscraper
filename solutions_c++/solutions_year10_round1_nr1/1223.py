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
typedef pair<int,int> pii;
typedef long long ll;
const int maxn = 40+5;
int r;
int N,K;
char jk[maxn][maxn];
char rjk[maxn][maxn];
char njk[maxn][maxn];

void init()
{
	for(int i = 0;i<N;i++)
	{
		for(int j =N-1;j>=0;j--)
		{
			if(jk[j][i] != '.')
				rjk[i][N-j-1] = jk[j][i];
		}
	}
	
	for(int i = 0;i<N;i++)
	{
		for(int j =N-1;j>=0;j--)
		{
			if(rjk[j][i] != '.')
			{
				for(int k=j+1;k<N;k++)
				{
					if(rjk[k][i] != '.')
					{
						if(k > j+1)
						{
							rjk[k-1][i] = rjk[j][i];
							rjk[j][i] = '.';
						}
						break;
					}
					else
					{
						if(k == N-1)
						{
							if(k> j)
							{
								rjk[k][i] = rjk[j][i];
								rjk[j][i] = '.';
							}
						}
					}
				}
			}
		}
	}
}
int solve()
{
	int findr = 0;
	int findb = 0;
	int look = 0;
	int find = 0;
	for(int i=0;i<N;i++)
	for(int j=0;j<N;j++)
	{
		if(rjk[i][j] == '.')
			continue;
		look = rjk[i][j];
		if(look == 'R' && findr == 1) continue;
		if(look == 'B' && findb == 1) continue;
		int k=0;find = 0;
		for(k = 0;k<K && k+j < N;k++) if(rjk[i][k+j] != look)break;
		if(k == K) find = 1;
		for(k = 0;k<K && k+i < N;k++) if(rjk[i+k][j] != look)break;
		if(k == K) find = 1;
		for(k = 0;k<K && k+i < N && k+j < N;k++) if(rjk[i+k][j+k] != look)break;
		if(k == K) find = 1;
		for(k = 0;k<K && k+i < N && j-k >= 0;k++) if(rjk[i+k][j-k] != look)break;
		if(k == K) find = 1;
		if(find == 1) 
		{
			if(look == 'R')findr = 1;
			else findb = 1;
		}
	}
	
	r = findr+2*findb;
	return r;
}

int main()
{
//	freopen("a-test.in","r",stdin);//freopen("a-test.out","w",stdout);
	freopen("a-small-attempt3.in","r",stdin);freopen("a-small.out","w",stdout);
//	freopen("a-large.in","r",stdin);freopen("a-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		cin>>N>>K;
		memset(jk,'.',sizeof jk);
		memset(rjk,'.',sizeof rjk);
		memset(njk,'.',sizeof njk);
		
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				cin>>jk[i][j];
		init();
		solve();
		cout<<"Case #"<<caseId<<": ";
		if(r == 0)
			cout<<"Neither"<<endl;
		else if(r == 1)
			cout<<"Red"<<endl;
		else if(r == 2)
			cout<<"Blue"<<endl;
		else if(r == 3)
			cout<<"Both"<<endl;
		cerr<<caseId<<"/"<<testcase<<endl;
	}
	return 0;
}













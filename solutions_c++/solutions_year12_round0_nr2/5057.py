//TC Accretia Code Template
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

bool srot(int a,int b)
{
	return (a > b);
}

int
main()
{
	int T;
	int N,S;
	int tmp,P;
	vector<int> score;
	int ans;
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		ans = 0;
		score.clear();
		scanf("%d %d %d",&N,&S,&P);
		for(int i = 0;i < N;i++)
		{
			scanf("%d", &tmp);
			score.PB(tmp);
		}
		sort(score.begin(),score.end(),srot);
		for(int i = 0;i < N;i++)
		{
			int high = score[i]/3;
			int rem = score[i] % 3;
			if(rem != 0)high++;
			
			if(high >= P)
			{
				ans++;
				continue;
			}
			else if(high == P-1 &&  high > 1 && S > 0)
			{
				if(rem == 0 || rem == 2)
				{
					S--;
					ans++;
				}
				else break;
			}
			else break;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
return 0;
}
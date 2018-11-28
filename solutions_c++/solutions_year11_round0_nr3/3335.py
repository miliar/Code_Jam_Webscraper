#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <bitset>
#include <cstdlib>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin();it!=(v).end(); ++it)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
int N;

void solve(int tc)
{
	int rt = 1<<30;
	int sum = 0;
	int x;
	ll S = 0;
	scanf("%d", &N);
	rep(i,0,N)
	{
		scanf("%d", &x);
		S += x;
		sum ^= x;
		rt = min(rt, x);
	}
	if(sum)
	{
		printf("Case #%d: NO\n", tc);
	}
	else
	{
		cout << "Case #" << tc << ": " << (S-rt) << endl;
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	rep(i,0,T)
		solve(i+1);
  return 0;
}

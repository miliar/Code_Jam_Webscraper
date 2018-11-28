#include <iostream>
#include <fstream>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <list>
#include <deque>

#include <cmath>
#include <string>
#include <ctime>
#include <ctime>
#include <cstdlib>
#include <algorithm>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define tr(v,it) for(typeof(v.begin()) it = v.begin(); it != v.end() ; ++it)
#define all(c) c.begin(),c.end()
#define SZ(c) (int)c.size()
#define SQ(x) (x)*(x)
#define OUT(a,b)FOR(i,0,b)cout << a[i] << " ";cout << endl;
#define PI 2.0*acos(0.0)
#define SET(a,b) memset(a,b,sizeof a)
#define r(T) scanf("%d",&T)
using namespace std;

typedef long long LL;
const int MAXN = 1001;
int arr[MAXN];
map<int,int> score;
int main()
{
	int T,R,K,N;
	r(T);
	REP(cases,1,T)
	{
		r(R);r(K);r(N);
		FOR(i,0,N)r(arr[i]);
		score.clear();
		LL cost = 0;
		int head = 0;
		int rounds = 0;
		int visited = 0;
		do
		{
			int sum = 0;
			++rounds;
			int aa = N;
			while((sum < K) && (aa--) )
			{
				sum += arr[head];
				head++;
				if(head == N)head = 0;
			}
			if(sum > K)
			{
				if(head == 0)head = N-1;
				else --head;
				sum -= arr[head];
			}
			cost += sum;
			score[rounds] = cost;
			if(head == 0)visited = true;
		}while(rounds<R && !visited);
		if(rounds < R)
		{
			int cycle = rounds;
			cost = (R/cycle)*cost;
			cost += score[R%cycle];
		}
		printf("Case #%d: %lld\n",cases,cost); 
	}
	return 0;
}

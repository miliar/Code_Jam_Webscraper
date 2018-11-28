#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <deque>

using namespace std;

#define reep(i,f,t) for(int i=f ; i<int(t) ; ++i)
#define rep(i,n) reep(i, 0, n) 

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int main()
{
	int t;
	scanf("%d", &t);
	rep(i, t){
		int d, g;
		long long n;
		scanf("%lld%d%d", &n, &d, &g);
		
		int tmp = d;
		int m = 100;
		int div[] = {2, 2, 5, 5};
		rep(j, 4){
			if(tmp%div[j]==0){
				tmp /= div[j];
				m /= div[j];
			}
		}
		
		if(n < m)
			printf("Case #%d: Broken\n", i+1);
		else{
			if(d != 100 && g == 100)
				printf("Case #%d: Broken\n", i+1);
			else if(d != 0 && g == 0)
				printf("Case #%d: Broken\n", i+1);
			else
				printf("Case #%d: Possible\n", i+1);
		}
	}

	return 0;
}


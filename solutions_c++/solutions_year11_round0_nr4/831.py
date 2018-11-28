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
	int n;
	scanf("%d", &n);
	
	rep(i, n){
		int m;
		scanf("%d", &m);
		int diff = 0;
		rep(j, m){
			int a;
			scanf("%d", &a);
			if(j+1 != a) diff++;
		}
		printf("Case #%d: %lf\n", i+1, (double)diff);
	}
	
	return 0;	
}


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
		scanf("%d%*c", &m);
		
		int time = 0;
		int pos[2] = {1, 1};
		int moved[2] = {0, 0};
		rep(j, m){
			char c;
			int a;
			scanf("%c%*c%d%*c", &c, &a);
			
			int id = c == 'O';
			time += max(0, abs(pos[id] - a) - (time - moved[id])) + 1;
			pos[id] = a;
			moved[id] = time;
		}

		printf("Case #%d: %d\n", i+1, time);
	}

	return 0;
}


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
		
		int sum = 0;
		int minimum = 10000000;
		int xoring = 0;
		rep(j, m){
			int c;
			scanf("%d", &c);
			xoring ^= c;
			sum += c;
			minimum = min(minimum, c);
		}
		
		printf("Case #%d: ", i+1);
		if(xoring != 0)
			puts("NO");
		else
			printf("%d\n", sum-minimum);
	}
	
	return 0;
}


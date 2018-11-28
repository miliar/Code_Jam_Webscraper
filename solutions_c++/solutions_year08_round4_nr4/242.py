#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b) x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) c.begin(), c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for (VAR(i,c.begin()); i != c.end(); ++i)
#define PB push_back
#define ST first
#define ND second

const int MAXS = 50000+1;
char str[MAXS];

int main() {
	int z;
	scanf("%d",&z);
	FOR(a,1,z+1) { 
		int k;
		scanf("%d\n",&k);
		int ss = 0;
		while ((str[ss] = getchar()) != '\n') {
		  ++ss;
		}
  		int p[5] = {0,1,2,3,4};
		int h = 1000000000;
		do {
			char ns[MAXS];
			for (int i = 0; i < ss; i += k) REP(j,k)
				ns[i+j] = str[i+p[j]];
			int nh = 0;
			for(int i = 0; i < ss; )  {
				int j;
				for (j = i+1; j < ss && ns[j] == ns[i]; ++j);
				//mx = max(mx,j-i);
				i = j;
				++nh;
			}
			h = min(h,nh);
		} while (next_permutation(p,p+k));
		printf("Case #%d: %d\n",a,h);
	}	
	return 0;
}

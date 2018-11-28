// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

struct {
	int pos, time;
} Robot[2];

int Time;

void move(int r, int p) {
	int dt = Time-Robot[r].time;
	int dp = abs(p-Robot[r].pos);
	Time += max(dp-dt,0);
	Robot[r].pos  = p;
	Robot[r].time = ++Time;
}

int main() {
	int T;
    scanf("%d ", &T);
    FORTO(t,1,T) {
		char R; int P, N;
		Time = 1;
		FOR(i,2) Robot[i].pos = Robot[i].time = 1;
		
		scanf("%d ", &N);
		FOR(i,N) {
			scanf("%c %d ", &R, &P);
			if (R == 'O') move(0,P);
			if (R == 'B') move(1,P);
		}
		
		printf("Case #%d: %d\n", t, Time-1);
	}
	return 0;
}


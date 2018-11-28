#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

vector < int > color;
vector < int > pos[2];

int nextTime(int c, int p, int now) {
	if( p >= pos[c].size() ) {
		return 99999;
	}
	else {
		return now+abs(pos[c][p]-pos[c][p-1]);
	}
}

int calc() {
	int p[2] = {1,1}, t[2] = {0,0};
	int now = 0;

	t[0] = nextTime(0, p[0], t[0]);
	t[1] = nextTime(1, p[1], t[1]);

	for(int i=0;i<color.size();i++) {
		if( t[color[i]] > now ) {
			now = t[color[i]]+1;
		} else {
			now = now + 1;
		}
		t[color[i]] = nextTime(color[i], ++p[color[i]], now);
	}
	return now;
}

int main()
{
	int nCase = 1;
	int T, N, p;
	char col[2];

	cin >> T;
	while( T-- > 0 ) {
		cin >> N;
		pos[0].clear();
		pos[1].clear();
		pos[0].push_back(1);
		pos[1].push_back(1);
		color.clear();
		for( int i = 0 ; i < N ; ++i ) {
			cin >> col >> p;
			if( col[0] == 'O' ) {
				color.push_back(0);
				pos[0].push_back(p);
			} else {
				color.push_back(1);
				pos[1].push_back(p);
			}
		}
		printf( "Case #%d: %d\n", nCase++, calc());
	}
	return 0;
}

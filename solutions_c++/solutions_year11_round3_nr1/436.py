#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

char tiles[64][64];

bool possible (int R, int C) {
    for (int i = 0; i<R; ++i)
	for (int j = 0; j<C; ++j) {
	    if (tiles[i][j] == '#') {
		if (i < R-1 and j<C-1 and
		    tiles[i][j+1] == '#' and
		    tiles[i+1][j] == '#' and
		    tiles[i+1][j+1] == '#') 
		{
		    tiles[i][j] = '/';
		    tiles[i+1][j] = '\\';
		    tiles[i][j+1] = '\\';
		    tiles[i+1][j+1] = '/';
		} else {
		    return false;
		}
	    }
	}
    return true;
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int R, C;
	cin >> R >> C;
	for (int i = 0; i<R; ++i)
	    for (int j = 0; j<C; ++j)
		cin >> tiles[i][j];
	
	printf("Case #%d:\n",c);
	if (possible(R,C)) {
	    for (int i = 0; i<R; ++i) {
		for (int j = 0; j<C; ++j) 
		    printf("%c",tiles[i][j]);
		printf("\n");
	    }
	} else {
	    printf("Impossible\n");
	}
    }

    return 0;
}

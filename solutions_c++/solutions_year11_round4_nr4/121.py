#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
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

int P;
bool w[512][512];
vector<int> connect[512];

int own[512];
int threatened[512];

int maxT;

bool IDFS (int curP, int D) {
    if (D == 0 and w[curP][1]) {
	int T = 0;
	for (int i = 0; i<P; ++i) 
	    if (threatened[i] > 0 and !own[i]) T++;
	if (T > maxT) maxT = T;
	return true;
    }
    if (D == 0) return false;

//    cout<<" D = "<<D<<" on planet "<<curP<<endl;

    bool f = false;


    for (int i = 0; i<P; ++i) {
	if (!w[curP][i] or own[i]) continue;
	own[i] = 1;
	for (vi::iterator v = connect[i].begin(); v<connect[i].end(); ++v)
	{
	    threatened[*v]++;
	}
	if (IDFS(i, D-1)) f = true;
	own[i] = 0;
	for (vi::iterator v = connect[i].begin(); v<connect[i].end(); ++v)
	{
	    threatened[*v]--;
	}
    }
    return f;
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int W;
	cin >> P >> W;
	memset(w,0,sizeof(w));
	for (int i = 0; i<P; ++i) 
	    connect[i].clear();
	
	for (int i = 0; i<W; ++i) {
	    string s;
	    cin >> s;
	    istringstream iss(s);
	    int x, y; char c;
	    iss >> x >> c >> y;
	    w[x][y] = w[y][x] = 1;
	    connect[x].push_back(y);
	    connect[y].push_back(x);
	}

	maxT = -1;

	memset(own,0,sizeof(own));
	memset(threatened,0,sizeof(own));
	own[0] = 1;
	for (vi::iterator i = connect[0].begin(); i<connect[0].end(); ++i)
	{
	    threatened[*i]++;
	}
	maxT = 0;
	int D;
	for (D = 0; D<P; ++D) 
	    if (IDFS(0,D)) break;
	

	printf("Case #%d: %d %d\n",c,D,maxT);
    }

    return 0;
}

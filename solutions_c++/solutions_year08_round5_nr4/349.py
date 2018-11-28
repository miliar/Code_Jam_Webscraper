#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define FOR(x,a,b) for(int x=a; x<(b); x++)
#define FI(b) FOR(i,0,b)
#define FJ(b) FOR(j,0,b)
#define FK(b) FOR(k,0,b)
#define FC(b) FOR(c,0,b)
#define EACH(v,it) for(__typeof(v.begin()) it=v.begin(); it!=v.end(); it++)

bool rock[110][110];

int cache[110][110];
int go(int r, int c) {
    if (r<0 || c<0) return 0;
    if (rock[r][c]) return 0;
    if (r == 0 && c == 0) return 1;

    int &ans = cache[r][c];
    if (ans>=0)return ans;

    return ans = (go(r-2,c-1) + go(r-1,c-2)) % 10007;
}

int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
        memset(rock,0,sizeof(rock));
        int rown, coln, rockn;
        cin >> rown >> coln >> rockn;

        for(int i=0; i<rockn; i++) {
            int r,c;
            cin >> r>>c;
            rock[r-1][c-1] = 1;
        }

        memset(cache,-1,sizeof(cache));
		cout << "Case #"<<(c+1)<< ": " << go(rown-1,coln-1) << endl;
	}

}

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(x,a,b) for(int x=a; x<(b); x++)
#define FI(b) FOR(i,0,b)
#define FJ(b) FOR(j,0,b)
#define FK(b) FOR(k,0,b)
#define FC(b) FOR(c,0,b)
#define EACH(v,it) for(__typeof(v.begin()) it=v.begin(); it!=v.end(); it++)

int rown,coln;
int bad[12];

int cache[12][1<<10];

int go(int row, int prevrow) {
    //cout <<"go " << row <<","<<prevrow<<endl;
    if (row == rown) return 0;

    int &ans = cache[row][prevrow];
    if (ans >= 0) return ans;

    ans = 0;
    for(int m=0; m<(1<<10); m++) {
        // Anyone sitting in bad seat?
        if (bad[row] & m) continue;

        // Any neighbors?
        bool works = true;
        for(int j=1; j<coln; j++) {
            if ((m&(1<<j)) && ((m&(1<<(j-1))))) works = false;
            if ((m&(1<<j)) && ((prevrow&(1<<(j-1))))) works = false;
            if ((prevrow&(1<<j)) && ((m&(1<<(j-1))))) works = false;
        }
        if (!works) continue;

        // Good! How many students?
        int cur = 0;
        for(int j=0; j<coln; j++) if ((m&(1<<j))) cur++;

        ans >?= cur+go(row+1, m);
    }

    return ans;
}

int main() {
	int cases;
	cin >> cases;
	for(int c=0; c<cases; c++) {
        cin >> rown >> coln;

        string str;
        for(int i=0; i<rown; i++) {
            cin >> str;
            bad[i] = 0;
            for(int j=0; j<coln; j++) if (str[j] == 'x') bad[i] = (bad[i] | (1<<j));
        }

        memset(cache,-1,sizeof(cache));
		cout << "Case #"<<(c+1)<< ": " << go(0,0) << endl;
	}

}

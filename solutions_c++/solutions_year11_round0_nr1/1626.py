#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

int run(int ncase){
    int i, j, k;
    int N, M;
    string line;
    int button;
    char color;
    int now;
    int opos, bpos;
    int opre, bpre;
    int move;
    int time;

    cin >> N;

    opos = bpos = 1;
    opre = bpre = now = 0;
    FOR(i, 0, N){
        cin >> color;
        cin >> button;

        if(color == 'O'){
            move = abs(opos - button);
            time = move - (now - opre);
            if(time > 0) now += time;
            now++;

            opos = button;
            opre = now;
            
        }else{
            move = abs(bpos - button);
            time = move - (now - bpre);
            if(time > 0) now += time;
            now++;

            bpos = button;
            bpre = now;
        }
    }

    cout << "Case #" << ncase << ": ";
    cout << now << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}

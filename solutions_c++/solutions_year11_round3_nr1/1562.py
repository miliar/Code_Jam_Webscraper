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
#include <cassert>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

int run(int ncase){
    int i, j, k;
    int R, C;
    vector<string> pic;

    cin >> R >> C;
    pic.resize(R);
    FOR(i, 0, R){
        cin >> pic[i];
    }

    int flag = 1;
    FOR(i, 0, R){
        FOR(j, 0, C){
            char c = pic[i][j];
            if(c == '.') continue;

            if(c == '#'){
                pic[i][j] = '/';
                if((i == R-1) || (j == C-1)){
                    flag = 0;
                    break;
                }

                
                if(pic[i][j+1] == '#'){
                    pic[i][j+1] = '\\';
                }else{
                    flag = 0;
                }

                if(pic[i+1][j] == '#'){
                    pic[i+1][j] = '\\';
                }else{
                    flag = 0;
                }

                if(pic[i+1][j+1] == '#'){
                    pic[i+1][j+1] = '/';
                }else{
                    flag = 0;
                }

            }
            if(!flag) break;
        }
        if(!flag) break;
    }



    cout << "Case #" << ncase << ":" << endl;
    if(!flag){
        cout << "Impossible" << endl;
    }else{
        FOR(i, 0, R){
            cout << pic[i] << endl;
        }
    }
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    //cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}

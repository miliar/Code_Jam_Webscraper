#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <numeric>
#include <fstream>
#include <iterator>

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

vector<string> exist;
vector<string> want;

bool cmp(string s){
    vector<string>::iterator it;
    foreach(exist, it){
        if(it->compare(s) == 0) return true;
    }
    return false;
}

int append(string s){
    string tmp;
    int pos;
    int cnt = 0;
    pos = string::npos;
    if(!cmp(s)) { exist.push_back(s); cnt++; }
    while((pos = s.find_last_of('/', pos)) != 0){
        tmp = s.substr(0, pos);
        if(!cmp(tmp)){
            exist.push_back(tmp);
            cnt++;
        }
        pos--;
    }

    return cnt;
}

int run(int ncase){
    int i, j, k;
    int N, M;
    int ans = 0;

    cin >> N >> M;

    exist.resize(N);
    want.resize(M);

    FOR(i, N) cin >> exist[i];
    FOR(i, M) cin >> want[i];

    exist.push_back( string("/") );
    
    vector<string> itr;
    int pos;
    foreach(exist , itr){
        append(*itr);
    }
    /*
    foreach(exist , itr){
        cout << *itr << endl;
    }
    cout << "----------------------" << endl;
    */
    foreach(want , itr){
        ans += append(*itr);
    }
    /*
    foreach(exist , itr){
        cout << *itr << endl;
    }
    cout << "----------------------" << endl;
    */

    cout << "Case #" << ncase << ": ";
    cout << ans << endl;
    return 0;
}

int main() {
    int i, test_set;
    cin >> test_set;
    FOR(i, test_set) run(i+1);
    return 0;
}

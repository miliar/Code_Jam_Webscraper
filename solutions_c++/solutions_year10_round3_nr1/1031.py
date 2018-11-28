#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DPRINT printf
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP(a,b) make_pair(a,b)

int main2(){
    int N; int intersection = 0;
    cin >> N;
    vector<pair<int,int> > wires;
    REP(i,N){
        int tmpA,tmpB;
        cin >> tmpA >> tmpB;
        wires.push_back(MP(tmpA,tmpB));
    }
    REP(i,N) {
        REP(j,N){
            if(i == j) { continue; }
            if((wires[i].first > wires[j].first && wires[i].second > wires[j].second) ||
               (wires[i].first < wires[j].first && wires[i].second < wires[j].second)){
                continue;
            }
            intersection++;
        }
    }
    // TODO.
    return intersection / 2;
}

int main(void){
    int numberOfTestCase;
    cin >> numberOfTestCase;
    REP(i,numberOfTestCase){
        cout << "Case #" << i + 1 << ": ";
        cout << main2() << endl;
    }
    return 0;
}

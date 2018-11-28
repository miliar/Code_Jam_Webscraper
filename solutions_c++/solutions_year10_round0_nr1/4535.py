#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iterator>

using namespace std;

inline void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	//freopen("test.out", "wt", stdout);
#endif
}

void solve();
void solve2(int, int, int);
void snap(bool *, int);
bool isOn(bool *, int);
void printsnappers(bool * , int);
int main() {
	openFiles();
	solve();
	return 0;
} 




void solve2(int n, int k, int nr){
    bool * snappers = new bool[n];
    for (int i = 0; i < k; i++){
        snap(snappers, n);
        //printsnappers(snappers, n);
    };
    cout << "Case #" << nr << ": " << (isOn(snappers, n) ? "ON" : "OFF") << endl;
    
}

void printsnappers(bool * snappers, int n){
    
    for (int i = 0; i < n; i++){
        cout << (snappers[i]  ? "ON " : "OFF ");
    }
    cout << endl;

}

void snap(bool * snappers, int size){
    int i = 0;
    while (snappers[i] && i < size) i ++;
    if (i < size) snappers[i] = true;
    i--;
    while (i >= 0){
        snappers[i] = !snappers[i];
        i--;
    }
}

bool isOn(bool * snappers, int size){
    bool result = true;
    for (int i = 0; i < size && result; i++){
        result &= snappers[i];
    }
    return result;

}
void solve() {
    int nr;
    cin >> nr;
    int n, k;
    
    for (int i = 0; i < nr; i++){
        cin >> n >> k;

        solve2(n, k, i + 1);
    }
}

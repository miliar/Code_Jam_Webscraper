#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> pris;

map<pair<int,int>, long long int> memory;

long long int best (int from, int to) {
    pair<int,int> key = make_pair(from,to);
    if (memory.find(key) != memory.end()) return memory[key];
    
    long long int & res = memory[key];
    if (from > to) return 0;
    int dist = 0;
    vector<int> mp;
    for (int i = 0; i < pris.size(); i++) {
        if (pris[i] >= from && pris[i] <= to) mp.push_back (pris[i]);
    }
    if (mp.size() == 0) return 0;
    long long int b = 10000000;
    b = (to-from)+best(from, mp[0]-1)+best(mp[0]+1, to);
    for (int i = 1; i < mp.size(); i++) {
        b = min (b, (to-from)+best(from, mp[i]-1)+best(mp[i]+1, to));
    }
    res = b;
    return res;
}

using namespace std;
int main () {
    int T,t = 1;
    cin >> T;
    while (T--) {
        int P, Q;
        cin >> P >> Q;
        for (int i = 0 ; i < Q; i++) {
            int p = 0;
            cin >> p;
            pris.push_back (p);
        }
        sort (pris.begin() , pris.end());
        int result = best (1,P);
        cout << "Case #" << t++ << ": " << result << endl;
        pris.clear();
        memory.clear();
    }
    return 0;
}


#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

int idx(char c) {
    return c - 'A';
}

char chr(int idx) {
     return (char)(idx + 'A');
}

int T, C, D, N, comb[100][100], a[1000];
bool opp[100][100];
string s;
deque<int> dq;

void invoke(int v) {
     if (dq.size() == 0) {
        dq.push_back(v);
        return;
     }
     
     int u = dq.back();
     if (comb[u][v] != -1) {
        dq.pop_back();
        invoke(comb[u][v]);
        return;
     }
     
     for (int i = 0; i < dq.size(); ++i) {
         u = dq[i];
         if (opp[u][v]) {
            dq.clear();
            return;
         }
     }
     
     dq.push_back(v);
}

string res() {
       string ret = "[";
       
       while (dq.size() > 1) {
           ret += chr(dq.front());
           ret = ret + ", ";
           dq.pop_front();
       }
       
       if (dq.size() > 0) {
          ret += chr(dq.front());
          dq.pop_front();
       }
       
       ret = ret + "]";
       
       return ret;
}

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        memset(comb, -1, sizeof(comb));
        memset(opp, false, sizeof(opp));

        cin >> C;
        
        for (int i = 1; i <= C; ++i) {
            cin >> s;
            
            int u = idx(s[0]);
            int v = idx(s[1]);
            int x = idx(s[2]);
            
            comb[u][v] = comb[v][u] = x;
        }
        
        cin >> D;
        
        for (int i = 1; i <= D; ++i) {
            cin >> s;
            
            int u = idx(s[0]);
            int v = idx(s[1]);
            
            opp[u][v] = opp[v][u] = true;
        }
        
        cin >> N >> s;
        for (int i = 0; i < N; ++i) a[i] = idx(s[i]);

        dq.clear();
        for (int i = 0; i < N; ++i) {
            //cout << "Invoke " << chr(a[i]) << endl;
            invoke(a[i]);
        }
        
        cout << "Case #" << t << ": " << res() << endl;
    }
                   
    return 0;
}

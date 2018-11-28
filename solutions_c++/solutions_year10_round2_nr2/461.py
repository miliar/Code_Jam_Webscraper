#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
using namespace std;

int main() {
    
    vector<int> x;
    vector<int> v;
    vector<bool> g;
    int C,N,K,B,T;
    ifstream in("in3.in");
    ofstream out("out.txt");
    in >> C;
    int cur,n,s,c;
    for(int k = 1; k <= C; k++) {
        in >> N >> K >> B >> T;
        if (K == 0) {
           out<<"Case #"<<k<<": "<<0<<endl;
        }
        for(int i = 0; i < N; i++) {
            in >> cur;
            x.push_back(cur);
        }
        for(int i = 0; i < N; i++) {
            in >> cur;
            v.push_back(cur);
        }
        for(int i = N - 1; i >= 0; i--) {
            if (v[i] == 0) g.push_back(0);
            else
            if ( (B - x[i])/double(v[i]) <= T ) g.push_back(1);
            else g.push_back(0);
        }
        n = 0;
        c = 0;
        for (int i = 0; i < g.size(); i++) {
            s = 0;
            if (g[i]) {
                for (int j = 0; j < i; j++) {
                    if (!g[j]) s++;
                }
                c++;
                n += s;
                if (c == K) {
                    out<<"Case #"<<k<<": "<<n<<endl;
                    goto hell;
                }
            }
        }
        if (c < K) out<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
        hell:;
        x.clear();
        v.clear();
        g.clear();
    }
}
                
                
    
            
            

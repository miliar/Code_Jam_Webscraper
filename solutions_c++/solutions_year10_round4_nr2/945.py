#include <cstdlib>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
#define FOR(i, n) for(int i=0; i<n; ++i)
#define FORV(i, v) for(int i=0; i<v.size(); ++i)
#define INF 2147483647

using namespace std;

int pow(int a, int b) {
    if(b == 0) return 1;
    else if(b%2) return pow(a, b/2)*pow(a, b/2)*a;
    else return pow(a, b/2)*pow(a, b/2);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    FOR(p, T) {
        int n;
        cin >> n;
        vector <int> M(pow(2, n));
        for(int i=0; i<M.size(); ++i)
            cin >> M[i];
        vector < vector <bool> > P(n);
        for(int i=0; i<P.size(); ++i)
            for(int j=0; j<pow(2, n-i-1); ++j) {
                int t;
                cin >> t;
                P[i].push_back(false);
            }
        int fl, pos;
        for(int i=0; i<M.size(); ++i) {
            fl = 0;
			pos = i/2;
            while(M[i]>0) 
                {fl++; pos /= 2; M[i]--;}
            while(fl<P.size()) 
                {P[fl][pos] = true; fl++; pos /= 2;}
        }
        int res = 0;
        for(int i=0; i<P.size(); ++i)
             for(int j=0; j<P[i].size(); ++j)
                 if(P[i][j]) 
                     res++;
        cout << "Case #" << p+1 << ": " << res << endl;
    }
    
    return 0;
}

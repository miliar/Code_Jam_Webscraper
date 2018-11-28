#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back

int aabs(int a) { return (a<0)?-a:a; }

int p10[8] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        int A, B;
        cin >> A >> B;
        
        int res = 0;
        FOR(n, A, B+1) {
            int d = 0;
            while(n >= p10[d]) d++;
            
            //cout << n << " - " << d << endl;
            
            int aux = n/10 + (n%10)*p10[d-1];
            while(aux != n) {
                //cout << "    " << aux << endl;
                if(n < aux && aux <= B) res++;
                aux = aux/10 + (aux%10)*p10[d-1];
            }
        }
        
        cout << "Case #" << caso+1 << ": " << res << endl;
        
    }
    return 0;
}
    
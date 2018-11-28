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

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        int N, S, p, arr[110];
        cin >> N >> S >> p;
        REP(i, N) cin >> arr[i];
        
        int res = 0;
        REP(i, N) {
            int pos = 0;
            REP(a, 11) REP(b, 11) REP(c, 11) {
                if(a+b+c == arr[i] && (a >= p || b >= p || c >= p) && aabs(a-b) < 3 && aabs(a-c) < 3 && aabs(b-c) < 3) {
                    if(aabs(a-b) == 2 || aabs(a-c) == 2 || aabs(b-c) == 2) {
                        if(pos == 0) pos = 1;
                    } else pos = 2;
                }
            }
            
            if(pos == 2) res++;
            else if(pos == 1 && S > 0) res++, S--;
        }
        
        cout << "Case #" << caso+1 << ": " << res << endl;
    }
    
    return 0;
}

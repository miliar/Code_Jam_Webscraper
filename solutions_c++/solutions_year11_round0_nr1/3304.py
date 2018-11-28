#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))

using namespace std;

int main ()
{
    // freopen("A-sample.in","r",stdin);freopen("A-sample.out","w",stdout);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
        int testcases;

        cin >> testcases;

        int instances;
        int oPos;
        int bPos;
        
        int nextO;
        int nextB;
        
        int step, t;
        
        for(int caseId = 1; caseId <= testcases; ++caseId)
        {
            cin >> instances;
            
            char robot[instances];
            int button[instances];
            
            for (int instanceId = 0; instanceId < instances; ++instanceId) {
                cin >> robot[instanceId];
                cin >> button[instanceId];
            }
            
            oPos = bPos = 1;
            nextO = nextB = -1;
            step = t = 0;
            
            
            for (int i =0; (nextO < 0 || nextB < 0) && i < instances; i++) {
                if (nextO < 0 && robot[i] == 'O') {
                    nextO = button[i];
                } else if(nextB < 0 && robot[i] == 'B') {
                    nextB = button[i];
                }
            }
            
            while (step < instances) {
               int incstep = 0;
                 if (nextO > 0) {
                     if (nextO == oPos) {
                         if (robot[step] == 'O') {
                             ++incstep;
                             nextO = -1;
                             for (int i = step + 1; nextO < 0 && i < instances; ++i) {
                                 if (robot[i] == 'O') {
                                     nextO = button[i];  
                                 }
                             }
                         }
                     } else {
                         oPos += nextO < oPos ? -1 : 1;
                     }
                 }
                 
                 if (nextB > 0) {
                     if (nextB == bPos) {
                         if (robot[step] == 'B') {
                             ++incstep;
                             nextB = -1;
                             for (int i = step+1; nextB < 0 && i < instances; ++i) {
                                 if (robot[i] == 'B') {
                                     nextB = button[i];  
                                 }
                             }
                         }
                     } else {
                         bPos += nextB < bPos ? -1 : 1;
                     }
                 }
                 step += incstep;
                 ++t;
            }

            
            cout << "Case #" << caseId << ": " << t;
             
            cout << endl;
        }

        return 0;
    }
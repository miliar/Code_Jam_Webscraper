#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>

using namespace std;

#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector <int> vi;
typedef vector <long long> vll;
typedef pair <int, int> pii;

int X, S, R, t, N;
int B[1000], E[1000], w[1000];

bool myfunction (pair<int,int> i,pair<int,int> j) { return (i.second<j.second); }

int main ()
{
    int tn;
    scanf("%d", &tn);
    forab(tt, 1, tn)
    {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        
        forn(i, N)
        {
            scanf("%d%d%d", &B[i], &E[i], &w[i]);
        }
        
        int lastPos = 0;
        double result = 0;
        vector <pair<int, int> > runs;
        
        forn(i, N)
        {
            if(B[i] > lastPos)
                runs.pb(mp(B[i]-lastPos, S));
            lastPos = B[i];
            if(E[i] > lastPos)
                runs.pb(mp(E[i]-lastPos, w[i]+S));
            lastPos = E[i];
        }
        if(X > lastPos)
            runs.pb(mp(X-lastPos, S));
        
        sort(all(runs), myfunction);
        
        double runBudget = (double)t;
        forn(i, sz(runs)) {
            
            double fast = (double)runs[i].second+(double)(R-S);
            double max = runBudget*fast; //distance
            
            if(runBudget > 0 && max >= (double)runs[i].first) {
                double used = (double)runs[i].first/fast;
                runBudget -= used;
                result += used;
            } else {
                double rem = (runBudget > 0) ? (double)runs[i].first-max : (double)runs[i].first;
                result += (runBudget > 0) ? max/fast : 0;
                result += rem/(double)runs[i].second;
                runBudget = 0;
            }
            
        }
        
        printf("Case #%d: %.10f\n", tt, result);
        fflush(stdout);
    }

    return 0;
}

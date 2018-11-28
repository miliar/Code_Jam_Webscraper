#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int main(void) {
    int L,D,N; 
    cin >> L >> D >> N;

    vector<string> data(D);
    FOR(i,D) {
        cin >> data[i];
    }

    vector<string> dict(L);
    FOR(i,N) {
         
        string d;
        cin >> d;

        int idx=0;
        FOR(j, d.size())
        {
            if (d[j] == '(') {
                int next = d.find(')', j);
                dict[idx++] = d.substr(j+1,  next - j - 1);
                j = next;
            }
            else 
                dict[idx++] = d.substr(j, 1);
        }

        int res = 0;
        FOR(j, D) {
            bool ok = true;
            FOR(k, L) {
                if (dict[k].find(data[j][k]) == -1) {
                    ok = false;
                    break;
                }
            }
            if (ok) ++res;
        }

        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}

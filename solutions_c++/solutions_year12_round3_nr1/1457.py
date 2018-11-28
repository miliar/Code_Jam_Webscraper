#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

#define REP(i,n) for(i=0;i<n;i++)
#define gout case_number++, printf("Case #%d: ",case_number), cout
int case_number;
void main23();

int main()
{
    int test_case, t;
    scanf ("%d", &test_case);

    for(t = 0; t < test_case; t++)
    {
            int i, j, k, n, adj[1001][1001];

            REP(i,1001) REP(j,1001) adj[i][j] = 12435678;
            scanf ("%d", &n);
            REP(i,n){
                int x, y;
                scanf ("%d", &x);
                REP(j,x){
                    scanf ("%d", &y);
                    adj[i][y-1] = 1;
                }
            }

            bool succ = false;
            REP(k,n) REP(i,n) REP(j,n) {

                int count = 0;
                if (adj[i][j] < 12345678) count++;
                if ((adj[i][k] + adj[k][j]) < 12345678) count++;
                if (count == 2){ succ = true; break; }

                adj[i][j] = min (adj[i][j], adj[i][k] + adj[k][j]);
            }

            if (succ) gout << "Yes\n";
            else gout << "No\n";
    }


    return 0;
}

#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

char adj[30][30];
int oppose[30][30];
char buff[111];

int main()
{
    int t;
    scanf("%d", &t);
    FOR(testcase, 0, t){
        int c, d, n;
        memset(adj, -1, sizeof(adj));
        memset(oppose, 0, sizeof(oppose));

        scanf("%d", &c);
        FOR(i, 0, c){
            scanf("%s", buff);
            adj[buff[0] - 'A'][buff[1] - 'A']  = adj[buff[1] - 'A'][buff[0] - 'A'] = buff[2];
        }

        scanf("%d", &d);
        FOR(i, 0, d){
            scanf("%s", buff);
            oppose[buff[0] - 'A'][buff[1] - 'A']  = oppose[buff[1] - 'A'][buff[0] - 'A'] = 1;
        }

        int pos = 0;
        int ret[111];
        int ele[30];
        memset(ele, 0, sizeof(ele));

        scanf("%d %s", &n, buff);
        FOR(i, 0, n){
            if(pos > 0 && adj[ret[pos - 1] - 'A'][buff[i] - 'A'] != -1){
                ele[ret[pos - 1] - 'A']--;
                ret[pos - 1] = adj[ret[pos - 1] - 'A'][buff[i] - 'A'];
            } else {
                bool clear = false;
                FOR(j, 0, 30) 
                    if(oppose[buff[i]-'A'][j] && ele[j] > 0){
                        clear = true;
                        break;
                    }

                if(clear){
                    memset(ele, 0, sizeof(ele));
                    pos = 0;
                } else {
                    ret[pos++] = buff[i];
                    ele[buff[i] - 'A']++;
                }
            }
        }

        printf("Case #%d: [", testcase + 1);
        FOR(i, 0, pos){
            printf("%c", ret[i]);
            if(i + 1 < pos) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}


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

#define FOR(A, B) for(int A = 0; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

struct cost {
    int gosta[100];
    int malt[100];
    int pos;
};

cost costs[120];
int n, m;
bool solut;
int solution[20];

void generate(int flavs[20], int pos)
{
    if(pos == n){
        int qtos = 0;
        FOR(i, m){
            FOR(j, costs[i].pos)
                if(flavs[costs[i].gosta[j]] == costs[i].malt[j]){
                    qtos++;
                    break;
                }
        }
        if(qtos == m){
            solut = true;
            FOR(i, n) solution[i] = flavs[i];
        }
        return;
    }
    if(solut) return;
    flavs[pos] = 0;
    generate(flavs, pos + 1);
    if(solut) return;
    flavs[pos] = 1;
    generate(flavs, pos + 1);
}

int main()
{
    int t;
    scanf("%d", &t);
    FOR(casos, t){
        scanf("%d %d", &n, &m);
        FOR(i, m){
            int flav;
            scanf("%d", &flav);
            costs[i].pos = 0;
            FOR(j, flav){
                int x, y;
                scanf("%d %d", &x, &y);
                costs[i].gosta[costs[i].pos] = x - 1;
                costs[i].malt[costs[i].pos] = y;
                costs[i].pos++;
            }
        }
        int flavs[20];
        solut = false;
        generate(flavs, 0);
        printf("Case #%d:", casos + 1);
        if(!solut)
            printf(" IMPOSSIBLE\n");
        else {
            FOR(i, n)
                printf(" %d", solution[i]);
            printf("\n");
        }
    }
    return 0;
}


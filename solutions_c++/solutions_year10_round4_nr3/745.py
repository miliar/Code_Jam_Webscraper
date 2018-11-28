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

int r;
set< pii > bact;
set< pii > newbact;
set< pii >::iterator it;

int solve()
{
    int seconds = 0;
    while(!bact.empty()){
        newbact.clear();

        for(it = bact.begin(); it != bact.end(); it++){
            pii b = (*it);

            // nao morre
            if(bact.find(make_pair(b.first - 1, b.second)) != bact.end() 
                || bact.find(make_pair(b.first, b.second - 1)) != bact.end())
                newbact.insert(b);

            // surge outra
            if(bact.find(make_pair(b.first + 1, b.second - 1)) != bact.end())
                newbact.insert(make_pair(b.first + 1, b.second));
        }

        bact.clear();
        bact = newbact;
        seconds++;
    }
    return seconds;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    FOR(testcase, 0, cases){
        int x1, y1, x2, y2;
        scanf("%d", &r);
        FOR(tmp, 0, r){
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            FOR(i, x1, x2 + 1)
                FOR(j, y1, y2 + 1)
                    bact.insert(make_pair(i, j));
        }

        printf("Case #%d: %d\n", testcase + 1, solve());
    }
    return 0;
}


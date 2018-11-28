#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

long long N;
int T, PD, PG;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for(int cas = 1; cas <= T; cas++){
        cin >> N >> PD >> PG;
        bool ok = false;
        if(PG == 0 || PG == 100){
            ok = (PG == PD);
        } else{
            for(int i = 1; i <= N && !ok; i++){
                if(PD*i%100) continue;
                for(int j = i; !ok && j < 10000; j++){
                    if(PG*j%100) continue;
                    if(PG*j < PD*i) continue;
                    ok = true;
                }
            }
        }
        printf("Case #%d: ", cas);
        if(ok)puts("Possible");
        else puts("Broken");
    }
    return 0;
}

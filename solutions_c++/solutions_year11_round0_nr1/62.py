#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        int T;
        cin>>T;
        int B = 1, O = 1, BT = 0, OT = 0, P;
        char C;
        while (T--) {
            cin>>C>>P;
            if (C == 'B') {
                BT += abs(P - B) + 1;
                BT = max(BT, OT + 1);
                B = P;
            }
            if (C == 'O') {
                OT += abs(P - O) + 1;
                OT = max(OT, BT + 1);
                O = P;
            }
        }
        printf("Case #%d: %d\n", caseN + 1, max(BT, OT));
    }
    return 0;
}

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
        int N, t;
        int m = 10000000, tot = 0, sum = 0;;
        cin>>N;
        while (N--) {
            cin>>t;
            tot ^= t;
            m <?= t;
            sum += t;
        }
        printf("Case #%d: ", caseN + 1);
        if (tot)
            puts("NO");
        else
            printf("%d\n", sum - m);
    }
    return 0;
}

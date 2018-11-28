#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
using namespace std;
int Case = 1, T, N, S, p, t[105];
int main(){
    freopen("a.out", "w", stdout);
    cin >> T;
    while(T--){
        cin >> N >> S >> p;
        for(int i = 0; i < N; i++)
            cin >> t[i];
        int ans = 0;
        for(int mask = 0; mask < (1 << N); mask++)if(__builtin_popcount(mask) == S){
            int cur = 0;
            for(int i = 0; i < N; i++){
                bool foundsurp = false, foundnot = false, sup = false, notSup = false;
                for(int p1 = 0; p1 <= 10; p1++)
                for(int p2 = 0; p2 <= 10; p2++){
                    if(p1 + p2 > t[i])continue;
                    int p3 = t[i] - p1 - p2;

                    if(abs(p1 - p2) > 2 || abs(p2 - p3) > 2 || abs(p3 - p1) > 2)continue;
                    if(abs(p1 - p2) == 2 || abs(p2 - p3) == 2 || abs(p3 - p1) == 2){
                        foundsurp = true;
                        sup |= p1 >= p || p2 >= p || p3 >= p;
                    }else{
                        foundnot = true;
                        notSup |= p1 >= p || p2 >= p || p3 >= p;
                    }
                }
                if(mask & (1 << i)){
                    if(!foundsurp)cur = -1 << 20;
                    else cur += sup;
                }
                else{
                    if(!foundnot)cur = -1 << 20;
                    else cur += notSup;
                }
            }
            ans = max(ans, cur);
        }
        printf("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}
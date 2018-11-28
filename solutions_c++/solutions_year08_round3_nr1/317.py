#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

int fre[1000];

int main() {
    int N;
    cin >> N;
    int num = 0;
    while( num < N ) {
        int P,K,L;
        cin >> P >> K >> L;
        int i;
        for( i = 0; i < L; i++ ) cin >> fre[i];
        sort(fre,fre+L);
        long long res = 0;
        long long tip = 1;
        int id = 0;
        if( P*K < L ) printf("Case #%d: Impossible\n",num+1);
        else {
            for( i = L-1; i > -1; i-- ) {
                if( id == K ) {
                   tip++;
                   id = 0;
                }
                res += tip*fre[i];
                id++;
            }
            printf("Case #%d: %I64d\n",num+1,res);
        }
        num++;
    }
    system("pause");
    return 0;
}

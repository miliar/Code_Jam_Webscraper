#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <set>
#include <stack>
#define pb push_back
#define fs first
#define sc second

using namespace std;

int gcd (int a, int b ){
    if ( !b ) return a;
    return gcd(b, a%b);
}

int main(void){
    int test;
    scanf ("%d", &test);

    for (int _test=0;_test<test;++_test){
        int n, l, h, tmp;

        scanf ("%d %d %d", &n, &l, &h);
        vector <int> nums;
        for (int i=0;i<n;++i){
            scanf ("%d", &tmp);
            nums.pb(tmp);
        }
        int res = -1;
        for (int i=l;i<=h;++i){
            bool ok = true;
            for (int j=0;j<nums.size();++j){
                if ( !(i % nums[j] == 0 || nums[j] % i == 0 )){
                    ok = false;break;
                }
            }
            if ( ok ){
                res = i;break;
            }
        }

        if ( res == -1 ) printf ("Case #%d: NO\n", _test+1);
        else printf ("Case #%d: %d\n", _test+1, res);

    }

    return 0;
}

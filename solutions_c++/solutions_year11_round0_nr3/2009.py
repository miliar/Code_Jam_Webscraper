#include <iostream>
#include <stdio.h>
#include <cmath>
#include <climits>
using namespace std;
int n,ntest,now,res ,sum;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> ntest;
    for(int i = 0;i<ntest; i++){
        cin >> n; now = INT_MAX/2;
        res = -1; sum = 0;
        while (n--){
            int x;
            cin >> x;
            now = min(now,x);
            if (res == -1) res = x; else res^=x;
            sum += x;
        }
        cout << "Case #" << i+1 << ": ";
        if (!res) cout << sum - now << endl;
          else cout << "NO" << endl;
    }
    //cout << "Hello world!" << endl;
    return 0;
}

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1010;


int a[maxn];
int n;


int main(){
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;

    cin >> T;

    for(int t = 1; t <= T; t ++){
        cin >> n;
        int tmp = 0;
        for(int i =  0; i < n; i ++){
            scanf("%d", &a[i]);
            tmp ^= a[i];
        }

        cout << "Case #" << t << ": ";

        if(tmp != 0){
            cout << "NO" << endl;
            continue;
        }
        sort(a, a + n);

        long long ret = 0LL;
        for(int i = 1; i < n; i ++)
            ret += a[i];

        cout << ret << endl;
    }

    return 0;
}

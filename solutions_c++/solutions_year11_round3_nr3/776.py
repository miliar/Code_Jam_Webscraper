#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 1010;

int n, L, H;
int a[maxn];


int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;

    cin >> T;

    for(int t = 1; t <= T; t ++){
        cin >> n >> L >> H;

        for(int i = 0; i < n; i ++)
            cin >> a[i];

        int ret = -1;
        for(int i = L; i <= H; i ++){
            bool flag = true;
            for(int j = 0; j < n; j ++){
                if(i % a[j] != 0 && a[j] % i !=  0){
                    flag = false;
                    break;
                }
            }
            if(flag){
                ret = i;
                break;
            }
        }

        cout << "Case #" << t << ": ";
        if(ret == -1)
            cout << "NO" << endl;
        else
            cout << ret << endl;
    }
}

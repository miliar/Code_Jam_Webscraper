#include <iostream>
#include <memory.h>
#include <deque>
#include <stdio.h>

using namespace std;
#define For(i, x, n) for (int i = (x); i < (n); ++i)
const int Inf = 1e9;
#define x first
#define y second
#define pb push_back

string a[2];
int t, n, k;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    a[0] = "ON";
    a[1] = "OFF";
    cin >> t;
    For (i, 0, t){
        cin >> n >> k;
        printf("Case #%d: ", i + 1);
        cout << a[(k % (1 << n)) != (1 << n) - 1] << endl;
    }
    return 0;
}

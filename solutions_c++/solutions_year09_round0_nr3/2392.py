#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;



int a[505][20];
char c[20] = "welcome to code jam";
int t;
char s[1000];

int rec(int x, int y){
//cout << x << " " << y << endl;
    if (y == -1) return 1;
    if (x < 0) return 0;
    if (a[x][y] != -1) return a[x][y];
    a[x][y] = rec(x - 1, y);
    if (c[y] == s[x]) a[x][y] += rec(x - 1, y - 1);
    a[x][y] %= 10000;
    return a[x][y];
}


int main(){
    cin >> t;
    gets(s);
    for (int _i = 0; _i < t; ++_i){
        memset(a, 255, sizeof(a));
        gets(s);
        cout << "Case #" << _i + 1 << ": ";
        int ans = rec(strlen(s), 18);
        if (ans < 1000) cout << 0;
        if (ans < 100)  cout << 0;
        if (ans < 10) cout << 0;
        cout << ans << endl;
   }
   return 0;
}
#include <iostream>
using namespace std;
const int N = 1000;
int a[N], b[N];
int n, total;
int i, j;

void init(){
    cin >> n;
    for (i=0;i<n;i++){
        cin >> a[i] >> b[i];
    }
    for (i=0;i<n-1;i++)
        for (j=i+1;j<n;j++)
            if (a[i]>a[j]) swap(a[i], a[j]), swap(b[i], b[j]);
    total = 0;
}

void solve(){
    for (i=0;i<n-1;i++)
        for (j=i+1;j<n;j++)
            if (b[i]>b[j]) total++;
}

int main(){
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=1;i<=T;i++){
        init(); solve();
        printf("Case #%d: %d\n", i, total);
    }
}

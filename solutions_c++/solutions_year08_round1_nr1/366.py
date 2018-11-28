#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    //*
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.txt", "w", stdout);
    //*/
    int kase, i, j, ks, n;
    int a[810], b[810];
    cin >> kase;
    for(ks = 1; ks <= kase; ks++){
        cin >> n;
        for(i = 0; i < n; i++)
            cin >> a[i];
        for(i = 0; i < n; i++)
            cin >> b[i];
        sort(a, a+n);
        sort(b, b+n);
        long long sum =0;
        for(i = 0, j = n-1; i < n; i++, j--){
            sum += a[i]*b[j];
        }
        //Case #1: -25
        cout << "Case #" << ks << ": " << sum << endl;
    }
    //system("pause");
    return 0;
}

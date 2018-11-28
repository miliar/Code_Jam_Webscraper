#include<iostream>
#include<algorithm>
#include<fstream>
#define cout fout
using namespace std;
long long n,d;
long long a[10001],b[10001];
long long v[10001];
int main(){
    ofstream fout("a.out");
    int t;
    cin >> t;
    for (int kk = 1; kk<=t; ++kk){
        cin >> n;
        for (int i = 0; i < n; ++i){
            cin >> a[i] >> b[i];
        }
        cin >> d;
        memset(v,0,sizeof v);
        a[n] = d;
        b[n] = d;
        v[0] = min(a[0],b[0]);
        for (int i = 0; i < n; ++i)
        if (v[i])
        {
//            cout << i << endl;
            for (int j = i+1; j <=n; ++j){
                if (a[i]+v[i]>=a[j] && !v[j]){
                    v[j] = min(a[j]-a[i],b[j]);
                 //   cout << j << " "<< v[j]<<endl;
                }
            }
        }
        cout << "Case #" << kk <<": ";
        if (v[n]){
            cout << "YES" << endl;
        } else{
            cout << "NO" << endl;
        }
    }
}

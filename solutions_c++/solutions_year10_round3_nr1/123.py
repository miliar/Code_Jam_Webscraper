#include <iostream>
using namespace std;
int main()
{
    int n0; int nn; cin>> nn; for (n0 = 1; n0<=nn; n0++) {
        int n;
        cin >> n ;
        int x[1100],y[1100];
        for (int i = 0 ; i<n; i++) cin >> x[i] >> y[i];
        for (int i = 0 ; i< n; i++)
          for (int j = i+1; j <n; j++)
            if (x[i]>x[j]) {
              int t = x[i]; x[i] =x[j]; x[j]=t;
              t=y[i]; y[i]=y[j]; y[j] =t;
            }
        int ans = 0 ;
      //  for (int i = 0; i<n; i++) cout << x[i] << "." << y[i] << endl;
        for (int i = 0 ; i<n; i++) 
          for (int j = 0 ;j<i; j++)
            if (y[j]>y[i]) ans ++;
        cout << "Case #"<<n0<<": "<<ans<<endl;
    }
}

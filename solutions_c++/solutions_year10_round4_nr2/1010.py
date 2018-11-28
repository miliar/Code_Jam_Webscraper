#include <iostream>
using namespace std;
int min(int a, int b) {return (a<b)?a:b; }
int main()
{
     int tt; cin >> tt ; for (int  t0 = 1; t0<=tt; t0++) {
         int p ;
         cin >> p ;
         int a[3000];
         int E = 1 << p;
         for (int i = 0 ; i< E; i++)
            cin >> a[i];
         int ans;
         int tmp;
         for (int i = 1 ; i <E; i++) cin >> tmp;
         int H = 0;
         ans = 0 ;
         while (H<E-1) {
           int q = min (a[H],a[H+1]);
           if (q <=0) ans ++;
           if (q ==0 ) q  =1 ;
           a[E++] = q-1;
           //cout << "ADD" << q-1 << endl;
           H+=2;
         }

         cout <<"Case #"<<t0 <<": "<<ans << endl;
     }
}

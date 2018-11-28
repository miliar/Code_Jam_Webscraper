#include <iostream>
int max(int a, int b) { return (a<b)?(b):a; }
int ABS(int a) {return (a<0)?-a:a;}
using namespace std;
int main() {
  int TT;
  cin >>TT;
  for (int tc = 1 ; tc<=TT; tc++) {
     int ans = 0 ;
     int fra = 0, frb = 0;
     int pa = 1, pb =1;
     int n;
     cin >> n;
     for (int i = 0 ; i <n; i++) {
       string A; int D;
       cin >> A >> D;
       if (A[0]=='O') {
          fra = max(frb+1,fra+ABS(D-pa)+1);          pa = D;
         // cout <<"hereA"<<fra<<" "<<frb<<endl;

       }
       else {
          frb = max(fra+1,frb+ABS(D-pb)+1);          pb = D;
           //         cout <<"hereB"<<fra<<" "<<frb<<endl;

       }
     }
     cout <<"Case #"<<tc<<": "<< max(fra,frb) << endl;
  }
}

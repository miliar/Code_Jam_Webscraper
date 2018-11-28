#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

long long tab[10000][2];


int main() {

long long n;
long long tst;
tst = 0;
long long x0,y0,A,B,C,D;
long long M;
    long long wyn;
cin >> tst ;
for(int u=0;u<tst;u++) {
cin >> n;
cin >> A;
cin >> B;
cin >> C;
cin >> D;
cin >> x0;
cin >> y0;
 //cout << "Case #" << tst << ": " << wyn << "\n";
cin >> M;

// cout << "Case #" << tst << ": " << wyn << "\n";
  wyn = 0;
long long X = x0;
long long Y = y0;
tab[0][0] =  X;
tab[0][1]  = Y;
for(int i = 1;i<=n-1;i++) {
  X = (A * X + B) % M ;
  Y = (C * Y + D) % M ;
  tab[i][0] =  X;
  tab[i][1] = Y;
}

for(int i = 0 ; i<=n-1; i++ ) {
 // cout << i << "\n";
for(int j = i+1 ; j<=n-1; j++ ) {
   // cout << j << " \n";
for(int t = j+1 ; t<=n-1; t++ ) {

   if (((tab[i][0] + tab[j][0] + tab[t][0]) % 3  == 0)
    && ((tab[i][1] + tab[j][1] + tab[t][1]) % 3  == 0))
    wyn++;

}
}

}
//wyn -= n;
  cout << "Case #" << u+1 << ": " << wyn << "\n";
}


return 0;
}

#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

long long A[600000];
  long long tab[600000];
    long long odp[600000];
int main() {

long long n;
long long tst;
tst = 0;
long long x0,y0,X,Y,Z,m;
long long M,K,pula;
    long long wyn;
cin >> tst ;
for(long long u=0;u<tst;u++) {
cin >> n;
cin >> m;
cin >> X;
cin >> Y;
cin >> Z;
for(long long i=0;i<n;i++) {
  A[i] = 0;
  tab[i] = 0;
}

for(long long i=0;i<m;i++) {
  cin >> A[i];
}

for(long long i = 0;i<=n-1;i++) {
  tab[i] = A[i % m];
  A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;

}
wyn = 0;

for(long long i = 0;i<=n-1;i++) {
  odp[i] = 1;
}

for(long long i = 0; i<=n-1; i++) {
  for(int j = 0;j < i; j++) {
     if (tab[j] < tab[i]) {
        odp[i] += odp[j];
        odp[i] %= 1000000007LL;
     }
  }
}
 for(long long i = 0;i<=n-1;i++) {
  wyn+=odp[i];
  wyn %= 1000000007LL;
}
  cout << "Case #" << u+1 << ": " << wyn << "\n";
}


return 0;
}

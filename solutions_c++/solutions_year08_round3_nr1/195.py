#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

vector<long long> tab;


int main() {

long long n;
long long tst;
tst = 0;
long long x0,y0,K,L;
long long P;
    long long wyn;
cin >> tst ;
for(int u=0;u<tst;u++) {
//cin >> n;
wyn = 0;
cin >> P;
cin >> K;
cin >> L;
long long a;
tab.clear();
 for(int i=0;i<L;i++) {
   cin >> a;
   tab.push_back(a);
 }
 sort(tab.begin(),tab.end());
 long long ile;
 ile = K;
 long long licznik;
 licznik = 1;
 for(int i=L-1;i>=0;i--) {
   wyn += licznik*tab[i];
   ile--;
   if (ile==0) {ile=K;licznik++;}
 }
  cout << "Case #" << u+1 << ": " << wyn << "\n";
}


return 0;
}

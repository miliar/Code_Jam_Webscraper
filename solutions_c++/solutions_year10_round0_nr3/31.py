#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<ctime>
using namespace std;
const int INF = 2147483647;
const double PI = 3.141592653589793;

long long res,temp;
int q,z,r,k,n,tab[1005],nex[1005],s[1005],ind,suma,i,akt,g;
bool bylo[1005];

int next (int a) {
    return (a+1) % n;
}

int main() {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d %d",&r,&k,&n);
    for (i=0;i<n;i++) {
        scanf ("%d",&tab[i]);
        nex[i]=-1; s[i]=-1; bylo[i]=false;
    }
    for (i=0;i<n;i++) {
        suma = tab[i];
        akt = i;
        while (next(akt)!=i && suma + tab[next(akt)] <= k) {
              akt = next(akt);
              suma += tab[akt];
        }
        s[i]=suma;
        nex[i]=next(akt);
    }
    i=0; res=0;
    while (r>0 && !bylo[i]) {
          bylo[i]=true;
          res+=s[i];
          i=nex[i];
          r--;
    }
    if (r>0) {
       ind = i; temp=0; g=0;  
       do {
           temp += s[i];
           i=nex[i];
           g++;
       }     
       while (i!=ind);
       res += temp * (r/g);
       r%=g;
       while (r>0) {
          res+=s[i];
          i=nex[i];
          r--;
       }       
    }
    cout << "Case #"<< q << ": " << res << endl;        
}
return 0;
}

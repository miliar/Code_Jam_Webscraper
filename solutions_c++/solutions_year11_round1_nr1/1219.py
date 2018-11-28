#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

void eea (long long a, long long b,
        long long& gcd, long long& x, long long& y) {
        x=0, y=1; 
        int u=1, v=0, m, n, q, r;
        gcd = b;
        while (a!=0) {
                q=gcd/a; r=gcd%a;
                m=x-u*q; n=y-v*q;
                gcd=a; a=r; x=u; y=v; u=m; v=n;
        }
}
void solve(int t)
{
long long N, PD, PG, gcd, x, y, TD, TG;
cin >> N;
cin >> PD;
cin >> PG;
eea(PD, 100, gcd, x, y);
if(PD)TD=100/gcd;
else TD=0;
eea(PG, 100, gcd, x, y);
if(PG)TG=100/gcd;
else TG=0;
//eea(PG, 100, gcd, x, y);
//if(PG)TG=100/gcd;
cout << "Case #" << t << ": ";
if(TD<=N && (PG!=100 || PD==100) &&(PG!=0 || PD==0))
cout << "Possible";
else
cout << "Broken";
#if 0
cout << " " << N << " "<<PD<<" "<<PG;
if(PD>=PG)cout << " "<<TD;
#endif
//cout << x << " " << y;
//cout << TD;
cout << endl;
}


int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}

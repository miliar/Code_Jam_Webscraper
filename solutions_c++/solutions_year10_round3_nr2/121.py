#include <iostream>
using namespace std;
int calc(long long  a,long long  b, int c) {
    if (b<=a*c) return 0;
    long long  b1 = b; long long  a1 =a;
    while (b1>a1) {
          b1/=c; a1*=c;
    }
    //a1>=b1;
    int t1 = calc(a,a1,c);
    int t2 = calc(a1,b,c);
    return (t1<t2)?t2+1:t1+1;
}
int main()
{
    int n0; int nn; cin>> nn; for (n0 = 1; n0<=nn; n0++) {
        int n;
        int L,P,C;
        cin >> L >> P >>C;
      int   ans= calc(L,P,C);
        cout << "Case #"<<n0<<": "<<ans<<endl;
    }
}

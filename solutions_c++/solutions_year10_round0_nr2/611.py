#include <gmp.h>
#include <gmpxx.h>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef mpz_class GMP;
typedef vector<GMP> VGMP;

GMP gcd(GMP a, GMP b) {
    if(a==0 || b==0) return a|b;
    return gcd(b,a%b);
}

template<typename T>
T mabs(T n) {
    if(n<0) return -n;
    return n;
}

GMP _abs(GMP a) {
    if(a<0) return -a;
    return a;
}

void doit(int kase) {
    int n;
    printf("Case #%d: ",kase);
    scanf("%d",&n);
    cerr << "n = " << n << endl;
    if(n==-1) {
        assert(0);
    }else {
        VGMP v;
        for(int i=0;i<n;i++) {
           GMP in;
           cin >> in;
//           cerr << "got: " << in << endl;
           v.push_back(in);
        }
        VGMP w;
        for(int i=0;i<n-1;i++)
            for(int j=i+1;j<n;j++)
                w.push_back(_abs(v[i]-v[j]));
        GMP g = 0,o;
        for(int i=0;i<(int)w.size();i++) g = gcd(g,w[i]);
        o = (g - v[0] % g) % g;
//        for(int i=0;i<(int)w.size();i++) assert(o == g-v[i]%g);
        //if(g==1) o = 0;
        cout << o << endl;
    }
}


int main(){
    int N;
    cin >> N;
    for(int i=1;i<=N;i++) doit(i);
    return 0;
}

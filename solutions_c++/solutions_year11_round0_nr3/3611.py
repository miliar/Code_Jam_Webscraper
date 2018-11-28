#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

typedef pair<char, int> PCI;
typedef vector<PCI> VPCI;
typedef vector<int> VI;

#define D 0

void do_case(int cn) {
    int n;
    int mxor = 0;
    cin >> n;
    int a[n];
    int ma = -1;
    int mi = 1<<30;
    int mmsum = 0;
    for(int i=0;i<n;i++) {
        int in;
	cin >> in;
        mxor = mxor ^ in;
        a[i] = in;
        mmsum += in;
        mi = min(mi, in);
    }
    /*
    for(int i=1;i<((1<<n)-1);i++) {
        int suma, sumb, SumA, SumB;
        suma=sumb=SumA=SumB=0;
        for(int j=0;j<n;j++) 
            if(i&(1<<j)) {
                suma = suma^a[j];
                SumA += a[j];
            } else {
                sumb = sumb^a[j];
                SumB += a[j];
            }
        if(suma==sumb) ma = max(max(SumA, SumB), ma);
    }
    */
    //if(ma == -1) { 
    if(mxor) { 
         assert(mxor); 
         printf("Case #%d: NO\n", cn);
    } else {
//        assert(ma == (mmsum - mi));
        printf("Case #%d: %d\n", cn, mmsum - mi);
	assert(!mxor);
    }
}

int main() {
    int N;
    cin >> N;
    for(int i=1;i<=N;i++) do_case(i);
    return 0;
}

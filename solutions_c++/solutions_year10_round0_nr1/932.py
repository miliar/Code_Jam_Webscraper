#include<iostream>
using namespace std;

int data,N,M,K;

int main() {
    freopen("al.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>data;
    while (data--) {
        cin>>K>>N; M++;
        int t=0;
        for (int i=0; i<K; i++) if (N&1) {
            t++; N=N/2;
        } else break;
        printf("Case #%d: ",M);
        if (t==K) puts("ON"); else puts("OFF");
    }
    return 0;
}

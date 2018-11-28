#include<iostream>
using namespace std;

const int maxN=1000+1;

int data,M,R,k,N,j;
int B[maxN];
long long ans,A[maxN],C[maxN];

int main() {
    freopen("cs.in","r",stdin);
    freopen("b.out","w",stdout);
    cin>>data; 
    while (data--) {
        cin>>R>>k>>N; M++;
        ans=j=0;
        for (int i=0; i<N; i++) {
            cin>>A[i]; A[i+N]=A[i];
            if (A[i]>k) puts("asdfads");
        }
        for (int i=0; i<N; i++) {
            long long t=A[i]; int j=i;
            while (j-i+1<N && t+A[j+1]<=k) t+=A[++j];
            B[i]=j; C[i]=t;
        }
        //for (int i=0; i<N; i++) cout<<B[i]<<' '<<C[i]<<endl;
        for (int i=0; i<R; i++) {
            ans+=C[j];
            j=(B[j]+1)%N;
        }
        printf("Case #%d: ",M);
        cout<<ans<<endl;
    }
    return 0;
}

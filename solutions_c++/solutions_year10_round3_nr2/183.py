#include<iostream>

using namespace std;

const int maxN=1000+1;

int data,N,A[maxN][2],ans;

int main() {
    freopen("al.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>data;
    for (int T=1; T<=data; T++) {
        printf("Case #%d: ",T);
        cin>>N;
        ans=0;
        for (int i=1; i<=N; i++) cin>>A[i][0]>>A[i][1];
        for (int i=1; i<=N; i++) 
            for (int j=1; j<=N; j++)
                ans+=((A[i][0]-A[j][0])*(A[i][1]-A[j][1])<0);
        printf("%d\n",ans/2);
    }
    return 0;
}

#include <iostream>
using namespace std;
int A[100000];
int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int T;
    cin>>T;
    for(int tc = 1; tc <= T; tc++) {
        cout<<"Case #"<<tc<<": ";
        int N,L,H;
        cin>>N>>L>>H;
        for(int i = 0; i <  N; i++) cin>>A[i];
        int res = -1;
        for(int i = L; i <= H; i++) {
            int ok = 1;
            for(int j = 0; j < N; j++) {
                if(A[j]==0) {
                    continue;
                }
                if(i%A[j]!=0&&A[j]%i!=0) ok = 0;
            }
            if(ok){
                res=i;
                break;
            }
        }
        if(res==-1)cout<<"NO"<<endl;
        else cout<<res<<endl;
    }
}

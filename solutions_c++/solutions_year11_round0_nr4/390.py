#include <iostream>
typedef unsigned int uint;
using namespace std;

int main(){
    int T; cin>>T;
    for(int t=1;t<=T;t++){
        int N; cin>>N;
        int A[1024], V[1024]={0};
        for(int i=1;i<=N;i++) cin>>A[i];
        float ans = 0;
        for(int i=1;i<=N;i++) if(A[i]!=i && !V[i]){
            int cycle_len = 0;
            int curr = i;
            do{
                cycle_len++;
                V[curr] = 1;
                curr = A[curr];
            } while(curr!=i);
            ans += cycle_len;
        }
        printf("Case #%d: %.6f\n",t,ans);
    }
}

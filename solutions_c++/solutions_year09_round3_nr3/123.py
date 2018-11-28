#include <iostream>
#include <cstdio>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define inf 100000000


int n,q;
int F[101][101];
int a[101];

int main(){
    
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int n0fTest;
    cin>>n0fTest;    
    For(test,1,n0fTest){
        
        cin>>n>>q;
        For(i,1,q) cin>>a[i];
        
        sort(a+1, a+q+1);
        
        ++q;
        
        a[0]=0;
        a[q]=n+1;
        
        memset(F, 0, sizeof(F));
            
        For(k,1,q) For(u,0,q-k){
            int v=u+k;
            
            if (k==1) {
                F[u][v]=a[v]-a[u]-1;
                continue;
            }
            
            F[u][v]=inf;
            For(i, u+1, v-1) F[u][v]=min(F[u][v], F[u][i]+F[i][v]);
            F[u][v]+=a[v]-a[u]-1;
        }
        
        int res=F[0][q]-n;
        cout<<"Case #"<<test<<": "<<res<<endl;
    }
    return 0;
}

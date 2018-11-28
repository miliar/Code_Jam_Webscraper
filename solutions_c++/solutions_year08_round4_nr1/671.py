#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
using namespace std;
#define For(i,a,b)  for(int i=a; i<=b; i++)
#define Ford(i,a,b) for(int i=a; i>=b; i--)
#define fillchar(a) memset(a, 0, sizeof(a))
#define inf 1000000

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out","w", stdout);
    int ntest;
    cin>>ntest;
    int a[10010], b[10010], F[10010][2];
    For(test,1,ntest){
        int m,v;
        cin>>m>>v;
        For(i,1,(m-1)/2){
            cin>>a[i]>>b[i];
        }
        int cc;
        For(i,(m+1)/2,m){
            cin>>cc;
            F[i][cc]=0;
            F[i][1-cc]=inf;
        }
        Ford(i,(m-1)/2,1){
            int u=i*2, v=u+1;
            F[i][0]=F[i][1]=inf;
            //asfsdf
                if (a[i]==0){
                    F[i][0]=min(F[i][0],F[u][0]+F[v][0]);
                    F[i][1]=min(F[i][1],F[u][1]+F[v][0]);
                    F[i][1]=min(F[i][1],F[u][0]+F[v][1]);                    
                    F[i][1]=min(F[i][1],F[u][1]+F[v][1]);                    
                }
                if (a[i]==1){
                    F[i][1]=min(F[i][1],F[u][1]+F[v][1]);
                    F[i][0]=min(F[i][0],F[u][1]+F[v][0]);
                    F[i][0]=min(F[i][0],F[u][0]+F[v][1]);                    
                    F[i][0]=min(F[i][0],F[u][0]+F[v][0]);                    
                }                
            // if changable
            if (b[i]==1){
                if (a[i]==0){
                    F[i][0]=min(F[i][0],F[u][1]+F[v][0]+1);
                    F[i][0]=min(F[i][0],F[u][0]+F[v][1]+1);                    
                }
                if (a[i]==1){
                    F[i][1]=min(F[i][1],F[u][1]+F[v][0]+1);
                    F[i][1]=min(F[i][1],F[u][0]+F[v][1]+1);                    
                }                                
            }
        }
        cout<<"Case #"<<test<<": ";
        if (F[1][v]>=inf) cout<<"IMPOSSIBLE"<<endl; else cout<<F[1][v]<<endl;
    }    
    return 0;
}

#include <iostream>
#include <cstdio>
using namespace std;
int N,S,p;
int scores[101];
bool more[101];
bool same[101];
int surprise[101];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blarge.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        scanf("%d%d%d",&N,&S,&p);
        for(int i=0;i<N;i++)scanf("%d",scores+i);
        int ans = 0,c=0;
        for ( int i=0;i<N;i++){
            int v = scores[i]/3;
            int m = scores[i]%3;
            if ( v>=p){
                ans++;
                continue;   
            }
            if ( v== p-1){
                if ( m==0 && c<S && v>0){
                    ans++;
                    c++;   
                }
                if ( m==1 || m==2){
                    ans++;   
                }
            }
            else if ( v==p-2){
                if ( m==2 && c<S){
                    ans++;
                    c++;   
                }  
            }
               
        }
        printf("Case #%d: %d\n",I,ans);
    }
return 0;
        
}

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
#define sz(a) (a).size()
#define all(c) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
using namespace std;
int main(){
        freopen("A-large.in","r",stdin);
        freopen("ALAR.txt","w",stdout);
        int T,N;
        scanf("%d",&T);
        for(int Kases=1;Kases<=T;Kases++){
            printf("Case #%d:\n",Kases);
            scanf("%d",&N);
            char inp[N][N+1];
            double OWP[N],OOWP[N],w[N];
            double WP[N][N];
            for(int i=0;i<N;i++){
                scanf("%s",inp[i]);
                for(int j=0;j<N;j++)
                    WP[i][j]=-1.0;
                //OW[i]=0.0;
                //OOW[i]=0.0;
               }
            for(int i=0;i<N;i++){
                int a=0,b=0;
                    for(int j=0;j<N;j++){
                        if(inp[i][j]!='.'){
                            if(inp[i][j]=='1')
                                a++;
                            //p+=inp[i][j]-48;
                            b++;
                        }
                    }
                //w[i]=(double)p/(double)q;
                w[i]=a*1.0/b;
                for(int j=0;j<N;j++)
                if(inp[i][j]!='.')
                WP[i][j]=((a-inp[i][j]+48)*1.0)/(b-1);
            }

            for(int i=0;i<N;i++){
                OWP[i]=0.0;
                int q=0;
                for(int j=0;j<N;j++){
                    if(j==i)
                        continue;
                    if(WP[i][j]>=0){
                        OWP[i]+=WP[j][i];
                        q++;
                    }
                }
                OWP[i]/=q*1.0;
            }
            double x=0.0;
            for(int i=0;i<N;i++){
                OOWP[i]=0.0;
                int q=0;
                for(int j=0;j<N;j++){
                    if(i!=j && inp[i][j]!='.'){
                        OOWP[i]+=OWP[j];
                        q++;
                    }
                }
                OOWP[i]/=q;
            }


            for(int i=0;i<N;i++){
                double val=0.25*w[i]+0.5*OWP[i]+0.25*OOWP[i];
                printf("%.8lf\n",val);
            }
       }
}

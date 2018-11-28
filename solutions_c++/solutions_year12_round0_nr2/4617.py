#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    cin>>test;
    int N,S,p;
    for(int t=1;t<=test;++t) {
        scanf("%d %d %d",&N,&S,&p);
        int ar[N];
        for(int i=0;i<N;++i) scanf("%d",&ar[i]);
        
        int ct=0;
        for(int i=0;i<N;++i) {
            int div= ar[i]/3;
            int mod= ar[i]%3;
            if(mod==0) {
                if(div>=p) ++ct;
                else if( div!=0 && (div+1) >= p && S>0) {
                    ++ct;
                    --S;
                }
            }
            else if(mod==1) {
                if( (div+1) >= p) ++ct;
            }
            else {
                if( (div+1) >= p) ++ct;
                else if( (div+2) >= p && S>0) {
                    ++ct;
                    --S;
                }    
            }
        }
        printf("Case #%d: %d\n",t,ct);
    }
    return 0;
}                         

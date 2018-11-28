#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int v[105], f[105];
bool overbound(int n) { return n < 0 || n > 10; }
int test(int k, int p, int fa)
{
        int d;
        if(fa){
                if(k>1 && (k-2)%3==0){
                        d=(k-2)/3;
                        if(!overbound(d) && !overbound(d+2) && d+2>=p) return 1;
                }
                if(k>2 && (k-3)%3==0){
                        d=(k-3)/3;
                        if(!overbound(d) && !overbound(d+2) && d+2>=p) return 1;
                }
                if(k>3 && (k-4)%3==0){
                        d=(k-4)/3;
                        if(!overbound(d) && !overbound(d+2) && d+2>=p) return 1;
                }
                return 0;

        } else {
                if(k%3==0){
                        d=k/3;
                        if(!overbound(d) && d>=p) return 1;
                }
                if(k && (k-1)%3==0){
                        d=(k-1)/3;
                        if(!overbound(d) && !overbound(d+1) && d+1>=p) return 1;
                }
                if(k && (k-2)%3==0){
                        d=(k-2)/3;
                        if(!overbound(d) && !overbound(d+1) && d+1>=p) return 1;
                }
                return 0;
        }
}
void Solve(int n, int s, int p)
{
        int i, j, g, q;
        memset(f,0xff,sizeof f);
        f[0]=0;
        for(i=0;i<n;i++){
                for(j=s;j>=0;--j){
                        g=q=-1;
                        if(j && f[j-1]!=-1) g=f[j-1]+test(v[i],p,1);
                        if(f[j]!=-1) q=f[j]+test(v[i],p,0);
                        if(g<q) g=q;
                        f[j]=g;
                }
        }
        printf("%d\n",f[s]);
}
int main()
{
        int i,t,n,s,p,cas=0;
        freopen("B-large.in","r",stdin);
        freopen("B.out","w",stdout);
        scanf("%d",&t);
        while(t--){
                scanf("%d%d%d",&n,&s,&p);
                for(i=0;i<n;i++) scanf("%d",&v[i]);
                printf("Case #%d: ",++cas);
                Solve(n,s,p);

        }
        return 0;
}

#include<cstdio>
#include<cstring>

using namespace std;

char a[6000][20];
int l,m,n,i,j,k,t,ans;
bool f[6000];
char s[10000];
bool g[300];

int main(){
    scanf("%d%d%d",&l,&m,&n);
    for(i=0;i<m;++i) scanf("%s",a[i]);
    for(t=1;t<=n;++t){
        scanf("%s",s);
        for(i=0;i<m;++i) f[i]=true;
        k=0;
        for(i=0;i<l;++i){        
            memset(g,0,sizeof(g));
            if(s[k]=='(')
                while(s[++k]!=')') g[s[k]]=true;
            else  g[s[k]]=true;
            ++k;
            for(j=0;j<m;++j)
                if(!g[a[j][i]]) f[j]=false;
        }
        ans=0;
        for(i=0;i<m;++i) ans+=f[i];
        printf("Case #%d: %d\n",t,ans);
    }
}

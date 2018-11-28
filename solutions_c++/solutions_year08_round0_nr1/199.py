#include<stdio.h>
#include<string.h>

const int maxs=128;
const int maxq=1024;
const int maxl=128;
int ans[maxs],t[maxs];
char s[maxs][maxl];
char q[maxl];
int n,m;

int solve()
{
    int i,j,k;
    scanf("%d",&n);
    gets(s[0]);
    for(i=0;i<n;i++){
        gets(s[i]);
    }
    memset(ans,0,sizeof(ans));
    scanf("%d",&m);
    gets(q);
    for(i=0;i<m;i++){
        gets(q);
        memset(t,-1,sizeof(t));
        for(j=0;j<n;j++){
            if(strcmp(q,s[j])!=0){
                for(k=0;k<n;k++){
                    if(ans[k]>=0){
                        if(k==j){
                            if(t[j]<0 || t[j]>ans[k]) t[j]=ans[k];
                        }else{
                            if(t[j]<0 || t[j]>ans[k]+1) t[j]=ans[k]+1;
                        }
                    }
                }
            }
        }
        memcpy(ans,t,sizeof(ans));
    }
    for(j=-1,i=0;i<n;i++){
        if(ans[i]>=0 && (j<0 || ans[j]>ans[i])) j=i;
    }
    return ans[j];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,cas;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++){
        //input();
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
} 

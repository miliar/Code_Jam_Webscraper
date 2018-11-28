#include<cstdio>
#include<cstring>

int n;
int in[1000];
int abs(int a){return a>0?a:-a;}
void solve(){
    int i,j,ans=0,sum=0,k=10000000;
    for(i=0;i<n;++i){
        ans^=in[i];
        sum+=in[i];
        if(k>in[i])k=in[i];
    }
    if(ans){
        printf("NO\n");
        return;
    }
    printf("%d\n",sum-k);
}
int main(){
  //  freopen("C-small-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int num=1;
    while(t--){
        scanf("%d",&n);
        int i;
     //   char ch[10];
        for(i=0;i<n;++i){
            scanf("%d",in+i);
        //    scanf("%s%d",ch,&pos[i]);
     //       order[i]=ch[0]=='O';
        }
   //     solve();
        printf("Case #%d: ",num++);
        solve();
    }
    return 0;
}

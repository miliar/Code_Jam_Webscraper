#include<cstdio>
#include<cstring>

int order[100];
int pos[100];
int n;
int abs(int a){return a>0?a:-a;}
void solve(){
    int i,j,ans=0;
    int t1=0,t2=0;// t1 == 'O' t2 == 'B'
    int l1=1,l2=1;
    for(i=0;i<n;++i){
        if(order[i]){
            int need=abs(pos[i]-l1);
            if(t1>need){
                t1=0;
                ans++;
                l1=pos[i];
                t2++;
            }
            else {
                ans+=need-t1+1;
                t2+=need-t1+1;
                t1=0;
                l1=pos[i];
            }
        }
        else {
            int need=abs(pos[i]-l2);
            if(t2>need){
                t2=0;
                ans++;
                l2=pos[i];
                t1++;
            }
            else {
                ans+=need-t2+1;
                t1+=need-t2+1;
                t2=0;
                l2=pos[i];
            }
        }
    }
    printf("%d\n",ans);
}
int main(){
  //  freopen("A-small-attempt1.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int num=1;
    while(t--){
        scanf("%d",&n);
        int i;
        char ch[10];
        for(i=0;i<n;++i){
            scanf("%s%d",ch,&pos[i]);
            order[i]=ch[0]=='O';
        }
   //     solve();
        printf("Case #%d: ",num++);
        solve();
    }
    return 0;
}

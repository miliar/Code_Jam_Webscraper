#include<cstdio>
#include<cstring>

int n;
int np;
int nm;
char rep[500][40];
char mis[500][30];
char in[10000];
int abs(int a){return a>0?a:-a;}
char ans[100000];
int len;
char findrep(char a,char b){
    int i;
    for(i=0;i<np;++i){
        if(rep[i][0]==a&&rep[i][1]==b)return rep[i][2];
        if(rep[i][0]==b&&rep[i][1]==a)return rep[i][2];
    }
    return 0;
}
int find(char a,char b){
    int i;
    for(i=0;i<nm;++i){
        if(mis[i][0]==a&&mis[i][1]==b)return 1;
        if(mis[i][0]==b&&mis[i][1]==a)return 1;
    }
    return 0;
}
void solve(){
    int i,j;
    len=0;
    for(i=0;i<n;++i){
        if(len>=1){
            char res=findrep(in[i],ans[len-1]);
            if(res)ans[len-1]=res;
            else{
                int flag=1;
                for(j=0;j<len&&flag;++j){
                    if(find(in[i],ans[j])){
                        len=0;
                        flag=0;
                    }
                }
                if(flag)ans[len++]=in[i];
            }
        }
        else ans[len++]=in[i];
    }
    printf("[");
    for(i=0;i<len;++i){
        printf("%c",ans[i]);
        if(i<len-1)printf(", ");
    }
    printf("]\n");
}
int main(){
  //  freopen("B-small-attempt5.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int num=1;
    while(t--){
        scanf("%d",&np);
        int i;
        for(i=0;i<np;++i){
            scanf("%s",rep[i]);
        }
        scanf("%d",&nm);
        for(i=0;i<nm;++i){
            scanf("%s",mis[i]);
        }
        scanf("%d",&n);
        scanf("%s",in);
        printf("Case #%d: ",num++);
        solve();
    }
    return 0;
}

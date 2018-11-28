#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using namespace std;
struct combi{
    int first,second,result;
    combi(){
        first=0;
        second=0;
        result=0;
    }
    combi(int f,int s,int r){
        first=f;
        second=s;
        result=r;
    }
    bool match(int a,int b){
        return (a==first)&&(b==second);
    }
};
void solve(int test){
    int C;
    scanf("%d",&C);
    char tmp[10];
    combi combine[40];

    for(int i=0;i<C;i++){
        scanf("%s",tmp);
        combine[i]=combi(min(tmp[0],tmp[1]),max(tmp[0],tmp[1]),tmp[2]);
    }
    int D;
    pair<int,int> opp[30];
    scanf("%d",&D);
    for(int i=0;i<D;i++){
        scanf("%s",tmp);
        opp[i].first=min(tmp[0],tmp[1]);
        opp[i].second=max(tmp[1],tmp[0]);
    }
    int n;
    scanf("%d",&n);
    char str[n+5];
    char ans[n+5];
    int tail=0;
    scanf("%s",str);
    for(int i=0;i<n;i++){
        ans[tail++]=str[i];
        // check combine
        if(tail>=2){
            int last[2]={min(ans[tail-1],ans[tail-2]),max(ans[tail-1],ans[tail-2])};
            bool alCom=0;
            for(int j=0;j<C;j++)if(combine[j].match(last[0],last[1])){
                tail-=2;
                ans[tail++]=combine[j].result;
                alCom=1;
                break;
            }
            if(alCom==0){
                bool opps=0;
                for(int j=0;j<tail-1&&opps==0;j++){
                    for(int k=0;k<D&&opps==0;k++){
                        if(min(ans[j],ans[tail-1])==opp[k].first&&opp[k].second==max(ans[j],ans[tail-1])){
                            opps=1;
                            break;
                        }
                    }
                }
                if(opps==1)tail=0;
            }
        }
    }
    ans[tail]='\0';
    printf("Case #%d: [",test);
    if(tail>0)printf("%c",ans[0]);
    for(int i=1;i<tail;i++)printf(", %c",ans[i]);
    printf("]\n");
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int C;
    scanf("%d",&C);
    for(int i=1;i<=C;i++){
        solve(i);
    }
}

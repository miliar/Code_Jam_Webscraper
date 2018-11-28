#include <stdio.h>
int ins[105];
int where[3][105];
int myabs(int a){return a<0?-a:a;}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cs;
    char ch;
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        int n,i,cc=0,c2=0,v,cur1=1,cur2=1,j,k;
        scanf("%d",&n);
        for(i=1;i<=n;++i){
            scanf(" %c %d",&ch,&v);
            if(ch=='O'){
                ins[i]=1;
                where[1][cc++]=v;
            }
            else{
                ins[i]=2;
                where[2][c2++]=v;
            }
        }
        int res=0;
        j=k=0;
        for(i=1;i<=n;++i){
            if(ins[i]==1){
                res+=myabs(where[1][j]-cur1)+1;
                if(k<c2&&cur2<where[2][k]){
                    cur2+=myabs(where[1][j]-cur1)+1;
                    if(cur2>where[2][k]) cur2=where[2][k];
                }
                else if(k<c2&&cur2>where[2][k]){
                    cur2-=myabs(where[1][j]-cur1)+1;
                    if(cur2<where[2][k]) cur2=where[2][k];
                }
				cur1=where[1][j++];
            }
            else{
                res+=myabs(where[2][k]-cur2)+1;
                if(j<cc&&cur1<where[1][j]){
                    cur1+=myabs(where[2][k]-cur2)+1;
                    if(cur1>where[1][j]) cur1=where[1][j];
                }
                if(j<cc&&cur1>where[1][j]){
                    cur1-=myabs(where[2][k]-cur2)+1;
                    if(cur1<where[1][j]) cur1=where[1][j];
                }
                cur2=where[2][k++];
            }
        }
        printf("Case #%d: %d\n",cs,res);
    }
    return 0;
}

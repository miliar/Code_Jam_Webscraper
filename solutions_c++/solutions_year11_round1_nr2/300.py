#define MAX 10005
#include <stdio.h>
#include <string.h>
bool mark[MAX];
char word[MAX][15];
char seq[100];
int len[MAX];
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,cs,n,m,i,j,k,kk;
    char ch;
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;++i){
            scanf(" %s",word[i]);
            len[i]=strlen(word[i]);
        }
        printf("Case #%d:",cs);
        for(i=1;i<=m;++i){
            scanf(" %s",seq);
            int maxi=-1,ind=-1;
            for(j=1;j<=n;++j){
				memset(mark,false,sizeof mark);
                int cnt=0,cc=0,s=0;
                for(k=1;k<=n;++k) if(len[k]!=len[j]) mark[k]=true;
                while(cc<len[j]){
                    ch=seq[s++];
                    for(k=1;k<=n;++k){
                        if(mark[k]) continue;
                        for(kk=0;kk<len[k];++kk) if(word[k][kk]==ch) break;
                        if(kk!=len[k]) break;
                    }
                    if(k!=n+1){
						bool stat=false;
                        for(kk=0;kk<len[j];++kk){
                            if(word[j][kk]==ch){
								stat=true;
                                ++cc;
                                for(k=1;k<=n;++k){
                                    if(kk>=len[k]) mark[k]=true;
                                    else if(word[k][kk]!=ch) mark[k]=true;
                                }
                            }
                            else{
                                for(k=1;k<=n;++k){
                                    if(kk>=len[k]) continue;
                                    if(word[k][kk]==ch) mark[k]=true;
                                }
                            }
                        }
						if(stat==false) ++cnt;
                    }
                }
                if(cnt>maxi) maxi=cnt,ind=j;
            }
            printf(" %s",word[ind]);
        }
        printf("\n");
    }
    return 0;
}

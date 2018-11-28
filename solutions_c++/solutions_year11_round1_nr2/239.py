#include<cstdio>
#include<cstring>

int t,n,m;
bool ok[105],guess[1000];
char dict[105][100];
char l[15][100];
char tmp[100];

int main(){
    scanf("%d",&t);
    for (int ca=1;ca<=t;++ca){
        scanf("%d%d",&n,&m); gets(tmp);
        
        for (int i=0;i<n;++i) scanf("%s",dict[i]);
        for (int i=0;i<m;++i) scanf("%s",l[i]);
        
        printf("Case #%d:",ca);
        for (int i=0;i<m;++i){
            int count=-1;
            char ans[100];
            for (int j=0;j<n;++j){
                int tcount=0;
                int len=strlen(dict[j]);
                memset(ok,1,sizeof(ok));
                memset(guess,0,sizeof(guess));
                for (int k=0;k<n;++k){
                    if (strlen(dict[k])!=len) ok[k]=0;
                }
                
                for (int c=0;c<26;++c){
                    bool go=0;
                    for (int k=0;k<n;++k){
                        if (ok[k]){
                            int tn=strlen(dict[k]);
                            for (int x=0;x<tn;++x){
                                if (dict[k][x]==l[i][c]) go=1;
                            }
                        }
                    }
                    if (go){
                        bool right=0;
                        for (int k=0;k<len;++k){
                            if (dict[j][k]==l[i][c]){
                                right=1; break;
                            }
                        }
                        if (!right) ++tcount;
                        
                        guess[l[i][c]]=1;
                        for (int k=0;k<n;++k){
                            if (ok[k]){
                                int tn=strlen(dict[k]);
                                for (int p=0;p<tn;++p){
                                    if (guess[dict[k][p]] && !guess[dict[j][p]]) ok[k]=0;
                                    if (!guess[dict[k][p]] && guess[dict[j][p]]) ok[k]=0;
                                    if (guess[dict[k][p]] && guess[dict[j][p]] && (dict[j][p]!=dict[k][p])) ok[k]=0;
                                }
                            }
                        }
                    }
                }
                if (tcount > count){
                    count = tcount;
                    strcpy(ans, dict[j]);
                }
            }
            printf(" %s",ans);
        }
        puts("");
    }
    return 0;
}

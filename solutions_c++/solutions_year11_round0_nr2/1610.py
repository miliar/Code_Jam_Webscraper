#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
char st[10];
char str[105];
char res[105];
int ct[256][256];
bool ot[256][256];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    int T,C,D,N;
    scanf("%d",&T);
    for(int _case=1;_case<=T;_case++){
        memset(ct,0xff,sizeof(ct));
        memset(ot,false,sizeof(ot));
        scanf("%d",&C);
        for(int i=0;i<C;i++){
            scanf(" %s",st);
            ct[st[0]][st[1]]=st[2];
            ct[st[1]][st[0]]=st[2];
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf(" %s",st);
            ot[st[0]][st[1]]=true;
            ot[st[1]][st[0]]=true;
        }
        scanf(" %d %s",&N,str);
        res[0]=str[0];
        int rt=1;
        for(int i=1;i<N;i++){
            if(rt==0){
                res[rt++]=str[i];
                continue;
            }
            if(ct[res[rt-1]][str[i]]!=-1){
                res[rt-1]=ct[res[rt-1]][str[i]];
            }
            else{
                bool flag=false;
                for(int j=0;j<rt;j++){
                    if(ot[res[j]][str[i]]){
                        rt=0;
                        flag=true;
                        break;
                    }
                }
                if(!flag)res[rt++]=str[i];
            }
        }
        printf("Case #%d: [",_case);
        for(int i=0;i<rt;i++){
            if(i==rt-1)printf("%c",res[i]);
            else printf("%c, ",res[i]);
        }
        printf("]\n");
    }
    return 0;
}

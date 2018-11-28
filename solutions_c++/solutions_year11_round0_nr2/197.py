#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
int n;
char s[200];
char map[30][30];
bool clc[30][30];
int C,D,N;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ca=1;ca<=cas;ca++){
        for(int i=0;i<26;i++){
            for(int j=0;j<26;j++){
                map[i][j]=' ';
                clc[i][j]=false;
            }
        }
        scanf("%d",&C);
        for(int i=0;i<C;i++){
            scanf("%s",&s);
            map[s[0]-'A'][s[1]-'A']=s[2];
            map[s[1]-'A'][s[0]-'A']=s[2];
        }
        scanf("%d",&D);
        for(int i=0;i<D;i++){
            scanf("%s",&s);
            clc[s[0]-'A'][s[1]-'A']=true;
            clc[s[1]-'A'][s[0]-'A']=true;
        }
        scanf("%d",&N);
        scanf("%s",&s);
        //cout<<"N="<<N<<endl;
        char res[200];
        int cnt=0;
        for(int i=0;i<N;i++){
            res[cnt++]=s[i];
            while(cnt>1){
                char tp=map[res[cnt-1]-'A'][res[cnt-2]-'A'];
                if(tp!=' '){
                    res[cnt-2]=tp;
                    cnt--;
                }else break;
            }
            //cout<<"i="<<i<<endl;
            //for(int j=0;j<cnt;j++) cout<<res[j];
            //cout<<endl;
            for(int j=0;j<cnt-1;j++){
                if(clc[res[j]-'A'][res[cnt-1]-'A']){
                    cnt=0;
                    break;
                }
            }
            //for(int j=0;j<cnt;j++) cout<<res[j];
            //cout<<endl;
        }
        printf("Case #%d: [",ca);
        for(int i=0;i<cnt;i++){
            if(i!=0) printf(", ");
            printf("%c",res[i]);
        }
        printf("]\n");
    }
    return 0;
}

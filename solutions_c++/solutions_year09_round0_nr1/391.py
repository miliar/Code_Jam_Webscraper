/*
  NAME : Siwakorn  Srisakaokul
  ID : ping128
  LANG : C++
  CONTEST : CodeJam -- Qualification Round
  TASK : Alien Language
*/
#include<stdio.h>
#include<string.h>

char in[505][30][30];
char word[5005][1000];
int num[505];
int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out","w",stdout);
    char add[1000];
    int N,D,L,l,k;
    int len;
    scanf("%d %d %d",&L,&D,&N);
    for(int i=0;i<D;i++) scanf("%s",word[i]);
    for(int i=0;i<N;i++){
        scanf("%s",add);
        len=strlen(add);
        l=0;
        for(int j=0;j<len;j++){
            if(add[j]=='('){
                for(k=j+1;add[k]!=')';k++){
                    in[i][l][add[k]-'a']++;
                }
                j=k;
            } else {
                in[i][l][add[j]-'a']++;
            }
            l++;
        }
    }
    for(int i=0;i<D;i++){
        for(int j=0;j<N;j++){
            int s=1;
            for(k=0;k<L;k++) s*=in[j][k][word[i][k]-'a'];
            num[j]+=s;
        }
    }
    for(int i=0;i<N;i++){
        printf("Case #%d: %d\n",i+1,num[i]);
    } //while(1);
return 0;
}

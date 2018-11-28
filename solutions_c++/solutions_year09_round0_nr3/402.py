/*
  NAME : Siwakorn  Srisakaokul
  ID : ping128
  LANG : C++
  CONTEST : CodeJam -- Qualification Round
  TASK : Welcome to Code Jam
*/
#include<stdio.h>
#include<string.h>
int main(){
    freopen("C-large.in.txt","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,len1,len2;
    char cmp[]={"welcome to code jam"};
    char in[505];
    int DP[30][505];
    scanf("%d",&T);
    scanf("\n");
    len1=strlen(cmp);
    for(int t=0;t<T;t++){
        gets(in);
        len2=strlen(in);
        for(int i=0;i<=len1;i++)
            for(int j=0;j<=len2;j++) DP[i][j]=0;
        for(int i=0;i<=len2;i++) DP[0][i]=1;
        for(int i=1;i<=len1;i++){
            for(int j=1;j<=len2;j++){
                if(in[j-1]!=cmp[i-1]) DP[i][j]=DP[i][j-1];
                else DP[i][j]=(DP[i][j-1]+DP[i-1][j-1])%10000;
            }
        }
        printf("Case #%d: %04d\n",t+1,DP[len1][len2]);
    }
fclose(stdout);
return 0;
}

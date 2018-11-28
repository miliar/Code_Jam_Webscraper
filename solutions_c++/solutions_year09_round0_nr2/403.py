/*
  NAME : Siwakorn  Srisakaokul
  ID : ping128
  LANG : C++
  CONTEST : CodeJam -- Qualification Round
  TASK : Watersheds
*/
#include<stdio.h>
#define INF 30000
int T,R,C;
char DP[105][105];
int MAP[105][105];
int cx[]={-1,0,0,1},cy[]={0,-1,1,0};
char letter;
char search(int ii,int jj){
    if(DP[ii][jj]!='0') return DP[ii][jj];
    else {
        int min=INF,s=-1;
        for(int k=0;k<4;k++){
            if(ii+cx[k]>=1 && ii+cx[k]<=R && jj+cy[k]<=C && jj+cy[k]>=1){
                if(MAP[ii+cx[k]][jj+cy[k]]<MAP[ii][jj]){
                    if(MAP[ii+cx[k]][jj+cy[k]]<min){
                        min=MAP[ii+cx[k]][jj+cy[k]];
                        s=k;
                    }     
                }
            }
        }
        if(s==-1){
            DP[ii][jj]=letter;
            letter++;
            return DP[ii][jj];
        } else {
            DP[ii][jj]=search(ii+cx[s],jj+cy[s]);
            return DP[ii][jj];
        }
    }
}
int main(){
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        letter='a';
        printf("Case #%d:\n",t+1);
        scanf("%d %d",&R,&C);
        for(int j=0;j<=R+1;j++)
            for(int k=0;k<=C+1;k++) DP[j][k]='0';
        for(int j=0;j<=R;j++) MAP[j][C+1]=MAP[j][0]=INF;
        for(int j=0;j<=C+1;j++) MAP[R+1][j]=MAP[0][j]=INF;
        for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++)
                scanf("%d",&MAP[i][j]);
        for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++){
                if(DP[i][j]=='0'){
                    DP[i][j]=search(i,j);
                }
            }
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++) printf("%c ",DP[i][j]);
            printf("\n");
        }
    }
    fclose(stdin);
    fclose(stdout);
return 0;
}
            
    

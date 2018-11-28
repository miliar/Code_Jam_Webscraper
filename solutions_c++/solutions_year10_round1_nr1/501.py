#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#define SIZE 55
using namespace std;
char s0[SIZE][SIZE],s1[SIZE][SIZE],s2[SIZE][SIZE];
int R,B,N,K,t;
int dx[4]={1,1,0,0};
int dy[4]={1,0,1,-1};
void G(char s[][SIZE]){
    int i,j,k;
    for(i=0;i<N;i++){
        for(j=k=N-1;j>=0;j--){
            if(s[j][i]!='.')
                s[k--][i]=s[j][i];
        }
        for(;k>=0;k--)s[k][i]='.';
    }
}
void rotate(){
    int i,j;
    for(i=0;i<N;i++)
        for(j=0;j<N;j++){
            s1[i][j]=s0[N-1-j][i];
            s2[i][j]=s0[j][N-1-i];
        }
    G(s1);
    G(s2);
}
void Go(char s[][SIZE]){
    int i,j,k,l;
    for(i=0;i<N;i++)
        for(j=0;j<N;j++){
            if(s[i][j]!='.'){
                for(l=0;l<4;l++){
                    for(k=1;k<K;k++){
                        if(i+k*dx[l]<0||i+k*dx[l]>=N||j+k*dy[l]<0||j+k*dy[l]>=N)break;
                        if(s[i+k*dx[l]][j+k*dy[l]]!=s[i+(k-1)*dx[l]][j+(k-1)*dy[l]])break;
                    }
                    if(k==K)break;
                }
                if(l<4){
                    if(s[i][j]=='B')B=t;
                    else R=t;
                }
            }
        }
}
main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int i,T;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d %d",&N,&K);
        for(i=0;i<N;i++)scanf("%s",s0[i]);
        rotate();
        Go(s0);
        Go(s1);
        printf("Case #%d: ",t);
        if(R==t&&B==t)puts("Both");
        else if(R==t)puts("Red");
        else if(B==t)puts("Blue");
        else puts("Neither");
    }
}

#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<set>

using namespace std;

typedef long long lld;

int N,K;

char in[55][55];
char board[55][55];
int main(){
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small6.out","w",stdout);
    int C;
    char pp;
    scanf("%d",&C);
    for(int c=1;c<=C;c++){
        scanf("%d %d",&N,&K);
        for(int i=0;i<N;i++) scanf("%s",in[i]);
        for(int i=0;i<55;i++)
            for(int j=0;j<55;j++)
                board[i][j]='.';
        for(int i=N-1;i>=0;i--){
            for(int j=0;j<N;j++){
                board[j][N-i-1]=in[i][j];
            }
        }
        
      
        for(int i=N-1;i>=0;i--){
            for(int j=0;j<N;j++){
                if(board[i][j]!='.'){
                    int k;
                    for(k=i+1;k<N;k++){
                        if(board[k][j]!='.'){
                            k--;
                            break;
                        }
                    }
                    if(k==N) k=N-1;
                    
                    pp=board[i][j];
                    board[i][j]='.';
                    board[k][j]=pp;
                        
                }
            }
        } 
       
        
        int a=0,b=0;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++){
                if(board[i][j]=='R'){
                    int ch=1;
                    for(int k=0;k<K;k++){
                        if(j+k>=N){ ch=0; break; }
                        if(board[i][j+k]!='R'){ ch=0; break; }      
                    } 
                    if(ch) a=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(i+k>=N){ ch=0; break; }
                        if(board[i+k][j]!='R'){ ch=0; break; }      
                    } 
                    if(ch) a=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(j+k>=N || i+k>=N){ ch=0; break; }
                        if(board[i+k][j+k]!='R'){ ch=0; break; }      
                    } 
                    if(ch) a=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(j-k<0 || i-k<0){ ch=0; break; }
                        if(board[i-k][j-k]!='R'){ ch=0; break; }      
                    } 
                    if(ch) a=1;
                    
                    
                } else if(board[i][j]=='B'){
                    int ch=1;
                    for(int k=0;k<K;k++){
                        if(j+k>=N){ ch=0; break; }
                        if(board[i][j+k]!='B'){ ch=0; break; }      
                    } 
                    if(ch) b=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(i+k>=N){ ch=0; break; }
                        if(board[i+k][j]!='B'){ ch=0; break; }      
                    } 
                    if(ch) b=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(j+k>=N || i+k>=N){ ch=0; break; }
                        if(board[i+k][j+k]!='B'){ ch=0; break; }      
                    } 
                    if(ch) b=1;
                    
                    ch=1;
                    for(int k=0;k<K;k++){
                        if(j-k<0 || i-k<0){ ch=0; break; }
                        if(board[i-k][j-k]!='B'){ ch=0; break; }      
                    } 
                    if(ch) b=1;
                }
            }
        if(a && b) printf("Case #%d: Both\n",c);
        else if(a) printf("Case #%d: Red\n",c);
        else if(b) printf("Case #%d: Blue\n",c);
        else printf("Case #%d: Neither\n",c);
    }
return 0;
}

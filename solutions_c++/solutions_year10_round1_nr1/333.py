#include<stdio.h>
#include<stdlib.h>

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    char board[100][100];
    for(int time=1;time<=t;time++){
        int n,k;
        int rwin=0,bwin=0;
        scanf("%d %d",&n,&k);
        for(int i=0;i<n;i++)scanf("%s",board[i]);
        for(int i=0;i<n;i++){
            for(int j=n-2;j>=0;j--){
                int z=j;
                if(board[i][z]!='.'){
                    while(z+1<n&&board[i][z+1]=='.'){
                        char tmp=board[i][z];
                        board[i][z]='.';
                        board[i][z+1]=tmp;
                        z++;
                    }
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]=='B'){
                    if(j+k<=n){
                        int z=j+1;
                        while(z<j+k&&board[i][z]=='B')z++;
                        if(z>=j+k)bwin=1;
                    }
                    if(i+k<=n){
                        int z=i+1;
                        while(z<i+k&&board[z][j]=='B')z++;
                        if(z>=i+k)bwin=1;
                    }
                    if(i+k<=n&&j+k<=n){
                        int z=i+1,x=j+1;
                        while(z<i+k&&x<i+k&&board[z][x]=='B'){
                            z++;x++;
                        }
                        if(z==i+k&&x==i+k)bwin=1;
                    }
                    if(j-k+1>=0&&i+k<=n){
                        int z=i+1,x=j-1;
                        while(z<i+k&&x>j-k&&board[z][x]=='B'){
                            z++;x--;
                        }
                        if(z==i+k&&x==j-k)bwin=1;
                    }
                }
                if(board[i][j]=='R'){
                    if(j+k<=n){
                        int z=j+1;
                        while(z<j+k&&board[i][z]=='R')z++;
                        if(z>=j+k)rwin=1;
                    }
                    if(i+k<=n){
                        int z=i+1;
                        while(z<i+k&&board[z][j]=='R')z++;
                        if(z>=i+k)rwin=1;
                    }
                    if(i+k<=n&&j+k<=n){
                        int z=i+1,x=j+1;
                        while(z<i+k&&x<i+k&&board[z][x]=='R'){
                            z++;x++;
                        }
                        if(z==i+k&&x==i+k)rwin=1;
                    }
                    if(j-k+1>=0&&i+k<=n){
                        int z=i+1,x=j-1;
                        while(z<i+k&&x>j-k&&board[z][x]=='R'){
                            z++;x--;
                        }
                        if(z==i+k&&x==j-k)rwin=1;
                    }
                }
            }
        }
        printf("Case #%d: ",time);
        if(rwin==0&&bwin==0)printf("Neither\n");
        else if(rwin==1&&bwin==1)printf("Both\n");
        else if(rwin==1&&bwin==0)printf("Red\n");
        else printf("Blue\n");
    }
}

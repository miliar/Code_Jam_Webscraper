#include <iostream>
using namespace std;

int ca,T,n,k;
char maze[100][100];

void Trans(int x,int  y){
    int j=y;
    while(1){
        ++j;
        if(j>n) break;
        if(maze[x][j]=='B'||maze[x][j]=='R')    break;
    }
    maze[x][j-1]=maze[x][y];
    if(j-1!=y)  maze[x][y]='.';
}

bool check(int x,int y,char ch){
    int i,j;
    int cnt;
    cnt=0;
    for(i=x,j=y;j<=n;j++){
        if(maze[i][j]==ch)    cnt++;
        else    break;
    }
    if(cnt>=k)  return true;
    
    cnt=0;
    for(i=x,j=y;i<=n;i++){
        if(maze[i][j]==ch)    cnt++;
        else    break;
    }
    if(cnt>=k)  return true;
    
    cnt=0;
    for(i=x,j=y;i<=n&&j<=n;i++,j++){
        if(maze[i][j]==ch)    cnt++;
        else    break;
    }
    if(cnt>=k)  return true;
    
    cnt=0;
    for(i=x,j=y;i<=n&&j<=n;i++,j--){
        if(maze[i][j]==ch)    cnt++;
        else    break;
    }
    if(cnt>=k)  return true;
    
    return false;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    std::ios::sync_with_stdio(false);
    cin>>T;
    while(T--){
        int i,j;
        cin>>n>>k;
        memset(maze,0,sizeof(maze));
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                cin>>maze[i][j];
            }
        }
        for(i=n;i>=1;i--){
            for(j=n;j>=1;j--){
                if(maze[i][j]=='R'||maze[i][j]=='B'){
                    Trans(i,j);
                }
            }
        }
        bool flag1=false;
        bool flag2=false;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(maze[i][j]=='R'){
                    flag1=flag1||check(i,j,'R');
                }
                else if(maze[i][j]=='B'){
                    flag2=flag2||check(i,j,'B');
                }
            }
        }
        if(flag1==false&&flag2==false){
            cout<<"Case #"<<++ca<<": "<<"Neither"<<endl;
        }
        if(flag1&&flag2){
            cout<<"Case #"<<++ca<<": "<<"Both"<<endl;
        }
        if(flag1&&flag2==false){
            cout<<"Case #"<<++ca<<": "<<"Red"<<endl;
        }
        if(flag1==false&&flag2){
            cout<<"Case #"<<++ca<<": "<<"Blue"<<endl;
        }
    }
    return 0;
}

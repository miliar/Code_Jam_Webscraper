#include<iostream>
#include<queue>
using namespace std;
int T[110][110];
int C[110][110];
static int dRow[4]={-1,0,0,1},dCol[4]={0,-1,1,0};
int H,W;
bool isValid(int row,int col){
    return row>=0&&row<H&&col>=0&&col<W;
}
bool isSink(int row,int col){
    for(int i=0;i<4;++i){
        int row2=row+dRow[i],col2=col+dCol[i];
        if(isValid(row2,col2)){
            if(T[row2][col2]<T[row][col])return 0;
        }
    }
    return 1;
}
int sinksTo(int cell){
    int row=cell/W,col=cell%W;
    int ret=-1,value=1000000;
    for(int i=0;i<4;++i){
        int row2=row+dRow[i];
        int col2=col+dCol[i];
        if(isValid(row2,col2)&&T[row2][col2]<T[row][col]){
            if(T[row2][col2]<value){
                value=T[row2][col2];
                ret=row2*W+col2;
            }
        }
    }
    return ret;
}
void bfs(int row,int col,int color){
    queue<int> Q;
    Q.push(row);
    Q.push(col);
    while(!Q.empty()){
        int cRow=Q.front();Q.pop();
        int cCol=Q.front();Q.pop();
        C[cRow][cCol]=color;
        for(int i=0;i<4;++i){
            int newRow=cRow+dRow[i];
            int newCol=cCol+dCol[i];
            if(isValid(newRow,newCol)&&sinksTo(newRow*W+newCol)==cRow*W+cCol){
                Q.push(newRow);
                Q.push(newCol);
            }
        }
    }
}
void f(int test){
    cout<<"Case #"<<test<<":"<<endl;
    cin>>H>>W;
    for(int i=0;i<H;++i)
        for(int j=0;j<W;++j){
            cin>>T[i][j];
        }
    int color=1;
    for(int i=0;i<H;++i)
        for(int j=0;j<W;++j){
            if(isSink(i,j)){
                bfs(i,j,color++);
            }
        }
    char mapeo[30]={};
    char basin='a';
    for(int i=0;i<H;++i){
        for(int j=0;j<W;++j){
            if(mapeo[C[i][j]]==0){
                mapeo[C[i][j]]=basin++;
            }
            if(j>0)cout<<" ";
            cout<<mapeo[C[i][j]];
        }
        cout<<endl;
    }
}
int main(){
    int T;
    cin>>T;
    int test=1;
    while(T--){
        f(test++);
    }
}

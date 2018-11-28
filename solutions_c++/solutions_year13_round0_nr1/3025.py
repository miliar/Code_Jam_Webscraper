#include<iostream>
using namespace std;
char board[4][4];
int judge(int mi,int mj)
{
    if(board[mi][mj]=='.' || board[mi][mj]=='T')
    {
        return 0;
    }
    int posi=1;
    char tmp=board[mi][mj];
    int dir[4][2]={0,1,1,0,1,1,-1,1};
    int cnt[4]={1,1,1,1};
    for(int i=0;i<4;i++)
    {

        int step=1;
        while(mi-dir[i][0]*step>=0 && mj-dir[i][1]*step>=0){
            if(board[mi-dir[i][0]*step][mj-dir[i][1]*step]==tmp
                ||board[mi-dir[i][0]*step][mj-dir[i][1]*step]=='T')
            {
                cnt[i]++;
                step++;
            }
            else break;
        }
        step=1;
        while(mi+dir[i][0]*step<4 && mj+dir[i][1]*step<4){
            if(board[mi+dir[i][0]*step][mj+dir[i][1]*step]==tmp
                ||board[mi+dir[i][0]*step][mj+dir[i][1]*step]=='T')
            {
                cnt[i]++;
                step++;
            }
            else break;
        }
    }
    for(int i=0;i<4;i++)
    {
        if(cnt[i]==4)
            return 1;

    }
    return 0;
}
int main()
{
    int t=0,cas=1;

    cin>>t;
    while(t--){
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>board[i][j];
            }
        }

    cout<<"Case #"<<cas++<<": ";
    int flag=0,white=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(board[i][j]=='.') white=1;
            if(judge(i,j))
            {
                flag=1;
                cout<<board[i][j]<<" won"<<endl;
                break;
            }
        }
        if(flag==1)break;
    }
    if(flag==0)
    {
        if(white==0)
        {
            cout<<"Draw"<<endl;
        }
        else
        {
            cout<<"Game has not completed"<<endl;
        }
    }
    }
    return 0;
}

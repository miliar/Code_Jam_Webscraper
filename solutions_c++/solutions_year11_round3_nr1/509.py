#include<iostream>
#include<string>
using namespace std;

#define MAXN 55

string mat[MAXN];
int col[MAXN][MAXN];

int main()
{
//    freopen("A.in","r",stdin);
//    freopen("A.out","w",stdout);
    
    int t;
    cin>>t;
    int num=1;
    while(t--){
       int r,c;
       cin>>r>>c;
       int i;
       for(i=0;i<r;i++)
         cin>>mat[i];
       int j;
       memset(col,-1,sizeof(col));
       for(i=0;i<r;i++)
         for(j=0;j<c;j++)
           if(mat[i][j]=='#')
              col[i][j]=0;
       for(i=0;i<r-1;i++)
         for(j=0;j<c-1;j++)
            if(col[i][j]==0&&col[i][j]==0&&col[i+1][j]==0&&col[i+1][j+1]==0){
                col[i][j]=1;
                col[i][j+1]=2;
                col[i+1][j]=3;
                col[i+1][j+1]=4;
            }
       int flag=1;
       for(i=0;i<r&&flag;i++)
         for(j=0;j<c&&flag;j++)
           if(col[i][j]==0){
              flag=0;
           }
       if(flag){
          printf("Case #%d:\n",num++);
          for(i=0;i<r;i++){
             for(j=0;j<c;j++){
                if(col[i][j]==-1) cout<<".";
                if(col[i][j]==1) cout<<"/";
                if(col[i][j]==2) cout<<"\\";
                if(col[i][j]==3) cout<<"\\";
                if(col[i][j]==4) cout<<"/";
             }
             cout<<endl;
          }
       }
       else{
          printf("Case #%d:\n",num++);
          printf("Impossible\n");
       }
    }
}

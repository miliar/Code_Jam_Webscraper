#include <iostream>
using namespace std;
int main(){
    int i ,j,ntc,a[100][100],m,n;
    string ch[6]={"","/","\\","\\","/","."};
     cin >> ntc;
     for(int tc=1;tc<=ntc;tc++){
             cin >> m >> n;
             char s;
             for(i=1;i<=m;i++)
               for(j=1;j<=n;j++){
                  cin >> s;
                  if(s=='.')
                     a[i][j]=5;
                  else
                     a[i][j]=0;
               }
             for(i=0;i<=m+1;i++)
                for(j=0;j<=n+1;j++)
                   if(i==0 || j==0 || i==m+1 || j==n+1)
                      a[i][j]=5;
             int no=0;
             for(i=1;i<=m;i++)
               for(j=1;j<=n;j++)
                   if(a[i][j]==0)
                       if(a[i][j]==0 && a[i+1][j]==0 && a[i][j+1]==0 && a[i+1][j+1]==0)
                           a[i][j]=1,a[i][j+1]=2,a[i+1][j]=3,a[i+1][j+1]=4;
                       else 
                           no=1;
                 printf("Case #%d:\n",tc);             
             if(no){
                 printf("Impossible\n");
             }
             else{
               for(i=1;i<=m;i++){
                  for(j=1;j<=n;j++)
                     cout << ch[a[i][j]];
                     cout << endl;
                     }
             }
     }
}

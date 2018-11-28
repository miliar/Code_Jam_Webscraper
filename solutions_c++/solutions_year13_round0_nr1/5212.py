#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int main()
{
    string arr[6];
    bool X,Y,D,Dot;
    int tc,x,y;
    cin>>tc;
    for(int z=1;z<=tc;++z)
    {
            X=false;
            Y=false;
            Dot=false;
               for(int i=0;i<4;++i)
               {
                       cin>>arr[i];
                       for(int j=0;j<4;++j)
                       {
                       if(arr[i][j]=='.')
                       Dot=true;
                       }
               }
               for(int i=0;i<4;++i)
               {
                       x=0;
                       y=0;
                       for(int j=0;j<4;++j)
                       {
                               if(arr[i][j]=='T')
                               {
                                                 ++x;
                                                 ++y;
                               }
                               else if(arr[i][j]=='X')
                               ++x;
                               else if(arr[i][j]=='O')
                               ++y;
                       }
                       if(x==4)
                       {
                               X=true;
                               break;
                       }
                       else if(y==4)
                       {
                            Y=true;
                            break;
                       }
                       x=0;
                       y=0;
                       for(int j=0;j<4;++j)
                       {
                               if(arr[j][i]=='T')
                               {
                                                 ++x;
                                                 ++y;
                               }
                               else if(arr[j][i]=='X')
                               ++x;
                               else if(arr[j][i]=='O')
                               ++y;
                       }
                        if(x==4)
                       {
                               X=true;
                               break;
                       }
                       else if(y==4)
                       {
                            Y=true;
                            break;
                       }
               }
               if( !Y && !X)
               {
                   x=0;
                   y=0;
                   for(int i=0;i<4;++i)
                   {
                           if(arr[i][i]=='T')
                           {
                                             ++x;
                                             ++y;
                           }
                           else if(arr[i][i]=='X')
                           ++x;
                           else if(arr[i][i]=='O')
                           ++y;
                   }
                     if(x==4)
                       {
                               X=true;
                       }
                       else if(y==4)
                       {
                            Y=true;
                       }
                       else
                       {
                       x=0;
                       y=0;
                       for(int i=3;i>=0;--i)
                       {
                               if(arr[3-i][i]=='T')
                               {
                                                   ++x;
                                                   ++y;
                               }
                               else if(arr[3-i][i]=='X')
                               ++x;
                               else if(arr[3-i][i]=='O')
                               ++y;
                       }
                       if(x==4)
                       {
                               X=true;
                       }
                       else if(y==4)
                       {
                            Y=true;
                       }
                       }
               }
               cout<<"Case #"<<z<<": ";
               if(X)
               cout<<"X won"<<endl;
               else if(Y)
               cout<<"O won"<<endl;
               else if(Dot)
               cout<<"Game has not completed"<<endl;
               else
               cout<<"Draw"<<endl;
               
    }
    return 0;
}

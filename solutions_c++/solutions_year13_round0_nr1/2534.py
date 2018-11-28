#include<iostream>
#include<vector>
#include<string.h>
#include<string>
using namespace std;
string str[4];
int main()
{
    int tc;
    cin>>tc;
    int cc=0;
    while(tc--)
    {
               ++cc;
               for(int i=0 ; i<4 ; ++i)
               cin>>str[i];
               bool isdot=0;
               for(int i=0 ; i<4 ; ++i)
               for(int j=0 ; j<4 ; ++j)
               if(str[i][j]=='.')
               isdot=1;
               int o=0,x=0,o1=0,x1=0;
               bool iso=0,isx=0;
               for(int i=0 ; i<4 ; ++i)
               {
                       x=0,o=0;
                       for(int j=0 ; j<4 ; ++j)
                       {
                               if(str[i][j]=='O' || str[i][j]=='T')
                               ++o;
                               if(str[i][j]=='X' || str[i][j]=='T')
                               ++x;
                       }
                       if(x==4)
                       {
                               isx=1;
                               break;
                       }
                       if(o==4)
                       {
                               iso=1;
                               break;
                       }
               }
               if(!iso && !isx)
               {
                   for(int j=0 ; j<4 ; ++j)
                   {
                           x=0,o=0;
                           for(int i=0 ; i<4 ; ++i)
                           {
                                   if(str[i][j]=='O' || str[i][j]=='T')
                                   ++o;
                                   if(str[i][j]=='X' || str[i][j]=='T')
                                   ++x;
                           }
                           if(x==4)
                           {
                                   isx=1;
                                   break;
                           }
                           if(o==4)
                           {
                                   iso=1;
                                   break;
                           }
                   }
               }
               x=0,o=0;
               if(!iso && !isx)
               for(int i=0 ; i<4 ; ++i)
               {
                       if(str[i][i]=='O' || str[i][i]=='T')
                       ++o;
                       if(str[i][i]=='X' || str[i][i]=='T')
                       ++x;
                       if(str[i][3-i]=='O' || str[i][3-i]=='T')
                       ++o1;
                       if(str[i][3-i]=='X' || str[i][3-i]=='T')
                       ++x1;
               }
               if(x==4)
                           {
                                   isx=1;
                           }
                           if(o==4)
                           {
                                   iso=1;
                           }
                            if(o1==4)
                           {
                                   iso=1;
                           }
                            if(x1==4)
                           {
                                   iso=1;
                           }
               cout<<"Case #"<<cc<<": ";
               if(isx)
               cout<<"X won"<<endl;
               else if(iso)
               cout<<"O won"<<endl;
               else if(!iso && !isx)
               {
                    if(isdot)
                    cout<<"Game has not completed"<<endl;
                    else
                    cout<<"Draw"<<endl;
               }
    }    
}

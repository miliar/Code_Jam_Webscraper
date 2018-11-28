#include<iostream>
using namespace std;

void print(int ans)
{
     switch(ans)
     {
                case 1:cout<<"O won";
                        break;
                case 2:cout<<"X won";
                        break;
                case 3:cout<<"Draw";
                break;
                case 4: cout<<"Game has not completed";
     }
     cout<<"\n";
}
int main()
{
    int t,i,j,m;
    char cc[10][10];
    
    cin>>t;
    m=t;
    while(t--)
    {
              cout<<"Case #"<<m-t<<": ";
              for(i=0;i<4;i++)
             
              cin>>cc[i];
              
              int a,b,c,ans;
              a=b=c=ans=0;
              
              for(i=0;i<4;i++)
              {
                              a=b=c=0;
                              
                              for(j=0;j<4;j++)
                              {
                                              if(cc[i][j]=='O')
                                              a++;
                                              if(cc[i][j]=='X')
                                              b++;
                                              if(cc[i][j]=='T')
                                              c++;
                              }
                              
                              if(a+c==4)
                              ans=1;
                              if(b+c==4)
                              ans=2;
              }
              if(ans)
              {
                     print(ans);
                     continue;
              }
              
              for(j=0;j<4;j++)
              {
                              a=b=c=0;
                              
                              for(i=0;i<4;i++)
                              {
                                              if(cc[i][j]=='O')
                                              a++;
                                              if(cc[i][j]=='X')
                                              b++;
                                              if(cc[i][j]=='T')
                                              c++;
                              }
                              
                              if(a+c==4)
                              ans=1;
                              if(b+c==4)
                              ans=2;
              }
              
              if(ans)
              {
                     print(ans);
                     continue;
              }
              
              a=b=c=0;
              for(i=0;i<4;i++)
                              {
                                              if(cc[i][i]=='O')
                                              a++;
                                              if(cc[i][i]=='X')
                                              b++;
                                              if(cc[i][i]=='T')
                                              c++;
                              }
                              
                              if(a+c==4)
                              ans=1;
                              if(b+c==4)
                              ans=2;
                              
                              if(ans)
                              {
                     print(ans);
                     continue;
                              }
                              
                              a=b=c=0;
              for(i=0;i<4;i++)
                              {
                                              if(cc[3-i][i]=='O')
                                              a++;
                                              if(cc[3-i][i]=='X')
                                              b++;
                                              if(cc[3-i][i]=='T')
                                              c++;
                              }
                              
                              if(a+c==4)
                              ans=1;
                              if(b+c==4)
                              ans=2;
                              
                              if(ans)
                              {
                     print(ans);
                     continue;
                              }
              int count=0;
              
              for(i=0;i<4;i++)
              for(j=0;j<4;j++)
              if(cc[i][j]=='O'||cc[i][j]=='X'||cc[i][j]=='T')
              count++;
              
              if(count==16)ans=3;
              else ans=4;       
              
              print(ans);         
              }
              return 0;
    }

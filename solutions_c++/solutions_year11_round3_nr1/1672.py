#include<iostream>
#include<conio.h>
#include<cmath>
using namespace std;

# define fir(i,a,b) for(int i=a;i<b;i++)
class games
{
      private:
      int T, R,C, i,j,k, flag, cnt;
      char str[51], tile[51][51];
            
              
      public:
      void control();
      void output();
      
};



void games::control()
{
     cin>>T;
     
     for(i=1;i<=T;++i)
     {  
                    flag=1; 
                    cnt = 0;           
                    cin>>R>>C;
                    
                    for(int j=0;j<R;++j)
                    {
                           cin>>str;
                           
                           for(int k=0;k<C;++k)
                           {
                                     tile[j][k] = str[k];
                                     if(tile[j][k] == '#')
                                     cnt++;
                           }
                    }
                    
                    if(cnt!=0)
                    {
                        for(int j=0;j<R;++j)
                        {
                                  for(int k=0;k<C;++k)
                                  {
                                            if(tile[j][k] == '#')
                                            {
                                             if(j == R-1 || k==C-1 ||tile[j][k+1] !='#' || tile[j+1][k] !='#' || tile[j+1][k+1] !='#')
                                             {
                                                             flag = -1;
                                                             break;
                                             }
                                             
                                             tile[j][k] = '/';
                                             tile[j][k+1] = '\\';
                                             tile[j+1][k] = '\\';
                                             tile[j+1][k+1] = '/';
                                            }      
                                  }
                                  
                                  if(flag==-1)
                                  break;
                        }
                    }
                    
                    
                    output();
     }
}


void games::output()
{
     cout<<"Case #"<<i<<":"<<'\n';
     if(flag==1)
     {
                    fir(j,0,R)
                    {
                           fir(k,0,C)
                           {
                                     cout<<tile[j][k];
                           }
                           
                           cout<<'\n';
                    }
     }
     else
     {
         cout<<"Impossible\n";
     }
     
     
}



int main()
{
    games obj;
    obj.control();
    getch();
    return 0;
}

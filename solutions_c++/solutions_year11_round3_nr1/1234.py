#include<iostream>
using namespace std;
int t,r,c;
char m[55][55];
//bool f;
//char ti[4]={'/','\','\','/'};
bool f()
{    int cnt=0;
     for(int i=1;i<=r;i++)
        for(int j=0;j<c;j++)
        {  if(m[i][j]=='#')
             if(((j+1)<c)&&((i+1)<=r)&&(m[i][j+1]=='#')&&(m[i+1][j]=='#')&&(m[i+1][j+1]=='#'))
             {
                  m[i][j]='/';
                  m[i][j+1]='\\';
                  m[i+1][j]='\\';
                  m[i+1][j+1]='/';                                                                              
             }
             else return false;
          
        }
     return true;
}
int main()
{
    
    freopen("inp.txt","r",stdin);
    freopen("outp.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
          cin>>r>>c;
          getchar();
          for(int j=1;j<=r;j++)
          cin>>m[j]; 
            
    if(f())
    {cout<<"Case #"<<i<<":\n";
     for(int i=1;i<=r;i++)
     {  for(int j=0;j<c;j++)
        cout<<m[i][j];
      cout<<endl;
     }
           
           
    }
    
    
    else cout<<"Case #"<<i<<":\nImpossible"<<endl;        
    }
    
   // system("PAUSE");
    return 0;}

#include <iostream>
using namespace std;
int dig[10];
int digA[10];
int main()
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int T;cin>>T;
  for(int i=1;i<=T;i++)
   {memset(dig,0,sizeof(dig));
          int x; cin>>x;
          int _x=x;
      //if(x==0)dig[x]++;
      while(x!=0)
      {dig[x%10]++;
      x/=10;
      }    
     for(int j=_x+1;;j++)
      {int _j=j;
       memset(digA,0,sizeof(digA));
       //if(_j==0)digA[_j]++;
         while(_j!=0)
         {digA[_j%10]++;
          _j/=10;           
         }
       //evaluamos:
       bool ok=1;
          for(int a=1;a<10;a++)
            if(dig[a]!=digA[a]) 
               {ok=0;break;}
         if(ok) 
          {cout<<"Case #"<<i<<": "<<j<<endl;break;}                
      }      
   }       
return 0;    
}

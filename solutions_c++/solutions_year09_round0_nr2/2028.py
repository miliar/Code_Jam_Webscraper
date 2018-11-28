#include <iostream>
using namespace std;
int T,H,W;
int M[100][100];
int parent[10000];
char print[100000]; 
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
int Find(int x)
{
 while(parent[x]!=x)
   x=parent[x];
 return x;     
}
void Union(int x,int y)
{
int _x,_y;
  _y=Find(y);
  _x=Find(x);
  if(_x!=_y)
  parent[_y]=_x;     
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
cin>>T;
for(int caso=1;caso<=T;caso++)
  {cin>>H>>W;
      for(int j=0;j<H;j++)
        for(int k=0;k<W;k++)
          cin>>M[j][k];// llenamos el mapa de altitudes
      for(int j=0;j<H;j++)
        for(int k=0;k<W;k++)    
           {parent[j*100+k]=j*100+k;
            print[j*100+k]='.'; 
           }
      char letter='a';     
     for(int j=0;j<H;j++)
        for(int k=0;k<W;k++)
         { int min=10001,x=-1,y=-1;
             for(int i=0;i<4;i++)
               if(j+dx[i]>=0&&j+dx[i]<H&&k+dy[i]>=0&&k+dy[i]<W&&M[j][k]>M[j+dx[i]][k+dy[i]])              
                 if(min>M[j+dx[i]][k+dy[i]])
                    {min=M[j+dx[i]][k+dy[i]];
                     x=j+dx[i];
                     y=k+dy[i];                          
                    }
           if(x!=-1)
             Union(j*100+k,x*100+y);                     
         }       
      cout<<"Case #"<<caso<<":"<<endl;   
      for(int j=0;j<H;j++)
        {for(int k=0;k<W;k++)
          {int aux=Find(j*100+k);
           if(print[aux]=='.')
           {print[aux]=letter;
           letter=(char)(letter+1);
           }
           cout<<print[aux]<<" ";          
          }
        cout<<endl;  
        }      
  }
return 0;    
}

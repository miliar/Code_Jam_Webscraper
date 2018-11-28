#include<iostream>
#include<vector>
using namespace std;


bool final(  vector<vector<bool> >&vb,int &maxX,int &maxY)
{
     for(int i=0;i<=maxX;i++)
     {
       for(int j=0;j<=maxY;j++)
       {
               if(vb[i][j])
               return false;
       }        
     }
     return true;
}
int vc[101][101];
void perform(  vector<vector<bool> >&vb,int &maxX,int &maxY)
{
    
         
     
     for(int i=1;i<=maxX;i++)
     {
       for(int j=1;j<=maxY;j++)
       {
               if(vb[i][j]==1)
               {
                              if(vb[i-1][j]==0 && vb[i][j-1]==0)
                              vc[i][j]=-1;
                              
                            
                                
               }else 
               {
                              if(vb[i-1][j]==1 && vb[i][j-1]==1)
                              vc[i][j]=1;
                              
               }
              
       }        
     }
     
      for(int i=1;i<=maxX;i++)
     {
       for(int j=1;j<=maxY;j++)
       {
               if(vc[i][j]==1)
               vb[i][j]=1;
               
               else if(vc[i][j]==-1)
               vb[i][j]=0;
               
               vc[i][j]=0;
               
       }
       
     }
   
}
int main()
{   
    
     freopen("out.txt","w",stdout);
   freopen("C-small-attempt0(2).in", "r", stdin);
     int T;
    cin>>T;
    
    for(int i=0;i<101;i++)
    for(int j=0;j<101;j++)
    vc[i][j]=0;
    
    
    for(int I=1;I<=T;I++)
    { 
            vector<vector<bool> >vb(101,vector<bool>(100,0));
            int R;
            cin>>R;
           int maxX=0;
           int maxY=0;
            for(int i=0;i<R;i++)
            {
               int X1,Y1,X2,Y2;
               cin>>X1>>Y1>>X2>>Y2;
              
              if(X2>maxX)
              maxX=X2;
              
              if(Y2>maxY)
              maxY=Y2;
              for(int x=X1;x<=X2;x++)
              {
                      for(int y=Y1;y<=Y2;y++)
                      {
                              vb[x][y]=1;
                      }

              }
          
               
               
            }
            
            int cnt=0;
            while(!final(vb,maxX,maxY))
            {
               perform(vb,maxX,maxY);       
               cnt++;                   
            }
            cout<<"Case #"<<I<<": "<<cnt<<endl;
            
    }
    
    
 //   system("pause");
    return 0;
    
}

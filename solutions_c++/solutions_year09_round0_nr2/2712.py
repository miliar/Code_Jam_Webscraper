#include<iostream>
using namespace std;
#include<vector>
#include<queue>
int main()
{
    int i,j,k,l,n,r,c;
    cin>>n;
    vector<string>v;
    
    string s;
    string a;
    while(n>0)
    {
          queue<pair<int,int> >q;    
          scanf("%d",&r);
          scanf("%d",&c);    
          for(i=0;i<r;i++)
          {
              cin>>s;
              v.push_back(s);
              }
          int a[r][c];
          int b[r][c];
         for(i=0;i<r;i++)
         {
                         for(j=0;j<c;j++)
                  {
                                         if(v[i][j]=='1')
                                       {    q.push(make_pair(i,j));
                                             a[i][j]=0;
                                             b[i][j]=0;
                                         }
                                          if(v[i][j]=='0')
                                            { a[i][j]=1000;
                                                  b[i][j]=1;}                                                                        
                                                                     
                    }
                      
                      
        }
                      
 while(!q.empty())
 {
        pair<int,int>p;
        p=q.front();
        q.pop();
        i=p.first;
               
        j=p.second;
                    
        int x,y;
        x=i-1;
        y=j;
        if(x<r && x>=0 && y<c && y>=0 && b[x][y]==1  )
                     {   a[x][y]=a[i][j]+1;
                         q.push(make_pair(x,y));
                         b[x][y]=0;
                         
                           }
         x=i+1;
         y=j;                  
        if(x<r && x>=0 && y<c && y>=0 && b[x][y]==1 )
                     {   a[x][y]=a[i][j]+1;
                         q.push(make_pair(x,y));
                          b[x][y]=0;
                         
                           }
         x=i;
         y=j+1;                   
         if(x<r && x>=0 && y<c && y>=0 && b[x][y]==1 )
                   {      a[x][y]=a[i][j]+1;
                          q.push(make_pair(x,y));
                          b[x][y]=0;
                          
                           }
         x=i;
         y=j-1;                   
         if(x<r && x>=0 && y<c && y>=0 && b[x][y]==1 )
               {          a[x][y]=a[i][j]+1;
                          q.push(make_pair(x,y));
                           b[x][y]=0;
                                                }
 
            
 
      } 
     
 
    
    for(i=0;i<r;i++)
    {
                    for(j=0;j<c;j++)
                    {
                                                                      cout<<a[i][j]<<" ";
                             
                                                               
                                      }
                     cout<<endl;                 
                                      }  
                                                                                   
     
     n--;
     v.erase(v.begin(),v.end());
}   
                                                                    
                                                      
                      
 system("pause");
 
}                       
                       

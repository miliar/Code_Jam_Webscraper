#include <iostream>
#include <stack>
#include <utility>
using namespace std;
int area[128][128];
char sol[128][128];

bool sink(int i,int j,int h,int w)
{
 if(j+1<w&&area[i][j+1]<area[i][j])return 0;
 if(j-1>=0&&area[i][j-1]<area[i][j])return 0;
 if(i+1<h&&area[i+1][j]<area[i][j])return 0;
 if(i-1>=0&&area[i-1][j]<area[i][j])return 0;
 return 1;
}
void ncase(int z)
{
 int h,w;
 cin>>h;
 cin>>w;
 for(int i=0;i<h;i++)
  for(int j=0;j<w;j++)
   {cin>>area[i][j];
    sol[i][j]='-';
   }
 char next='a';
 for(int i=0;i<h;i++)
  for(int j=0;j<w;j++)
  if(sol[i][j]=='-')
  {
     stack <pair <int,int> > ans;
     int l=i,m=j; 
     bool b=1;
     while(b==1)
     { if(sink(l,m,h,w)==1||sol[l][m]!='-')               
        {
         //cout<<l<<" "<<m<<" "<<sol[l][m]<<" "<<next<<endl;
         if(sol[l][m]=='-'){sol[l][m]=next;next++;}
          while (!ans.empty())
          {
                pair <int,int> t=ans.top();
                ans.pop();
                sol[t.first][t.second]=sol[l][m];
          }
          b=0;
        }
       else
       {
           ans.push(make_pair(l,m));             
           int min=area[l][m];int way=0;
           if(l+1<h&&area[l+1][m]<=min){min=area[l+1][m];way=3;}
           if(m+1<w&&area[l][m+1]<=min){min=area[l][m+1];way=2;}
           if(m-1>=0&&area[l][m-1]<=min){min=area[l][m-1];way=4;}
           if(l-1>=0&&area[l-1][m]<=min){min=area[l-1][m];way=1;}
          
          
           if(way==1)l--;
           if(way==2)m++;
           if(way==3)l++;
           if(way==4)m--;
           //cout<<i<<" "<<j<<" "<<l<<" "<<m<<" "<<endl;
           ans.push(make_pair(l,m));
       }
       //cout<<"ASADA"<<endl;
     }          
  }
  cout<<"Case #"<<z<<":"<<endl;
  for(int i=0;i<h;i++)
   {for(int j=0;j<w;j++)
     cout<<sol[i][j]<<" ";
    cout<<endl;
   }
}
int main()
{
    int x;
    cin>>x;
    for(int i=0;i<x;i++)
     ncase(i+1);   
 return 0;   
}

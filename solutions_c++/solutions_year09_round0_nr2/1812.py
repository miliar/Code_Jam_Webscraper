/* 
 * File:   main.cpp
 * Author: hussein
 *
 * Created on September 3, 2009, 10:22 AM
 */

#include "iostream"
#include "string"
#include "vector"
#include "cassert"
using namespace std;
int arr[120][120]={999999};
char ans[120][120];
char current='a';
int w,h;
/*
 * 
 */
bool first=true;
char best(int x,int y)
{
 
    if(arr[x-1][y]<arr[x+1][y] && arr[x-1][y]<arr[x][y+1] && arr[x-1][y]<arr[x][y-1])
    {   
        return 'N';
    }
    if(arr[x+1][y]<arr[x-1][y] && arr[x+1][y]<arr[x][y+1] && arr[x+1][y]<arr[x][y-1])
    {
        return 'S';
    }
    if(arr[x][y+1]<arr[x-1][y] && arr[x][y+1]<arr[x+1][y] && arr[x][y+1]<arr[x][y-1])
    {
        return 'E';
    }

    if(arr[x][y-1]<arr[x-1][y] && arr[x][y-1]<arr[x+1][y] && arr[x][y-1]<arr[x][y+1])
    {
        return 'W';
    }
    assert(x!=0&&y!=0);
   int min=999999;
   if(min>arr[x][y+1]) min=arr[x][y+1];
   if(min>arr[x][y-1]) min=arr[x][y-1];
   if(min>arr[x+1][y]) min=arr[x+1][y];
   if(min>arr[x-1][y]) min=arr[x-1][y];

   if(arr[x-1][y] == min) return 'N';
   if(arr[x][y-1] == min) return 'W';
   if(arr[x][y+1] == min) return 'E';
   if(arr[x+1][y] == min) return 'S';
   
}
char recurse(int x,int y)
{

    if(ans[x][y]!='#') return ans[x][y];
  //  ans[x][y] = current;
    int x1=x,y1=y;
    char c;
  //  ans[x][y] = current;
    c=best(x,y);
    switch(c)
    {
        case 'N':
            x1=x-1;
            break;
        case 'E':
            y1=y+1;
            break;
        case 'W':
            y1=y-1;
            break;
        case 'S':
            x1=x+1;
            break;
    }
    
    if(arr[x1][y1]>=arr[x][y]) // No More Moves
    {

      
        ans[x][y] = current;
        current++;
        return ans[x][y];
    }
 
    if(ans[x1][y1] != '#')  // Reached a known position
    {
      
        ans[x][y] = ans[x1][y1];
        return ans[x][y];
    }

 
   
        ans[x][y] = recurse(x1,y1);
        return ans[x][y];

                
}
int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int cases;
    cin>>cases;
    for(int k=0;k<cases;k++)
    {
        current = 'a';
    cin>>h>>w;
    for(int i=0;i<120;i++)
        for(int j=0;j<120;j++)
        {
            ans[i][j] = '#';
            arr[i][j] = 999999;
        }
    for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
        {
            cin>>arr[i][j];                       
        }
  
        for(int i=1;i<=h;i++)
        {
            for(int j=1;j<=w;j++)
            {
                if(ans[i][j]=='#')
                {
                    recurse(i,j);
                }
             
            }
        }
        cout<<"Case #"<<k+1<<":"<<endl;
    for(int i=1;i<=h;i++)
    {
        for(int j=1;j<=w;j++)
        {
            cout<<ans[i][j]<<" ";
          
        }
        cout<<endl;
    
    }
    }
    return 0;
}


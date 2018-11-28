#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;
long long Cmb[550][550],arr[550][550];


int main()
{
    freopen("C://Users//abir//Desktop//Topcoder//c.in","r",stdin);
    freopen("C://Users//abir//Desktop//Topcoder//c.out","w",stdout);
     int f[1000],t,i,x,cn=1,j,c,r,k,x1,y1,x2,y2;
     cin>>t;
     
     while(t--)
     {
            c=0;
        bool arr[600][600]={0};
         cin>>r;
         for(i=0;i<r;i++)
         {
            cin>>x1>>y1>>x2>>y2;
            for(j=x1+100;j<=x2+100;j++)
                   for(k=y1+100;k<=y2+100;k++)
                   {
                      if(arr[j][k]==0)arr[j][k]=1,c++;
                   }                
         }       
         x=0;
         while(c>0)
         {
             x++;   
                bool arr1[600][600]={0};
            for(i=1;i<=500;i++)
            {
                for(j=1;j<=500;j++)
                {
                    if(arr[i][j]==0)
                    {
                        if(arr[i-1][j]==1&&arr[i][j-1]==1)arr1[i][j]=1,c++;    
                    }
                    if(arr[i][j]==1)
                    {
                        if(arr[i-1][j]==0&&arr[i][j-1]==0)arr1[i][j]=0,c--;    
                        else if(arr[i-1][j]==1||arr[i][j-1]==1)arr1[i][j]=1;    
                    }    
                }
            }       
            for(i=1;i<=500;i++)
            {
                for(j=1;j<=500;j++)
                {
                    arr[i][j]=arr1[i][j];  
                }
            }
            
                
         }
         cout<<"Case #"<<cn++<<": "<<x<<endl;
     }
    cin>>i;
    
    return 0;
}

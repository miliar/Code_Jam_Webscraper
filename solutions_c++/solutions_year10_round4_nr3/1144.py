#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
int a[1002][1002]={0}; 
int b[1002][1002]={0};  
int aaa(int tempx , int tempy)  
{
    int i  , j ;
    for(i=1;i<=tempx;i++)
        for(j=1;j<=tempy;j++)
        {
            if(a[i][j]!=0)return 1;
        }
    return 0;    
}
int bbb(int tempx , int tempy)
{
    int i  , j ;
    for(i=1;i<=tempx;i++)
        for(j=1;j<=tempy;j++)
        {
            b[i][j]=a[i][j];
        }    
    for(i=1;i<=tempx;i++)
        for(j=1;j<=tempy;j++)
        {
            if(a[i][j]==1)
            {
                if(a[i-1][j]==0&&a[i][j-1]==0)b[i][j]=0;
            }
            if(a[i][j]==0) 
            {
                if(a[i-1][j]==1&&a[i][j-1]==1)b[i][j]=1;
            }       
        }
    for(i=1;i<=tempx;i++)
        for(j=1;j<=tempy;j++)
        {
            a[i][j]=b[i][j];
        }
    return 0;    
}        
int main() {
	freopen("F:\\C-small-attempt0.in", "r", stdin);
	freopen("F:\\out.txt", "w", stdout);
	int c  , ttt= 0 , r  , i  , j , p , k;
    int tempx , tempy;
    int x1 , y1 , x2 , y2 ;
    int a1 , b1 , c1 , d1 ;
    
	cin>>c;
	while(c--)
	{
	    cin>>r;

	    ttt++;
	    tempx=1;tempy=1;
	    k=0;
	    for(p=0;p<r;p++)
	    {
	        cin>>x1>>y1>>x2>>y2;
	        if(x1>x2){b1=x1; a1=x2;}
	        else {b1=x2; a1=x1;}
	        if(b1>tempy)tempy=b1;
	        if(y1>y2){d1=y1;c1=y2;}
	        else {d1=y2;c1=y1;}
	        if(d1>tempx)tempx=d1;
	        //cout<<a1<<b1<<c1<<d1<<endl;
	        for(i=c1;i<=d1;i++)
            {
                for(j=a1;j<=b1;j++)
                {a[i][j]=1;}
            }
	    } 
 
        while(aaa(tempx , tempy)!=0) 
        {
            k++;
            bbb(tempx, tempy);
	    
        }    
	    
	    for(i=0;i<=tempx;i++)
          for(j=0;j<=tempy;j++)
          {
            a[i][j]=0;b[i][j]=0;
          }
	    
       cout<<"Case #"<<ttt<<": "<<k<<endl;  
	}    
	
	return 0;
}

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
char a[51][51]; 
int b;
int b1;
   
int main() {
	freopen("F:\\B-large.in", "r", stdin);
	freopen("F:\\out.txt", "w", stdout);
	int t  , k  , ttt=0;
	int i , j;
	__int64 c;
    __int64 l , p ;
    __int64 ll; 
	cin>>t;
//	long a[9][32];
//	for(i=2;i<11;i++)
//	{
//       a[i][0]=i;
//	   for(j=1;j<31;j++)
//	   {
//	    if(a[i][j-1]>2147483647)a[i][j-1]=0;   
//        a[i][j]=a[i][j-1]*a[i][j-1];
//	   }  
//    }  
//    
	while(t--)
	{
	    ttt++;
	    k=0;
	    cin>>l>>p>>c;
	    ll=l*c;
	    while(ll<p)
	    {
           c=c*c; 
           ll=l*c;
           if(ll == 0) system("pause");
           k++;
         }
	    
       cout<<"Case #"<<ttt<<": "<<k<<endl;  
	}    
	return 0;
}

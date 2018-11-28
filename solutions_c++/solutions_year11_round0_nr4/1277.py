#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<cstring>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

int p[1010];
bool used[1010];
double fact(int n )
	{
		double ret = 1.0;
		for(int i=1 ;i<=n ; i++) ret = ret*i*1.0;
		return ret;
	}
int main()
	{
		int t , n ,  cnt, x = 1;
		double sum = 0;
		for(cin>>t ; t > 0 ; t-- )
		{
			memset( p , 0 , sizeof p );
			memset ( used , 0 , sizeof used );
			cin>>n;
			for( int i = 1 ; i <= n ; i++ ) cin>>p[i];
			sum=0;
			for(int i = 1 ; i <= n ; i++) 
			 if( !used[i] ) 
		 	  {
				used[i]=1;
				cnt = 1;
				for(int j = p[i] ; !used[j] ; j = p[j] ) used [j] =1 , cnt++;
				if ( cnt > 1 ) sum +=  cnt  ;
			  }		
			printf("Case #%d: %lf\n",x++,sum);	
		}
	}

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
vector<int> v_l,v_r;
long long  c[1010];

int main()
	{
		long long  t , n , sum_l , sum_r , s_l , s_r , n_l , n_r , ret , x = 1 , k ;
		for( cin>>t ; t>0 ; t-- )
		{

			memset( c , 0 , sizeof c ) ;
			cin>>n;
			for(int i=0;i<n;i++) cin>>c[i];
			//memset( used , 0 , sizeof used ) ;
			/*ret=-1;
			for( int i = 1 ; i < ( (1<<n)-1 )  ; i++) 
			{
				
				v_l.clear() , v_r.clear() ;
				for( int j = 0;j < n ; j++ ) 
				  if(i & (1<<j) ) v_l.push_back( c[j] );
				  else v_r.push_back( c[j] );
			
				s_l = sum_l = v_l[0] , s_r = sum_r = v_r[0] ;
				n_l = v_l.size() , n_r =  v_r.size();
				for( int j = 1 ; j < n_l ; j++ )  s_l ^= v_l[j] , sum_l += v_l[j] ;
				for( int j = 1 ; j < n_r ; j++ )  s_r ^= v_r[j] , sum_r += v_r[j] ;
				
				if(s_l ==  s_r ) ret = max ( ret , max ( sum_l , sum_r ) ) ;
			}*/


			sort( c , c + n );
			ret = c[0];
			sum_l = c[0];
			for( int i=1 ; i < n ; i++ ) ret ^= c[i] , sum_l += c[i] ;
		
			//cout<<ret<<" "<<sum_l<<endl;	
			cout<<"Case #"<<x<<": ";
			if( ret == 0 ) cout<< sum_l - c[0] <<endl;
			else cout<<"NO\n";
			x++;	
							
		}
	}	

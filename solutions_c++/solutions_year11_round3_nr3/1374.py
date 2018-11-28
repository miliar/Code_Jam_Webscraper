#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<long long> v;
int main()
	{

		long long t ,n , l , h , k ,  a, b ;
		int x=1;
		for(cin>>t ; t>0 ; t--) 
		 {
			v.clear();
			cin>>n>>l>>h;
			for(int i=0;i<n;i++) cin>>k, v.push_back(k);
			sort(v.begin(),v.end());
			int n = v.size();
		     	printf("Case #%d: ", x++);
			bool f_1=1;
			for(int i=l;i<=h;i++)
			 {
				bool f = 1;
				for(int j=0;j<n ; j++)
				 {
				
					if ( i % v[j] == 0 or v[j] % i ==0 ) {  continue;}
					else { f = 0 ; break;}
				 }
				if( f ) { cout<<i<<endl; f_1 = 0;break;}
			 }
			if(f_1) cout<<"NO\n";
		 }
	}

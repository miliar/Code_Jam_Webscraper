#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include<gmpxx.h>
using namespace std;
typedef mpz_class _int;

int main()
{
	_int T,n,n_1,n_2,n_3,x=1;
	for(cin>>T;T>0;T--)
	{
		cin>>n;
		if(n==2)
		{
			cin>>n_1>>n_2;
			//cout<<x<<" "<<n_1<<" "<<n_2<<endl;
			if(n_1>n_2) swap(n_1,n_2);
			_int t=n_2-n_1;
			if(n_2%t==0 && n_1%t==0) cout<<"Case #"<<x++<<": "<<0<<endl;
			else 
			 {
				_int m=n_1/t;
				_int tmp=(m+1)*t-n_1;
				cout<<"Case #"<<x++<<": "<<tmp<<endl;
			}
		}
		else 
		{
			vector<_int> v,v_d;
			for(int i=0;i<n;i++)cin>>n_1,v.push_back(n_1);
			sort(v.begin(),v.end());
			for(int i=0;i+1<n;i++)
			{
				v_d.push_back(v[i+1]-v[i]);
			}
			//_int t_1=v[1]-v[0],t_2=v[2]-v[1],t_3;
			_int t_3=__gcd(v_d[0],v_d[1]);
			for(int i=2;i<n-1;i++)
				t_3=__gcd(t_3,v_d[i]);
			if(v[0]%t_3==0) cout<<"Case #"<<x++<<": "<<0<<endl;
			else
			{
				_int m=v[0]/t_3;
				_int tmp=(m+1)*t_3-v[0];
				cout<<"Case #"<<x++<<": "<<tmp<<endl;
			}
		}
	}
}
					
	



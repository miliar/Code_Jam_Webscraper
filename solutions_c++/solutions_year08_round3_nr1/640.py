#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>
using namespace std;
int main()
{
	//cout<<"hello"<<endl;
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int p,k,l,t;
		cin>>p>>k>>l;
		vector<int> v;
		for( int j=0;j<l;j++)
		{
			cin>>t;
			v.push_back(t);
		}
		sort(v.begin(),v.end());
		int h = l/k,pr=0,ne = v.size();
		
		for(int u =0;u<=h;u++)
		{
			for(int w=0;w<k;w++)
			{
				if(u==h && (w+u*k) >= ne ) break; 
				pr+= (u+1)*v[ne-1 -(w + u*k)];
			}
		}
		cout<<"Case #"<<i+1<<": "<<pr<<endl;
		
	}	
	return 0;
}

#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<algorithm>
using namespace std;



main()
{
	int cases,num,p,k,l;
	vector<int> v;
	cin >> cases;

	for(int i=0;i<cases;i++)
	{
		v.clear();
		cin >> p >> k >> l;

		for(int j=0;j<l;j++)
		{
			cin >> num;
			v.push_back(num);
		}	

		cout<<"Case #"<<i+1<<": ";
		if( p*k < l)
		{
			cout<<"Impossible\n";
			continue;
		}

		sort(v.begin(),v.end());

		int count=0,n,index=0;

		for(int m=0;m<ceil(l*1.0/k);m++)
		{
			for(n=0;n<k && index < l;n++)
			{
				count+= v[l-1-index]*(m+1);
				index++;
			}	
		}

		cout<<count<<'\n';
			
		
	}
}	
		
			

		
			



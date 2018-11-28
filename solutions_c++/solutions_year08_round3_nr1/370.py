#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#ifdef ONLINE_JUDGE 
typedef long long LINT; 
typedef unsigned long long ULINT;
#else
#include <sstream>
#include <iomanip>
typedef __int64 LINT;
typedef unsigned __int64 ULINT;
ostream& operator << (ostream& os, LINT n) 
{
	stringstream strm;
	if(n<1000000000)
		strm<<(int)n;
	else
		strm<<n/1000000000<<setw(9)<<setfill('0')<<n%1000000000;
	return os<<strm.str();
}
ostream& operator << (ostream& os, ULINT n) 
{
	stringstream strm;
	if(n<1000000000)
		strm<<(int)n;
	else
		strm<<n/1000000000<<setw(9)<<setfill('0')<<n%1000000000;
	return os<<strm.str();
}
istream& operator >> (istream& is, LINT& n) 
{
	int t;
	is>>t;
	n=t;
	return is;
}
istream& operator >> (istream& is, ULINT& n) 
{
	unsigned int t;
	is>>t;
	n=t;
	return is;
}
#endif 


void main()
{
	int n;
	int p,k,l;
	int i,j;
	cin>>n;
	for(i=0; i<n; i++)
	{
		cin>>p>>k>>l;
		
		vector<int> v;
		int f;
		for(j=0; j<l ;j++)
		{
			cin>>f;
			v.push_back(f);
		}
		sort(v.begin(), v.end(), greater<int>());

		LINT num=0;
		int r=1;
		int cnt=0;
		for(j=0; j<l; j++)
		{
			num+=v[j]*r;
			if(++cnt==k)
			{
				r++;
				cnt=0;
			}
		}
		cout<<"Case #"<<i+1<<": "<<num<<endl;
	}
}
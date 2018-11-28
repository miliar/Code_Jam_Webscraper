#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <algorithm>

using namespace std;
template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

void main()
{
	ofstream ofs("D-small-attempt3.out");
	int i,j,k,jj;
	int n;
	cin>>n;
	string s;

	for(i=0; i<n; i++)
	{
		int aa[5]={0,1,2,3,4};

		cin>>k;
		cin>>s;
		if(i==5)
			int gg=1;

		int cnt=1;
		int a=0;

		for(j=1; j<s.length(); j++)
			if(s[j]!=s[j-1])
				cnt++;

		while(next_permutation(aa,aa+k))
		{
			int tt=1;
			string ns;
			for(j=0; j<s.length(); j+=k)
			{
				for(jj=0; jj<k; jj++)
				{
					ns+=s[j+aa[jj]];
				}
			}
			for(j=1; j<ns.length(); j++)
				if(ns[j]!=ns[j-1])
					tt++;

			cnt=TMIN(cnt,tt);
		}

		ofs<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
}

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <memory.h>
#include <sstream>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		int n;
		string s;
		cin>>s;
		stringstream ss;
		ss<<s;
		ss>>n;
		int k;
		int mn=2000000000;
		sort(s.begin(),s.end());
		do
		{
			if (s[0]=='0')
				continue;
			ss.clear();
			ss<<s;
			ss>>k;
			if (k>n && k<mn)
				mn=k;
			s.insert(++s.begin(),'0');
			ss.clear();
			ss<<s;
			ss>>k;
			if (k>n && k<mn)
				mn=k;
			s.erase(++s.begin());
		}
		while (next_permutation(s.begin(),s.end()));
		cout<<"Case #"<<t<<": "<<mn<<endl;
	}
	return 0;
}
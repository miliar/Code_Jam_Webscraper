#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

typedef unsigned long UL;

int main()
{
	UL N;
	cin>>N;
	for(UL i=0; i<N; ++i)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
		if(next_permutation(s.begin(), s.end()))
			cout<<s;
		else
		{
			UL skip=0;
			for(; skip < s.length(); ++skip)
				if(s[skip] != '0')
				{
					cout<<s[skip];
					break;
				}
			cout<<'0';
			for(UL i=0; i<s.length(); ++i)
				if(i != skip)
					cout<<s[i];
		}
		cout<<'\n';
	}
}

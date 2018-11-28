#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <complex>

using namespace std;

#define pb push_back
#define L(s) (int)((s).end()-(s).begin())
#define rep(i,n) for(int (i)=0;(i)<(n);++(i))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define vi vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#pragma comment(linker, "/STACK:16777216")
int test,tests;
vector<char> c;
string s;
int main()
{	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
			cin>>s;
			string t=s;
			cout<<"Case #"<<test<<": ";
			if (next_permutation(all(s)))
				cout<<s<<endl;
			else
			{
				sort(all(s));
				int k=0;
				while(s[0]=='0')
				{
					++k;
					s.erase(0,1);
				}
				cout<<s[0];
				for(int j=0;j<=k;++j)
					cout<<"0";
				cout<<s.substr(1,L(s)-1)<<endl;
			}
	}
	return 0;
}
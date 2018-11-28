#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#define F(i,a) for(int i=0;i<int((a).size());++i)
#define F2(i,j,a) F(i,a) F(j,(a)[i])
#define R(i,n) for(int i=0;i<(n);++i)
#define G(i,l,r) for(int i=(l);i<(r);++i)
#define MP make_pair
#define ALL(c) (c).begin(), (c).end()
#define X first
#define Y second
#define LL long long
#define LD long double
#define SQR(a) ((a)*(a))
using namespace std;

int main()
{
	vector<string> s(6);
	F(i,s) getline(cin,s[i]);
	map<char,char> mp;
	for (int i=0; i<3; ++i)
		for (int j=0; j<(int)s[i].size(); ++j)
			mp[s[i][j]]=s[i+3][j];
	mp['z']='q';
	mp['q']='z';

	int n;
	cin >> n;
	for (int i=1; i<=n; ++i)
	{
		string a;
		if (i==1)
			getline(cin,a);
		getline(cin,a);
		F(j,a) a[j]=mp[a[j]];
		cout << "Case #" << i << ": " << a << endl;
	}
	return 0;
}

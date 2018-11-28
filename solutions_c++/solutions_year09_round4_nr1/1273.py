#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

int v,i,j,t,n,k;
vector<int> a;
string s;
map<vector<int>,int> b;

int rec()
{
	if (b.find(a) != b.end()) return b[a];
	bool r = false;
	int i,j;
	for (i = 0;i<n;i++)
		if (a[i]>i+1) r = true;
	if (r == false) return 0;
	int x = 1000000;
	for (i = 0;i<n-1;i++)
		if (a[i]>a[i+1])
		{
			swap(a[i],a[i+1]);
			x = min(x,rec()+1);
			swap(a[i],a[i+1]);
		}
	b[a] = x;
	return x;
}

int main()
{
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
	cin >> t;
	for (v = 1;v<=t;v++)
	{
		cin >> n;
		a.clear();
		for (i = 1;i<=n;i++)
		{
			cin >> s;
			k = 0;
			for (j = 0;j<s.length();j++)
				if (s[j] == '1') k = max(k,j+1);
			a.push_back(k);
		}         
		b.clear();		
		cout << "Case #" << v << ": " << rec() << endl;
	}
	return 0;
}




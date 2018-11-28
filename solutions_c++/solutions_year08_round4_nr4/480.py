#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;
int k;
string s;
int a[20];

int go()
{
	string t = s;

	for (int i = 0 ; i < s.size() ; i += k)
	{
		for (int j = i ; j < i + k ; j++)
			t[j] = s[a[j%k]+i];
	}

	int ret = 1;
	for (int i = 1 ; i < s.size() ; i++)
		if (t[i] != t[i - 1]) ret++;


	return ret;
}

int main()
{
	ifstream cin("d.in");
	ofstream cout("d.out");

	int z;
	cin>>z;
	int tc = 1;
	while(z--)
	{
		
		cin>>k;
		
		for (int i = 0 ; i < k ; i++) a[i] = i;

		cin>>s;

		int ans = -1;

		do
		{
			int t = go();
			if (ans == -1 || t < ans) ans = t;
		}
		while(next_permutation(a, a + k));
	
		
		cout<<"Case #"<<tc++<<": "<<ans<<endl;
	}
	return 0;
}


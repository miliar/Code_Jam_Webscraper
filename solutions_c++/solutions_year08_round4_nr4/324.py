#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define eps 1e-8
#define pi acos(-1)

using namespace std;

int f(string s)
{
	int x = 1;
	for(int i=0; i<(int)s.size()-1; i++)
		if(s[i]!=s[i+1]) x++;
	return x;
}

string enc(string s, vector <int> v)
{
	if(s.size()==0) return "";
	
	string x = "";
	for(int i=0; i<v.size(); i++)
		x += s[v[i]];
	return x + enc(s.substr(v.size()), v);
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int N;
	cin>>N;
	
	for(int i=0; i<N; i++)
	{
		int k;
		string s;
		cin>>k>>s;
		
		vector <int> v(k);
		for(int j=0; j<k; j++)
			v[j] = j;
		
		int x = 1<<30;
		
		do
		{
			string s2 = enc(s, v);
			int t = f(s2);
			x = min(x, t);
		}while(next_permutation(all(v)));
		
		cout<<"Case #"<<i+1<<": "<<x<<endl;
	}
	return 0;
}

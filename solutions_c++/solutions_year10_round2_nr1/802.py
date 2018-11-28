#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>

#define all(x) x.begin() , x.end()
#define sz(x) ((int) x.size())
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define VI vector<int>
#define VS vector<string>

using namespace std;
bool func(string a,string b)
{
	return a.size() < b.size();
}

int match(string od, string nd)
{
	od=od+string(1,'/');
	nd=nd+string(1,'/');
	
	int n = min(nd.size(),od.size());
	int i=0,cnt=0;
	while(i < n)
	{
		int j=i+1;
		while(j<n && od[j] != '/' && od[j] == nd[j]) j++;
		if(j<n && od[j] == '/' && nd[j]=='/') cnt++;
		else break;
		i=j;
	}


	return cnt;
}

int main()
{
	int Te;
	cin >> Te;
	for(int te=0 ; te<Te  ; te++)
	{
		cout << "Case #"<<te+1 << ": ";
		int N,M;
		cin >> N >> M;
		cin.ignore();
		
		vector<string> exist;
		vector<string> need;
		string s;
		for(int i=0 ; i<N ; i++)
		{
			cin >> s;
			exist.push_back(s);
		}

		for(int i=0 ; i<M ; i++)
		{
			cin >> s;
			need.push_back(s);
		}

		int res=0;
		sort(all(need) , func);

		for(int i=0  ; i<need.size() ; i++)
		{
			int max_match = 0;
			for(int j=0 ; j<exist.size() ; j++)
			{
				string cur = exist[j];
				max_match = max(max_match , match(cur, need[i]));
			}

			int c = count(all(need[i]),'/');
			if(c > max_match)
				res += c-(max_match);
			exist.push_back(need[i]);
		}
		
		cout << res << endl;
	}
}

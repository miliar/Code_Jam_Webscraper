#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t, i, k; s(t);
	while(t--)
	{
		k++;
		string elements;
		int reducers;
		s(reducers);
		map<string,string> reduce_map;
		rep(i,reducers)
		{
			string r; cin >> r;
			reduce_map[r.substr(0,2)] = r.substr(2,1);
		}
		
		int eliminators;
		s(eliminators);
		set<string> eliminator_set;
		rep(i,eliminators)
		{
			string e; cin >> e;
			eliminator_set.insert(e);
			rev(e);
			eliminator_set.insert(e);
		}
		
		int len;
		s(len);
		string original_elements;
		cin >> original_elements;
		
		rep(i, len)
		{
			elements += original_elements[i];
			if(elements.sz  < 2) continue;
			string first_two = elements.substr(0,2);
			if(reduce_map.find(first_two) != reduce_map.end())
				elements = reduce_map[first_two] + elements.substr(2, elements.sz - 2);
			else
			{
				rev(first_two);
				if(reduce_map.find(first_two) != reduce_map.end())
					elements = reduce_map[first_two] + elements.substr(2, elements.sz - 2);
			}
			
			if(elements.sz < 2) continue;
			string last_two = elements.substr(elements.sz - 2, 2);
			if(reduce_map.find(last_two) != reduce_map.end())
				elements = elements.substr(0, elements.sz - 2) + reduce_map[last_two];
			else
			{
				rev(last_two);
				if(reduce_map.find(last_two) != reduce_map.end())
					elements = elements.substr(0, elements.sz - 2) + reduce_map[last_two];
			}
			if(elements.sz < 2) continue;
			int j, k;
			rep(j,elements.sz)
				repa(k,j+1,elements.sz)
				{
					string c; c.pb(elements[j]); c.pb(elements[k]);
					if(eliminator_set.find(c) != eliminator_set.end())
						{ elements = "";  break; }
				}
		}
		
		cout << "Case #" << k << ": [";
		rep(i,elements.sz)
			cout << elements[i] << (i == elements.sz - 1 ? "" : ", ");
		cout << "]" << endl;
	}
	return 0;
}

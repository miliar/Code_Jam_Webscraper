#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define dforn(a, n) for(int (a) = (n); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s); (a) >= (n); --(a))

#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define dforall(a, b) for(typeof((b).begin()) (a) = (b).rbegin(); (a) != (b).rend(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

double nodos[128];
vector<int> next[128];
map<string, int> hash;
char buffer[264];

double solve(vector<int>& f)
{
	sort(f.begin(), f.end());
	
	int pos = next[0][0];
	double ret = nodos[pos];
	
	while(next[pos].size() > 0)
	{
		if(binary_search(f.begin(), f.end(), pos))
			pos = next[pos][0];
		else
			pos = next[pos][1];
		
		ret *= nodos[pos];
	}
	
	return ret;
}

int main()
{
#ifdef TAVO92
	freopen("A-small.in" , "r" , stdin);
	freopen("A-small.out", "w" , stdout);
#endif
	
	int T, l, a, id, pare, sz, ava=1;
	scanf("%i", &T);
	string name;
	double val;
	char tc;
	
	forn(t, T)
	{
		scanf("%i", &l); cin.getline(buffer, 264);
		forn(i, 120) next[i].clear();
		hash.clear();
		
		stack<int> st; st.push(0);
		
		ava = 1;
		
		forn(yuytu, l)
		{
			cin.getline(buffer, 264);
			stringstream strm;
			strm << buffer;
			
			while(strm >> tc && tc != '(' && tc != ')');
			
			
			if(tc == ')')
				{st.pop(); continue;}
			
			strm >> val >> name;
			
			pare = 0;
			dforn(i, name.size()-1)
			{
				if(name[i] != ')') break;
				++pare;
			}
		
			name = name.substr(0, name.size()-pare);

			if(name.size() == 0)
				id = ava;
			else
				id = hash[name] = ava;
			++ava;

			nodos[id] = val;
			next[st.top()].push_back(id);
			st.push(id);
			
			forn(i, pare) st.pop();
		}
		
		printf("Case #%i:\n", t+1);
		scanf("%i", &a); cin.getline(buffer, 264);
		
		forn(i, a)
		{
			cin.getline(buffer, 264);
			stringstream strm; strm << buffer;
			
			strm >> name >> sz;
			id = hash[name];
			vector<int> feat(sz,0);
			
			forn(i, sz)
			{
				strm >> name;
				
				if(hash.count(name))
					feat[i] = hash[name];
				else
					feat[i] = INF;
			}
			printf("%.7f\n", solve(feat));
		}
		
	}
	
	return 0;
}

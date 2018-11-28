#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <bitset>

#define f(i, n)             for(int i = 0; i < n; i++)
#define s(n)				scanf("%d",&n)
#define sl(n) 				scanf("%lld",&n)
#define sf(n) 				scanf("%lf",&n)
#define sc(n)               scanf("%s", &n)    
#define fill(a,v) 			memset(a, v, sizeof a)
#define ull 				unsigned long long
#define ll 					long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb          		push_back
#define gcd					__gcd
#define inf (int)1e9
#define gc getchar_unlocked
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

int n, m;
vector <int> v[210];
map <string, int> M;
string exist[110], create[110];

vector <string> get(string s)
{
	vector <string> ret;
	int l = s.length();
	string tmp = "";
	for(int i = 1; i < l; i++)
	{
		if(s[i] == '/')
		{
			ret.pb(tmp);
			tmp = "";
		}
		else tmp.pb(s[i]);
		cout << "tmp : " << tmp << endl;
	}
	
	return ret;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t, p = 1;
	s(t);
	string tmp, home, x;
	
	for(int test = 1; test <= t; test++)
	{
		M.clear();
		p = 0;
		
		s(n); s(m); 
		f(i, n) cin >> exist[i];
		f(i, m) cin >> create[i];
		
		/*if(n > 0) 
		{
			string s = exist[0].substr(1);
			for(int i = 0; i < s.length(); i++) if(s[i] == '/') {s = s.substr(0, i); break;}
			home = s;
			M[s] = 0;
		}
		else if(m > 0)
		{
			string s = create[0].substr(1);
			for(int i = 0; i < s.length(); i++) if(s[i] == '/') {s = s.substr(0, i); break;}
			home = s;
			M[s] = 0;
		}
		else 
		{
			printf("Case #%d: 0\n", test);
			continue;
		}*/
		
		int cnt = 0;	
		f(i, n)
		{
			string s = exist[i];
			f(j, s.length()) if(s[j] == '/') s[j] = ' ';
			//cout << s << endl;
			stringstream ss;
			ss << s;
			//ss >> home;
			
			x = "";
			while(ss >> tmp)
			{
				x += "/" + tmp;
				if(M.find(x) == M.end()) M[x] = p++;
			}
		}
		
		f(i, m)
		{
			string s = create[i];
			f(j, s.length()) if(s[j] == '/') s[j] = ' ';
			//cout << s << endl;
			
			stringstream ss;
			ss << s;
			//ss >> home;
			
			x = "";
			while(ss >> tmp)
			{
				x += "/" + tmp;
				if(M.find(x) == M.end()) 
				{
					M[x] = p++;
					//cout << x << endl;
					cnt++;
				}
			}
		}
		
		printf("Case #%d: %d\n", test, cnt);
	}
}

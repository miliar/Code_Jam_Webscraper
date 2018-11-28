#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define db(x) cout << #x << " = " << x << endl
#define mod(A, B) ((((A) % (B)) + (B)) % (B))
#define Exist(container, element) (container.find(element) != container.end())
#define sz(a) int((a).size()) 
typedef long long ll;

template <class T>
void out(vector<T> v)
{
  cout << "{";
  For(_i,v.size()) {if(_i) cout<<","; cout<<v[_i];}
  cout<<"}"<<endl;
}

ll dif(string s)
{
	set<char>my;
	For(i,sz(s)) my.insert(s[i]);
	return sz(my);
}

int main ()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T;
	fin >> T;
	string s;
	For(z,T)
	{
		fin  >> s;
		ll base = dif(s);
		if(base == 1) base = 2;
		map<char,ll>my;
		ll t = 1;
		int idx = 0;
		my[s[0]] = 1;
		Fori(i,1,sz(s))
		{
			if(my.count(s[i]))
			{
				t = (t * base) + my[s[i]];
			}
			else
			{
				my[s[i]] = idx;
				t = (t * base) + (ll)idx;
				if(idx == 0)
				    idx += 2;
				else
				    ++idx;
			}
		}
		fout << "Case #" << z + 1 << ": " << t << endl;
	}
	fout.close();
	db("Done");
	getchar();
	return 0;
}

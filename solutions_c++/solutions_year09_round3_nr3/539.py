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

int findLeft(set<int>my, int target)
{
	int res = INT_MIN;
	Forstl(it,my)
	{
		if(*it >= target) continue;
		res = max(res, *it);
	}
	return res;
}

int findRight(set<int>my, int target)
{
	int res = INT_MAX;
	Forstl(it,my)
	{
		if(*it <= target) continue;
		res = min(res, *it);
	}
	return res;
}

int main ()
{
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	int T;
	fin >> T;
	For(z,T)
	{
		int P, Q;
		fin >> P >> Q;
		vector<int> v(Q);
		For(i,Q) fin >> v[i];
		sort(All(v));
		int res = INT_MAX;
		do
		{
			set<int> my;
			my.insert(0); my.insert(P+1);
			int cur = 0;
			//out(v);
			Forstl(it,v)
			{
				int t = (*it-findLeft(my,*it)-1) + (findRight(my,*it)-*it-1);
				//db(t);
				cur += t;
				my.insert(*it);
			}
		//	db("");
			res = min(res, cur);
		} while(next_permutation(All(v)));
		fout << "Case #" << z + 1 << ": " << res << endl;
	}
	fout.close();
	db("Done!");
	getchar();
	return 0;
}

/*
 * Util defines and templates written by me before the GCJ2008 contest started
 * Andre Susano Pinto <andresusanopinto@gmail.com>
 */
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
#include <cfloat>
#include <queue>
#include <climits>
#include <cassert>

typedef unsigned int uint32;
typedef unsigned long long uint64;

using namespace std;

template<typename T> typename T::iterator IterBegin(T &t) { return t.begin(); }
template<typename T> typename T::iterator IterEnd  (T &t) { return t.end(); }
template<typename T,int S> T* IterBegin(T (&t)[S]) { return t+0; }
template<typename T,int S> T* IterEnd  (T (&t)[S]) { return t+S; }

template<typename T> typename T::const_iterator IterBegin(const T &t) { return t.begin(); }
template<typename T> typename T::const_iterator IterEnd  (const T &t) { return t.end(); }
template<typename T,int S> const T* IterBegin(const T (&t)[S]) { return t+0; }
template<typename T,int S> const T* IterEnd  (const T (&t)[S]) { return t+S; }

template<typename T> int size(const T &t) { return t.size(); }
template<typename T, int S> int size(const T (&t) [S]) { return S; }

template<typename T> T read()
{
	T t;
	cin >> t;
//	cerr << "read: " << t << endl;
	return t;
}

int readtime()
{
	int a, b;
	char t;
	cin >> 	a >> t >> b;
	return a*60 + b;
}

string readline()
{
	string line;
	getline(cin, line);
	return line;
}

template <typename T> inline void reset(T &t, const T &val) { t = val; }
template <typename T, int S> void reset(T (&t) [S], const T &val)
{
	for(int i=0; i<S; i++) reset(t[i], val);
}

vector<string> parse_strings(const string &s)
{
	istringstream is( s);
	string t;
	vector<string> vs;
	while(is >> t) vs.push_back(t);
	return vs;
}

void solve();

int main()
{
	int cases;
	cin >> cases; cin.ignore();
	for(int i=1; i<=cases; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}


/*
 * Code itself
 */

struct DJSet
{
    vector<int> id;

                   
    DJSet(int sz) : id(sz)
    {                     
        for(int i=0; i<(int)id.size(); i++) id[i] = i;
    }                                                    
                                                         
    int getid(int p)                                     
    {                                                    
        if(id[p] == p) return p;                         
        return id[p] = getid(id[p]);                     
    }                                                    
                                                         
    bool join(int a, int b)                              
    {                                                    
        int ia = getid(a), ib = getid(b);                
        if(ia == ib) return false;
        id[ib] = ia;
        return true;
    }               

};



void solve()
{
	long long A, B, P;
	cin >> A >> B >> P;

	DJSet dj(B+1);
	for(int i=A; i<=B; i++)
	{
		int N = i;
//		cout << i << endl;
		for(int t=2; t <= i; t++)
		{
			while(N % t == 0)
			{
//				cout << N << endl;
				if(t >= P)
				{
//					cout << t << "+" << i << endl;
					dj.join(t, i);
				}
				N /= t;
			}
		}
	}

	set<int> nums;
	for(int i=A; i<=B; i++)
	{
//			cout << i << ":" << dj.getid(i) << endl;
			nums.insert(  dj.getid(i) );
	}
	

	cout << nums.size() << endl;

}


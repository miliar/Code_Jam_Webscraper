
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>  
using namespace std;


#define oo (int)1e8
#define v(x) vector<x>
#define pb push_back
#define sz size()
#define forz(i,n) for(int i = 0; i < (n); i++)
#define foro(i,o) for(int i = 0; i < (o).size(); i++)
#define fore(i,o) for(typeof((o).begin()) i = (o).begin(); i != (o).end(); i++)
#define all(a) (a).begin(),(a).end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define isto(c,x) ((c).find(x) != (c).end()) 
#define ist(c,x) (find(ALL(c),x) != (c).end()) 
#define GI ({int t; scanf("%d",&t);t;})

#define dbg(x) (cerr << #x << ": " << x<<'\t')
#define dbge(x) (dbg(x),cerr << endl)
#define iamhere (cout<< "I am here!!\n")

typedef pair<int,int> ii; 
typedef stringstream ss;
typedef long long ll;
typedef long double ld;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef priority_queue<ii,vector<ii>,greater<ii> > p_q;

template <class T>
inline void cmax(T &a, T b) { a = max(a,b); } 
template <class T>
inline void cmin(T &a, T b) { a = min(a,b); } 
string arr[6000];

set<char> getChar(string str, int& in)
{
	set<char> ret;
	if(str[in] != '(' ) ret.insert(str[in++]); 
	else
	{
		in++;
		while(str[in] != ')')
		{
			ret.insert(str[in++]);
		}
		in++;
	}
	return ret;
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int L = GI, D = GI, N = GI;
	forz(i,D) cin >> arr[i];
	forz(t,N)
	{

		vector<set<char> > str(L);
		string Str;
		cin >> Str;
		int in = 0;
		forz(i,L) {
			str[i] = getChar(Str,in);
		}
		int cnt = 0;
		forz(i,D)
		{
			int f = 0;
			forz(j,L)
			{
				if(str[j].count(arr[i][j])) continue;
				f = 1; break;
			}
			if(!f) cnt++;
		}
		cout << "Case #"<<t+1<<':'<<" "<<cnt<<endl;
	}
	return 0;
}


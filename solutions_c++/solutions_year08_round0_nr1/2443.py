//Saving the Universe
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
int s;int q;
vs arr, que;
int doit(int in)
{
	vi flag(s,false);
	forz(j,q)
	{
		if(j < in) continue;
		forz(i,s) {
		if(que[j] == arr[i])
		{
			flag[i] = true;
			if(accumulate(all(flag),0) == s) 
			{
				return 1+doit(j);
			}
		}
		}
	}
	return 0;
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int t=GI,T=0;
	while(t-->0)
	{
		arr.clear(), que.clear();
		string temp; 
		s=GI;
		getchar();
		forz(i,s)
		{
			getline(cin,temp);
			arr.pb(temp);
//			cout << temp << endl;
		}
		
		q=GI;
		getchar();
		forz(i,q)
		{
			getline(cin,temp);
			que.pb(temp);
//			cout << temp << endl;
		}
		T++;
		cout << "Case #"<<T<<": "<<doit(0) << endl;
	}
	return 0;
}


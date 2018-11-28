// Author: Vijay S, MIT, Anna University.
// stock charts
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
#define LET(a,b) __typeof__(b) a(b)
#define v(x) vector<x>
#define pb push_back
#define sz size()
#define forz(i,n) for(int i = 0; i < (n); i++)
#define foro(i,o) for(int i = 0; i < (o).size(); i++)
#define fore(i,o) for(LET(i,o.begin()); i != (o).end(); i++)
#define all(a) (a).begin(),(a).end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define isto(c,x) ((c).find(x) != (c).end()) 
#define ist(c,x) (find(all(c),x) != (c).end()) 
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

template<class A, class B> A cvt(B a) { ss in; in << a; A ret; in >> ret; return ret; }
template <class T>
inline void cmax(T &a, T b) { a = max(a,b); } 
template <class T>
inline void cmin(T &a, T b) { a = min(a,b); } 
vvi Arr;
int n,k;
int p;
int ans;
int st[150];
int Con[150][150];

bool isconf(int a, int b)
{
	for(int i = 0;i < k; i++)
	{
		if(Arr[a][i] >= Arr[b][i] ) return true;
	}
	return false;
}

void go(int a)
{
	int f = 0;
	if(a == n)
	{
		ans = min(ans,p);
		return;
	}
	for(int i = 0;i < p;i++)
	{
		if(!Con[st[i]][a])
		{
			int t = st[i];
			st[i] = a;
			go(a+1);
			st[i] = t;
			f = 1;
		}
	}
	if(f == 0) 
	{
		st[p++] = a;
		go(a+1);
		p--;
	}
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int t = GI;
	int tt = 0;
	while (tt<t)
	{
		cout << "Case #"<<++tt<<": ";
		int n = GI, k = GI;
		vvi arr(n,vi(k));
		forz(i,n) forz(j,k) cin >> arr[i][j];
		sort(all(arr));
//		forz(i,n) forz(j,k) cout <<  arr[i][j]<< (j+1==k?"\n":" ");
		Arr=arr;
		::n=n, ::k=k;
		ans = oo, p = 0;
		clr(Con, 0);
		forz(i,n) forz(j,n)
		{
			if(j > i)
			if(isconf(i,j)) Con[j][i] = Con[i][j] = 1;
		}
//		forz(i,n) forz(j,n) 
//			cout << Con[i][j] << (j+1==n?"\n":" ");
		go(0);
		cout << ans << endl;
	}	
}


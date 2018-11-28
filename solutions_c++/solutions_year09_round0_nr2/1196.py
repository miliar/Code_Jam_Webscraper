//watersheds

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
int arr[110][110];
char f[110][110];
int n,m;

int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};
int dl = 4;

int flow(int i, int j, int cnt)
{
	if(f[i][j] != 0) return f[i][j];
		int mini = -1, minj = -1, min = arr[i][j];
	forz(k, dl) 
	{
		int ni = i+di[k], nj = j+dj[k];
		if(ni >= 0 && nj >= 0 && ni < n && nj < m)
		{
			if(arr[ni][nj] < min) mini = ni, minj = nj, min = arr[ni][nj];
		}
	}
	if(mini == -1)
		f[i][j] = cnt;
	else 
        f[i][j] = flow(mini,minj, cnt);
	return f[i][j];
}

int main()
{
//	ios_base:: sync_with_stdio(false);
	int t = GI;
	forz(T,t)
	{
		memset(f,0,sizeof(f));
		cout << "Case #"<<T+1<<':'<<endl;
		n = GI, m = GI;
		forz(i,n)
			forz(j,m)
			{
				arr[i][j] = GI;
			}
		int cnt = 97;
		forz(i,n)
			forz(j,m)
			{
				if(f[i][j] == 0)
				{
                    int ret = flow(i,j, cnt);		
					if(ret == cnt) cnt++;
				}
			}
		forz(i,n) {
			forz(j,m)
				cout << f[i][j] << " ";
			cout << endl;
		}
	}
	return 0;
}


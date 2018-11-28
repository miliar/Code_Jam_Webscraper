#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != (c).end())
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}
inline int bitcnt(int n) {int ret = 0; while(n) { ret += n&1; n>>=1;}return ret; }

char table[51][51];
char eff[51][51];
int n,kk;

void rotate()
{
	memset(eff,'.',sizeof(eff));
	for(int i=0;i<n;++i)
	{
		int cnt = 0;
		for(int j=0;j<n;++j)
		{
			if(table[i][n-1-j] != '.')
			{
				eff[n-1-cnt][n-1-i] = table[i][n-1-j];
				++cnt;
			}
		}
	}
}

bool check(char p)
{
	int dx[2] = {1,-1};
	int dy[2] = {1,1};
	for(int i=0;i<n;++i)
	{
		for(int ch = 0;ch<2;++ch)
		{
			int ny = 0;
			int nx = i;
			if(ch == 1)
				swap(ny,nx);

			for(int k=0;k<2;++k)
			{
				int nCnt = eff[ny][nx] == p ? 1 : 0;
				int nMax = 0;
				while(true)
				{
					int gy = ny + dy[k];
					int gx = nx + dx[k];
					nMax = max(nMax,nCnt);

					if(gy >= n || gx >= n || gx < 0 || gy < 0)break;

					if(eff[gy][gx] == p)
					{
						++nCnt;
					}
					else
					{
						nCnt = 0;
					}
					ny = gy;
					nx = gx;
				}
				if(nMax >= kk)return true;
			}
		}
	}
	for(int i=0;i<n;++i)
	{
		int nCnt = 0;
		int nMax = 0;
		for(int j=0;j<n;++j)
		{
			nMax = max(nMax,nCnt);
			if(eff[j][i] == p){
				nCnt++;
			}
			else{
				nCnt = 0;
			}
		}
		nMax = max(nMax,nCnt);
		if(nMax >= kk)return true;
	}

	for(int i=0;i<n;++i)
	{
		int nCnt = 0;
		int nMax = 0;
		for(int j=0;j<n;++j)
		{
			nMax = max(nMax,nCnt);
			if(eff[i][j] == p){
				nCnt++;
			}
			else{
				nCnt = 0;
			}
		}
		nMax = max(nMax,nCnt);
		if(nMax >= kk)return true;
	}

	return false;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int tests;
	cin>>tests;
	for(int test=1;test<=tests;++test)
	{
		cin>>n>>kk;
		memset(table,0,sizeof(table));
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				cin>>table[i][j];
		rotate();

		bool B,R;
		B = check('B');
		R = check('R');
		if(B && R)
		{
			printf("Case #%d: %s\n",test,"Both");
		}
		else if(!B && !R)
		{
			printf("Case #%d: %s\n",test,"Neither");
		}
		else if(B)
		{
			printf("Case #%d: %s\n",test,"Blue");			
		}
		else if(R)
		{
			printf("Case #%d: %s\n",test,"Red");			
		}
	}
	return 0;
} 
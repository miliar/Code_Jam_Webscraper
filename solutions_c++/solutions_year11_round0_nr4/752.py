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
#include <memory.h>
#include <stdio.h>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != string::npos)
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests; cin>>tests;
	for(int test=1;test<=tests;++test){
		int data[1001];
		bool vis[1001]; memset(vis,0,sizeof(vis));
		double ans = 0.0;
		int n; cin>>n;
		for(int i=0;i<n;++i){
			cin>>data[i];
			--data[i];
		}
		for(int i=0;i<n;++i){
			if(data[i] != i && vis[i] == false){
				int cnt = 0;
				int now = i;
				while(true){
					++cnt;
					vis[now] = true;
					now = data[now];
					if(now == i) break;
				}
				ans += 1.0*cnt;
			}
		}
		/*
		double exp = 1.0/2;
		double prev = 1.0/4;
		double prevLast = prev;
		for(int i=3;i<=1000000;++i){
			double now = prev*0.5 + prevLast/3.0;
			prev = now;
			exp = exp + i*now;
			prevLast = prevLast/3.0;
		}
		printf("%lf\n",exp);
		*/
		printf("Case #%d: %.6lf\n",test,ans);
	}
	return 0;
} 

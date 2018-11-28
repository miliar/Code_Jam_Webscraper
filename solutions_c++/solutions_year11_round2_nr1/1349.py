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
#define present(c,x) ((c).find(x) != (c).end())
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
		double wp[101];
		int wpCnt[101];
		int wpWin[101];
		double owp[101];
		double oowp[101];
		char table[101][101];
		int n; cin>>n;
		for(int i=0;i<n;++i){
			for(int j=0;j<n;++j){
				cin>>table[i][j];
			}
		}
		for(int i=0;i<n;++i){
			int win = 0;
			int lose = 0;
			for(int j=0;j<n;++j){
				if(table[i][j] == '1')++win;
				if(table[i][j] == '0')++lose;
			}
			wpWin[i] = win;
			wpCnt[i] = win+lose;
			wp[i] = 1.0 * wpWin[i] / wpCnt[i];
		}

		for(int i=0;i<n;++i){
			double p = 0.0;
			int cnt = 0;
			for(int j=0;j<n;++j){
				if(table[i][j] == '1' || table[i][j] == '0'){
					double x = 0;
					if(table[j][i] != '.'){
						if((wpCnt[j]-1) != 0){
							if(table[j][i] == '1')
								x = 1.0 * (wpWin[j]-1) / (wpCnt[j]-1);
							else
								x = 1.0 * (wpWin[j]) / (wpCnt[j]-1);
						}
						else
							x = 0.0;
						if(x < 0) x= 0;
					}
					else x = 1.0 * wpWin[j] / (wpCnt[j]);
					p += x;
					++cnt;
				}
			}
			owp[i] = p / cnt;
		}

		for(int i=0;i<n;++i){
			double p = 0.0;
			int cnt = 0;
			for(int j=0;j<n;++j){
				if(table[i][j] == '1' || table[i][j] == '0')p += owp[j], ++cnt;
			}
			oowp[i] = p / cnt;
		}
		printf("Case #%d:\n",test);
		for(int i=0;i<n;++i){
			double p = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%llf\n",p);
		}
	}
	return 0;
} 

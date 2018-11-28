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
		int r,c; cin>>r>>c;
		char table[51][51];
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j){
				cin>>table[i][j];
			}
		}
		bool ok = true;
		for(int i=0;i<r;++i){
			for(int j=0;j<c;++j)if(table[i][j] == '#'){
				int nMax = 0;
				bool sub = true;
				for(int k=j, l = i ;k<j+1 && l<i+1;++k,++l){
					if(i+1 >= r || k >= c) { sub = false; break; }
					if(table[i+1][k] != '#'){ sub = false; break; }

					if(l >= r || j+1 >= c) { sub = false; break;}
					if(table[l][j+1] != '#') {sub = false; break;}
				}

				if(sub == false){
					ok = false;
					break;
				}

				for(int k=i;k<=i+1;++k){
					for(int l=j;l<=j+1;++l){
						table[k][l] = '\\';
					}
				}
				table[i][j] = '/';
				table[i+1][j+1] = '/';
			}
			if(!ok) break;
		}
		printf("Case #%d:\n",test);
		if(!ok) printf("Impossible\n");
		else{
			for(int i=0;i<r;++i){
				for(int j=0;j<c;++j){
					cout << table[i][j];
				}
				cout << endl;
			}
		}
	}
	return 0;
} 

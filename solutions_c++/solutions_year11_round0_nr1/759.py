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

int inc(int want,int now){
	if(now == want){
		return now;
	}else if(now < want){
		return now+1;
	}else{
		return now-1;
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test; cin>>test;
	int aa = 1;
	while(test--){
		int n; cin>>n;
		vector<pair<int,int> > data;
		int left[101];
		int right[101];
		memset(left,0xff,sizeof(left));
		memset(right,0xff,sizeof(right));

		for(int i=0;i<n;++i){
			char ch;
			int num;
			cin>>ch>>num;
			if(ch == 'O')data.push_back(make_pair(0,num));
			else data.push_back(make_pair(1,num));
		}
		
		for(int i=0;i<n;++i){
			for(int j=i;j<n;++j){
				if(data[j].first == 0){
					left[i] = data[j].second;
					break;
				}
			}
			for(int j=i;j<n;++j){
				if(data[j].first == 1){
					right[i] = data[j].second;
					break;
				}
			}
		}

		int now = 0;
		int cnt = 0;
		int leftPos = 1;
		int rightPos = 1;
		while(now != n){
			if(data[now].first == 0 && left[now] == leftPos){
				++now; ++cnt;
				if(right[now] != -1)rightPos = inc(right[now], rightPos);
				continue;
			}
			if(data[now].first == 1 && right[now] == rightPos){
				++now; ++cnt;
				if(left[now] != -1)leftPos = inc(left[now], leftPos);
				continue;
			}
			
			if(left[now] != -1)leftPos = inc(left[now], leftPos);
			if(right[now] != -1)rightPos = inc(right[now], rightPos);
			++cnt;
		}
		cout << "Case #" << aa << ": " << cnt << endl;
		++aa;
	}
	return 0;
} 

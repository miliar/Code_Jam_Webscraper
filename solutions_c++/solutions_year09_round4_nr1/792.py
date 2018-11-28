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
 
#define mp make_pair
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

vector<int> ori;
int n;


int go()
{
	int cnt =0;
	for(int i=0;i<n;++i)
	{
		if(ori[i] > i)
		{
			int nIdx = -1;
			for(int j=i+1;j<n;++j)
			{
				if(ori[j] <= i)
				{
					nIdx = j;
					break;
				}
			}
			for(int j=nIdx;j>i;--j)
			{
				swap(ori[j],ori[j-1]);
				++cnt;
			}
		}
	}
	return cnt;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test; cin>>test;
	for(int ntest=0;ntest<test;++ntest)
	{
		cerr <<ntest << endl;
		ori.clear();
		cin>>n;
		for(int i=0;i<n;++i){
			int mask =0;
			for(int j=0;j<n;++j)
			{
				char now;
				cin>>now;
				if(now != '0')
					mask = j;
			}
			ori.push_back(mask);
		}
		int ans = go();
		printf("Case #%d: %d\n",ntest+1,ans);
	}
	return 0;
} 

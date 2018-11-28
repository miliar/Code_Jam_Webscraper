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

double x[3],y[3],r[3];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test; cin>>test;
	for(int ntest=0;ntest<test;++ntest)
	{
		cerr <<ntest << endl;
		int n; cin>>n;
		long double ret = 99999999999;
		for(int i=0;i<n;++i)
			cin>>x[i]>>y[i]>>r[i];
		if(n==1)
		{
			ret = r[0];
		}
		else if(n==2)
		{
			ret = max(r[0],r[1]);
		}
		else if(n==3)
		{
			for(int i=0;i<n;++i)
			{
				long double now = r[i];
				int a,b;
				if(i==0) a =1, b=2;
				if(i==1) a = 0, b = 2;
				if(i==2) a= 0 , b= 1;
				long double d = (x[a] - x[b])*(x[a] - x[b]) + (y[a] - y[b])*(y[a] - y[b]);
				long double dist = sqrt(d) + r[a] + r[b];
				now = max(now, dist/2.0);
				ret = min(ret,now);
			}
		}
		printf("Case #%d: %llf\n",ntest+1,ret);
	}
	return 0;
} 

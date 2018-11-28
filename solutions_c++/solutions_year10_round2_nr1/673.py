#include<vector>
#include<iostream>
#include<map>
#include<queue>
#include<iterator>
#include<algorithm>
#include<iomanip>
#include<set>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<iomanip>
#include<memory>
#include<utility>
#include<tuple>
#include<queue>
#include<gmp.h>

using namespace std;

#define rep(i,N) for(int i=0;i<(N);i++)
#define repf(i,j,N) for(int i=(j);i<(N);i++)
#define repd(i,A,B) for(int i=(A);i>=(B);--i)
#define repb(i,j,k) for(int i=(j);i<=(k);i++)
#define pb push_back
#define all(x) x.begin(),x.end()
#define fore(it,C) for(auto it=(C).begin();it!=(C).end();++it)

template<typename T> inline int sz(const T& c) {return c.size();}
template<typename T> struct dumper {dumper(const T& t,int w) : t(t),w(w) {} const T& t;int w;};
template<typename T> inline dumper<T> dump(const T& t,int w=2) {return dumper<T>(t,w);}
template<typename T> inline ostream& operator<<(ostream& os,const dumper<T>& d)
{
	auto it=d.t.begin();
	for(;it!=d.t.end()-1;++it) os<<setw(d.w)<<*it<<" ";
	os<<setw(d.w)<<*it;
	return os;
}

typedef long long LL;
typedef vector<LL> VL;
typedef vector<vector<LL>> VVL;

map<string,int> mapa;

int main()
{
	int T;	
	cin >> T;
	for(int t=1;t<=T;++t)
	{
		mapa.clear();
		int N,M;
		cin>>N>>M;
		rep(n,N)
		{
			string s;
			cin>>s;
			int k=1;
			for(;k<(int)s.length();k++)
			{
				if(s[k]=='/') 
				{
					mapa[s.substr(0,k)] = 1;
				}
			}
			mapa[s.substr(0,k)] = 1;
		}
		int count = 0;
		rep(n,M)
		{
			string s;
			cin>>s;
			int k=1;
			for(;k<(int)s.length();k++)
			{
				if(s[k]=='/') 
				{
					if(mapa.find(s.substr(0,k)) == mapa.end())
					{
						mapa[s.substr(0,k)] = 1;
						count++;
					}
				}
			}
			if(mapa.find(s.substr(0,k)) == mapa.end())
			{
				mapa[s.substr(0,k)] = 1;
				count++;
			}
		}
		cout << "Case #" << t << ": " << count << endl;
	}
}



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

struct chick
{
	LL rem;
	LL speed;
	bool ok;
};

bool operator<(const chick& lhs, const chick& rhs)
{
	return lhs.rem < rhs.rem;
}


bool chick_test(LL rem, LL speed, LL t)
{
	return speed*t >= rem;
}

int main()
{
	int C;
	cin>>C;
	for(int c=1;c<=C;++c)
	{
		int N, K, B, T;
		cin>>N>>K>>B>>T;
		vector<chick> chicks(N);
		rep(n,N) 
		{
			LL loc;
			cin>>loc;
			chicks[n].rem = B-loc;
		}
		rep(n,N) cin>>chicks[n].speed;
		LL cnt=0;
		rep(n,N) if(chick_test(chicks[n].rem,chicks[n].speed,T))
		{
			chicks[n].ok = true;
			cnt++;
		}

		cout << "Case #" << c <<": ";
		if(cnt < K) 
			cout << "IMPOSSIBLE" <<endl;
		else
		{
			LL swap_count = 0;
			sort(chicks.begin(),chicks.end());

			LL cnt=0;
			int i=0;
			for(i=0;i<(int)chicks.size();i++)
			{
				if(chicks[i].ok) cnt++;
				if(cnt==K) break;
			}
			i++;
			for(;i<(int)chicks.size();i++) chicks[i].ok = false;

			for(int i=N-1;i>=0;--i) for(int j=i-1;j>=0;--j) if(chicks[i].ok)
			{
				if(!chicks[j].ok) swap_count++;
			}
			cout << swap_count << endl;
		}
	}
}


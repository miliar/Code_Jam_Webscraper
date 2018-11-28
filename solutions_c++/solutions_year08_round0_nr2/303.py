#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

struct E {
	int time, at, type;
	E() {}
	E(int time, int at, int type): time(time), at(at), type(type) {}
};

bool cmp(E a, E b) {
	if (a.time!=b.time)
		return a.time<b.time;
	else
		return a.type>b.type;
}

int readTime() {
	string s;
	cin>>s;
	int h,m;
	sscanf(s.c_str(),"%d:%d",&h,&m);
	return h*60+m;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	
	for (int tst=0; tst<tn; tst++) {
		printf("Case #%d: ",tst+1);
		int T,NA,NB;
		cin>>T>>NA>>NB;
		vector<E> e;
		for (int i=0; i<NA; i++) {
			int t1=readTime();
			int t2=readTime();
			t2+=T;
			e.pb(E(t1,0,-1));
			e.pb(E(t2,1,+1));
		}
		for (int i=0; i<NB; i++) {
			int t1=readTime();
			int t2=readTime();
			t2+=T;
			e.pb(E(t1,1,-1));
			e.pb(E(t2,0,+1));
		}
		sort(all(e),&cmp);
		int res[2];
		res[0]=res[1]=0;
		int cnt[2];
		cnt[0]=cnt[1]=0;
		for (int i=0; i<sz(e); i++) {
			cnt[e[i].at]+=e[i].type;
			if (cnt[e[i].at]<0) {
				cnt[e[i].at]++;
				res[e[i].at]++;
			}
		}
		cout<<res[0]<<" "<<res[1]<<endl;
	}

	return 0;
}

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

string p;
int k;
int n;
string str[200];

const int mod=10009;

vi solve(string s) {
	int cnt[30];
	string s0=s;
	memset(cnt,0,sizeof(cnt));
	for (int i=0; i<sz(s); i++)
		cnt[s[i]-'a']++;
	s="";
	for (int i=0; i<30; i++)
		if (cnt[i])
			s+=char(i+'a');
	vi ans(k);
	map<vi,short> cur,next;
	map<vi,short>::iterator it;
	next[vi(sz(s),0)]=1;
	for (int i=0; i<k; i++) {
		cur.swap(next);
		next.clear();
		for (it=cur.begin(); it!=cur.end(); it++) {
			vi v=it->first;
			for (int t=0; t<n; t++) {
				vi w=v;
				for (int j=0; j<sz(str[t]); j++) 
					for (int q=0; q<sz(s); q++)
						if (str[t][j]==s[q])
							w[q]++;
				next[w]=(next[w]+it->second)%mod;
			}
		}
		int res=0;
		for (it=next.begin(); it!=next.end(); it++) {
			vi v=it->first;
			int add=1;
			for (int i=0; i<sz(s0); i++) {
				int j=0;
				while (s[j]!=s0[i]) j++;
				add=add*v[j]%mod;
			}
			add=add*it->second%mod;
			res=(res+add)%mod;
		}
		ans[i]=res;
	}
	return ans;
}

void solve() {
	vi ans(k);
	for (int i=0; i<sz(p); i++)
		if (p[i]=='+')
			p[i]=' ';
	istringstream in(p);
	string tmp;
	while (in>>tmp) {
		vi add=solve(tmp);
		for (int i=0; i<k; i++)
			ans[i]=(ans[i]+add[i])%mod;
	}
	for (int i=0; i<k; i++)
		cout<<ans[i]<<" ";
	cout<<endl;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		cin>>p>>k;
		cin>>n;
		for (int i=0; i<n; i++) cin>>str[i];
		solve();
	}

	return 0;
}

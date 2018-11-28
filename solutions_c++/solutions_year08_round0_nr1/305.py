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

const int inf=1000*1000;

int a[1007][107];
int n;
vi q;

int solve(int t, int at) {
	int &res=a[t][at];
	if (res!=-1)
		return res;
	if (t==sz(q))
		return res=0;
	res=inf;
	if (q[t]!=at)
		res=solve(t+1,at);
	for (int i=0; i<n; i++)
		if (q[t]!=i)
			res=min(res,1+solve(t+1,i));
	return res;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;

	for (int tst=0; tst<tn; tst++) {
		printf("Case #%d: ",tst+1);
		scanf("%d\n",&n);
		map<string,int> num;
		int cnum=0;
		for (int i=0; i<n; i++) {
			char buf[1000];
			gets(buf);
			num[buf]=cnum++;
		}
		int m;
		scanf("%d\n",&m);
		q.clear();
		for (int i=0; i<m; i++) {
			char buf[1000];
			gets(buf);
			q.pb(num[buf]);			
		}
		int res=inf;
		memset(a,-1,sizeof(a));
		for (int i=0; i<n; i++)
			res=min(res,solve(0,i));
		cout<<res<<endl;
	}

	return 0;
}

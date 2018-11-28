#include<cstdio>
#include<iostream>
#include<sstream>
#include<string>
#include<set>
using namespace std;

string s, ts, ft;
set<string> a;
double tp[10000];
int cnt;
int lc[10000], rc[10000];
string f[10000];
char c;
stringstream ss;
double ans;

void build_tree(int i) 
{
//	cout << i << endl;
	double p;
	ss >> c;
//	cout << c << endl;
	ss >> p;
//	cout << p << endl;
	tp[i]=p;
	ss >> c;
	if (c!=')') {
		ss.putback(c);
		ss >> ft;
//		cout << ft << endl;
		f[i]=ft;
		lc[i]=++cnt;
//		tp[cnt]=p;
		build_tree(cnt);
		rc[i]=++cnt;
		build_tree(cnt);
	} else {
		//tp[i]=p; 
		return;
	}
	ss >> c;
}

void go(int i)
{
	ans*=tp[i];
	if (a.find(f[i])!=a.end()) {
		if (lc[i]!=0) go(lc[i]);
	} else if (rc[i]!=0) go(rc[i]);
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("a-large.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
	while (tt<T) {
		memset(lc,0,sizeof(lc));
		memset(rc,0,sizeof(rc));
		int L, n;
		scanf("%d\n",&L);
		s.clear();
		for(int i=0;i<L;++i) {
			getline(cin,ts);	
			s+=' '+ts;
//			cout << ts << endl;
		}
		tp[1]=1;
		cnt=1;
		ss.str(s);
//				cout << "g" << endl;
		build_tree(1);
//		cout << "g" << endl;
//		for(int i=1;i<=cnt;++i) {
//			cout << f[i] << ' ' << tp[i] << endl;
//		}	
		scanf("%d\n",&n);
		printf("Case #%d:\n",++tt);
		for(int i=0;i<n;++i) {
			a.clear();
			getline(cin,s);
			stringstream sp(s);
			int m;
			sp >> ts;
			sp >> m;
//			cout << m << endl;
			for(int j=0;j<m;++j) {
				sp >> ts; a.insert(ts);
			}
			ans=1;
			go(1);
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}
#include<set>
#include<iostream>
using namespace std;
double bas,rm;
char ts[5];
int top;
struct node{
	double lk,rk;
	string name;
	int left,right;
}a[1000000];
set<string>st;
char tc,tname[10];
pair<double,int> doit(bool check) {
	if (check)
	while (1) {
		tc=getchar();
		if (tc=='(') break;
	}
	double ret;
	scanf("%lf",&ret);
	int tt=++top;
	a[tt].name="";
	while(1) {
		tc=getchar();
		if (tc>='a'&&tc<='z') a[tt].name=a[tt].name+tc;
		else if (tc==')') {a[tt].name="";a[tt].left=a[tt].right=0;return make_pair(ret,tt);}
		else if (tc=='(') break;
	}
	pair<double,int>tp=doit(0);
	a[tt].lk=tp.first;
	a[tt].left=tp.second;
	tp=doit(1);
	a[tt].rk=tp.first;
	a[tt].right=tp.second;
	while (1) {
		tc=getchar();
		if (tc==')') break;
	}
	return make_pair(ret,tt);
}
void dfs(int k) {
	if (a[k].name=="") return;
	if (st.find(a[k].name)!=st.end()) {
		bas*=a[k].lk;
		dfs(a[k].left);
	}
	else {
		bas*=a[k].rk;
		dfs(a[k].right);
	}
}
int main()
{
	int nn;
	freopen("c:\\A-large.in","r",stdin);
	freopen("c:\\a.out","w",stdout);
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		printf("Case #%d:\n",ii);
		int l;
		scanf("%d",&l);
		gets(ts);
		top=0;
		pair<double,int>tp=doit(1);
		rm=tp.first;
		int m,n;
		scanf("%d",&m);
		while (m--) {
			string name,tt;
			cin>>name;
			scanf("%d",&n);
			st.clear();
			for (int i=1;i<=n;i++) {
				cin>>tt;
				st.insert(tt);
			}
			bas=rm;
			dfs(1);
			printf("%.7lf\n",bas);
		}
	}
}

#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
using namespace std;

const int MAXN = 110;
const int MOD =10009;

string p, s;
int cnt[50], a[MAXN][50], ans[10];
int n, k;
bool vtd[MAXN];

void calc(int k)
{
	int tmp=1, ta=0;
	for(int i=0;i<p.size();++i) {
//		cout << p[i];
		if (p[i]=='+') {
			ta+=tmp; tmp=1;
			if (ta>=MOD) ta-=MOD;
		} else {
			tmp=(tmp*cnt[p[i]-'a'])%MOD;
		}	
	}
	ta+=tmp;
	if (ta>=MOD) ta-=MOD;
//	if (k==3) 
//	cout << ta << endl;
	ans[k]+=ta;
	if (ans[k]>=MOD) ans[k]-=MOD;
}

void dfs(int dep, int st)
{
	if (dep==k) return;
	for(int i=0;i<n;++i) 
		{
		vtd[i]=true;
		for(int j=0;j<26;++j)
			cnt[j]+=a[i][j];
//		for(int j=0;j<26;++j)
//			cout << cnt[j] << ' ';
//		cout << endl;
		calc(dep+1);
		dfs(dep+1,i+1);
		vtd[i]=false;
		for(int j=0;j<26;++j)
			cnt[j]-=a[i][j];
	}
}

int main()
{
	freopen("B-small-attempt2.in","rt",stdin);
	freopen("b.out","wt",stdout);
	int T, tt=0;
	scanf("%d",&T);
	while (tt<T) {
		cin >> p >> k;
		cin >> n;
		memset(a,0,sizeof(a));
		memset(ans,0,sizeof(ans));
		for(int i=0;i<n;++i) {
			cin >> s;
			for(int j=0;j<s.size();++j)
				++a[i][s[j]-'a'];
//			for(int j=0;j<26;++j)
//				cout << a[i][j] << ' ';
//			cout << endl;
		}
		memset(cnt,0,sizeof(cnt));
		memset(vtd,0,sizeof(vtd));
		dfs(0,0);
		printf("Case #%d:",++tt);
		for(int i=1;i<=k;++i) 
			printf(" %d",ans[i]);
		printf("\n");
	}
	return 0;
}
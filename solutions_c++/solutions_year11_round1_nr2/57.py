#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> l[20001];
int b[20001];
int zero[20001];
int mark[20001];
int mask[20001];
int cnt;
char str[32];
char dic[10000][16];
int n,m;

void build(int t,vector<int> d,int k) {
	b[t]=mask[t]=0;
	for(int i=0;i<d.size();i++) for(int j=0;j<dic[d[i]][j];j++) mask[t]|=1<<dic[d[i]][j]-'a';
	int mm=0;
	for(int i=k;i<26;i++) mm|=1<<str[i]-'a';
	mask[t]&=mm;
	vector<pair<int,int> > mask1(d.size());
	vector<int> d1;
	for(int i=k;i<26;i++) if (mask[t]&1<<str[i]-'a') {
		for(int j=0;j<d.size();j++) mask1[j]=make_pair(0,j);
		for(int j=0;j<d.size();j++) for(int k=0;dic[d[j]][k];k++) if (dic[d[j]][k]==str[i]) mask1[j].first|=1<<k;
		sort(mask1.begin(),mask1.end());
		if (mask1[0].first==mask1[d.size()-1].first) continue;
		if (mask1[0].first==0) zero[t]=1; else zero[t]=0;
		for(int j=0,k=0;j<d.size();j=k) {
			d1.clear();
			for(;k<d.size() && mask1[j].first==mask1[k].first;k++) d1.push_back(d[mask1[k].second]);
			l[t].push_back(cnt++);
			build(cnt-1,d1,i+1);
		}
		return ;
	}
	b[t]=1;
	mark[t]=d[0];
}

pair<int,int> dp(int t) {
	if (!l[t].size()) return pair<int,int>(0,-mark[t]);
	pair<int,int> ret(-1,-1);
	for(int i=zero[t];i<l[t].size();i++) ret=max(ret,dp(l[t][i]));
	if (zero[t]) {
		pair<int,int> tt=dp(l[t][0]);
		tt.first++;
		ret=max(ret,tt);
	}
	return ret;
}

vector<int> d;
int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) {
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) scanf("%s",dic[i]);
		printf("Case #%d:",++cs);
		for(int i=0;i<m;i++) {
			scanf("%s",str);
			int ans=-1,ret=-1;
			for(int len=1;len<=10;len++) {
				for(int j=0;j<n;j++) if (strlen(dic[j])==len) d.push_back(j);
				if (!d.size()) continue;
				cnt=1;
				build(0,d,0);
				pair<int,int> r=dp(0);
				if (r.first>ans || r.first==ans && r.second>-ret) 
					ans=r.first,ret=-r.second;
				for(int j=0;j<cnt;j++) {
					l[j].clear();
					b[j]=zero[j]=0;
					mark[j]=-1;
				}
				d.clear();
			}
			printf(" %s",dic[ret]);
		}
		puts("");
	}
	return 0;
}

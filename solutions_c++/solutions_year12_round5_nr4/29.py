#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#define L 10000

using namespace std;

int k,n,ans,num,len;
int ch[300];
char s[L];
int bj[L],ln[L];
vector<int> lj[L];
int in[300],out[300];
int map[300][300];
pair<char,char> xl[L];

int dfs(int c){
	if (bj[c]==1)
		return 0;
	bj[c]=1;
	int ret=0;
	if (in[c]>out[c])
		ret=in[c]-out[c];
	for (int i=0;i<200;++i)
		if (map[c][i] || map[i][c])
			ret+=dfs(i);
	return ret;
}

void solve(){
	scanf("%d",&k);
	scanf(" %s",s);
	n=strlen(s);
	len=0;
	for (int i=0;i<n-1;++i){
		xl[len++]=make_pair(s[i],s[i+1]);
		if (ch[s[i]]!=0)
			if (ch[s[i+1]]!=0){
				xl[len++]=make_pair(ch[s[i]],s[i+1]);
				xl[len++]=make_pair(s[i],ch[s[i+1]]);
				xl[len++]=make_pair(ch[s[i]],ch[s[i+1]]);
			}
			else
				xl[len++]=make_pair(ch[s[i]],s[i+1]);
		else if (ch[s[i+1]]!=0)
			xl[len++]=make_pair(s[i],ch[s[i+1]]);
	}
	sort(xl,xl+len);
	len=unique(xl,xl+len)-xl;
	memset(out,0,sizeof out);
	memset(in,0,sizeof in);
	memset(map,0,sizeof map);
	for (int i=0;i<len;++i){
		map[xl[i].first][xl[i].second]=1;
		out[xl[i].first]++;
		in[xl[i].second]++;
	}
	memset(bj,0,sizeof bj);
	ans=len;
	for (int i=0;i<200;++i)
		if (bj[i]==0 && (out[i] || in[i])){
			int v=dfs(i);
			ans+=max(v,1);
		}
	printf("%d\n",ans);
}

int T,I=0;

int main(){
	memset(ch,0,sizeof ch);
	ch['o']='0';
	ch['i']='1';
	ch['e']='3';
	ch['a']='4';
	ch['s']='5';
	ch['t']='7';
	ch['b']='8';
	ch['g']='9';
	scanf("%d",&T);
	while (T--){
		printf("Case #%d: ",++I);
		solve();
	}
}


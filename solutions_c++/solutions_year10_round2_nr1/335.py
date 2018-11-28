#include<map>
#include<string>
#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;

map<string,int> mm[1000000];
int cnt;

int ins(vector<string> &s) {
	int p=0,ret=0;
	for(int i=0;i<s.size();i++) {
		if (mm[p].find(s[i])==mm[p].end()) {
			mm[p].insert(make_pair(s[i],cnt));
			cnt++;
			ret++;
		}
		p=mm[p][s[i]];
	}
	return ret;
}

char str[1000000];
void parse(char str[],vector<string> &r) {
	int l=strlen(str);
	if (l==1) return ;
	str[l]='/',str[l+1]='\0';
	string s;
	for(int i=1;str[i];i++) {
		if (str[i]!='/') s+=str[i];
		else {
			r.push_back(s);
			s="";
		}
	}
}

vector<string> v;

int main() {
	int N,cs=0,n,m;
	for(scanf("%d",&N);N--;) {
		cnt=1;
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) {
			scanf("%s",str);
			parse(str,v);
			ins(v);
			v.clear();
		}
		int ret=0;
		for(int i=0;i<m;i++) {
			scanf("%s",str);
			parse(str,v);
			ret+=ins(v);
			v.clear();
		}
		printf("Case #%d: %d\n",++cs,ret);
		for(int i=0;i<cnt;i++) mm[i].clear();
	}
	return 0;
}

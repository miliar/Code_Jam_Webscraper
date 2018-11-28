#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<map>
#include<vector>
using namespace std;
map<string,bool> wrd;
vector<char> v[16];
int l,d,n,ans;
void dfs(string tmp,int dep){
	if (dep==l){
		if (wrd[tmp]==1)
			ans++;
		return;
	}
	if (!tmp.empty() && wrd[tmp]==0)
		return;
	int i;
	for (i=0;i<v[dep].size();i++){
		tmp+=v[dep][i];
		dfs(tmp,dep+1);
		tmp.erase(dep);
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j;
	char c;
	string tmp;
	scanf("%d%d%d",&l,&d,&n);
	wrd.clear();
	while(d--){
		tmp.clear();
		for (i=0;i<l;i++){
			scanf(" %c",&c);
			tmp+=c;
			wrd[tmp]=1;
		}
	}
	for (i=1;i<=n;i++){
		for (j=0;j<l;j++){
			v[j].clear();
			scanf(" %c",&c);
			if (c=='(')
				while(c=getchar()){
					if (c==')')
						break;
					else
						v[j].push_back(c);
				}
			else
				v[j].push_back(c);
		}
		tmp.clear();
		ans=0;dfs(tmp,0);
		printf("Case #%d: %d\n",i,ans);
	}
}

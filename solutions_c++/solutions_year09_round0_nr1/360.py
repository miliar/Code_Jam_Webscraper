#include<iostream>
#include<ctype.h>
#include<string.h>
#define pb push_back
#include<vector>
using namespace std;
int L,D,M,ans;
int e[76000][26],root,pp;
vector<int> V[16];
void dfs(int d,int x){
	if(d==L)++ans;
	else{
		for(int i=0;i<V[d].size();++i){
			if(e[x][V[d][i]]>0)dfs(d+1,e[x][V[d][i]]);
		}
	}
}
int main(){
	int now,i,j;
	char s[1000];
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&M);
	root=0;
	pp=1;
	while(D--){
		scanf("%s",s);
		now=root;
		for(i=0;i<L;++i){
			if(e[now][s[i]-'a']==0)e[now][s[i]-'a']=pp++;
			now=e[now][s[i]-'a'];
		}
	}
	for(int Cas=1;Cas<=M;++Cas){
		scanf("%s",s);
		for(i=0;i<L;++i)V[i].clear();
		bool ok=true;
		for(i=0,j=0;i<strlen(s);++i){
			if(isalpha(s[i])){
				V[j].pb(s[i]-'a');
				if(ok)j++;
			}
			else if(s[i]==')'){
				j++;ok=true;
			}else if(s[i]=='('){
				ok=false;
			}

		}
		ans=0;
		dfs(0,root);
		printf("Case #%d: %d\n",Cas,ans);
	}
	return 0;
}

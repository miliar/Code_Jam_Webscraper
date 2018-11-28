#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<cmath>
#include<string>
using namespace std;

#define llong long long 
const double pi = acos(-1.0);
const int maxInt = 0x7fffffff;
const int minInt = ~maxInt;


const int N = 100005;
int ans;

struct Trie{
	Trie *son[200];
	int end;
	void init(){
		memset(this,0,sizeof(Trie));
	}
}*trie[N],mem[N];
int mm;

void add(Trie *root,char str[],bool flag){
	int i,j,k,len = strlen(str);
	for(i = 0;i<len;i++){
		k = str[i]-47;
		if(!root->son[k]){
			if(k==0 && flag)ans++;
			mem[mm].init();
			root->son[k] = &mem[mm++];
		}
		root = root->son[k];
		if(i+1==len){
			root->end++;
		}
	}
}
char str[N];
int n,m;
int main(){
	freopen("A-large.in","r",stdin);freopen("out.txt","w",stdout);
    int i,j,k,t,nc = 0;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&m);
		mm = 0;Trie tr;tr.init();
		for(i = 0;i<n;i++){
			scanf("%s",str);
			int len = strlen(str);
			str[len] = 47;
			str[len+1] = 0;
			add(&tr,str+1,false);
		}
		
		ans = 0;
		for(i = 0;i<m;i++){
			scanf("%s",str);
			int len = strlen(str);
			str[len] = 47;
			str[len+1] = 0;
			add(&tr,str+1,true);
		}
		printf("Case #%d: %d\n",++nc,ans);
	}
    return 0;
}

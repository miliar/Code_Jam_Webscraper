#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
using namespace std;

int trie[76000][26];
int ctr=0;
vector <string> vs;

void add(char * s){
	int u=0;
	for(int i=0;s[i];i++){
		if(!trie[u][s[i]-'a'])trie[u][s[i]-'a']=++ctr;
		u=trie[u][s[i]-'a'];
	}
	
}
char str[500];
int l,d,n,j;

int rec(int i, int u){
	if(i==l)return 0;
	int res=0;
	for(int j=0;j<(int)vs[i].size();j++){
		if(trie[u][vs[i][j]-'a']){
			if(i<l-1)res+=rec(i+1,trie[u][vs[i][j]-'a']);
			else res++;
		}
	}
	return res;
}

int main(){
	//freopen("A-large.in", "r", stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d %d %d", &l, &d, &n);
	vs.resize(l);
	for(int i=0;i<d;i++){scanf("%s", str); add(str);}
	for(int x=1;x<=n;x++){
		int k=0;
		scanf("%s", str);
		for(int i=0;i<l;i++)vs[i].clear();
		bool flag=0;
		for(int i=0, j=0;str[i];i++){
			if(str[i]=='(')flag=1;
			else if(str[i]==')'){flag=0;j++;}
			else{
				if(flag)vs[j]+=str[i];
				else vs[j++]+=str[i];
			}
		}
		k=rec(0,0);
		printf("Case #%d: %d\n",x,k);
		
	}
	return 0;
}
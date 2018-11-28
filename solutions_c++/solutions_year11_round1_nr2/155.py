#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

#define PB push_back
#define MP make_pair

#define maxn (20000)

char s[maxn][30];
char t[maxn][30];
int opt[maxn],len[maxn];
bool flag[maxn];
int T,n,m,now,ans;

void check_len(int x){
	for (int i=1;i<=n;i++) if (len[i]!=len[x]) flag[i]=false;
}

bool in_list(char x) {
	for (int i=1;i<=n;i++) if (flag[i])
		for (int j=0;j<len[i];j++) if (s[i][j]==x) return true;
		
	return false;
}

void exclude(char x) {
	for (int i=1;i<=n;i++) if (flag[i]) {
		bool find=false;
		for (int j=0;j<len[i];j++) if (s[i][j]==x) find=true;
		if (find) flag[i]=false;
	}
}

void reveal(char x,int r) {
	for (int i=1;i<=n;i++) if (flag[i])
		for (int j=0;j<len[i];j++) if (s[r][j]==x&&s[i][j]!=x||s[r][j]!=x&&s[i][j]==x) flag[i]=false;
}

void ask(char x,int r) {
	bool find=false;
	for (int i=0;i<len[r];i++) if (s[r][i]==x) find=true;
	
	if (find) {
		reveal(x,r);
	}
	else {
		now++; exclude(x);
	}
}

int main(){
	scanf("%d",&T);
	
	for (int tt=1;tt<=T;tt++) {
		printf("Case #%d:",tt);
		
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) scanf("%s",s[i]);
		for (int i=1;i<=m;i++) scanf("%s",t[i]);
		
		for (int i=1;i<=n;i++) len[i]=strlen(s[i]);
		
		for (int i=1;i<=m;i++) {
			ans=1;
			
			for (int k=1;k<=n;k++) {
				now=0; memset(flag,true,sizeof(flag));
				check_len(k);
				
				for (int j=0;j<26;j++) {
					if (!in_list(t[i][j])) continue;
					ask(t[i][j],k);
				}
				opt[k]=now;
			}
			
			for (int k=1;k<=n;k++) if (opt[k]>opt[ans]) ans=k;
			printf(" %s",s[ans]);
		}
		
		puts("");
 	}

	return 0;
}

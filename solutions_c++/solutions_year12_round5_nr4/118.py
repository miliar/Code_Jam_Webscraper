#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
char S[5005];
bool exist[35][35];
int conv[30], cnt[35];
void addpairs(char a,char b) {
	a -= 'a';
	b -= 'a';
	exist[a][b] = exist[a][conv[b]] = exist[conv[a]][b] = exist[conv[a]][conv[b]] = 1;
}
int main() {
	for(int i=0;i<26;++i) conv[i] = i;
	conv['o'-'a'] = 26;
	conv['i'-'a'] = 27;
	conv['e'-'a'] = 28;
	conv['a'-'a'] = 29;
	conv['s'-'a'] = 30;
	conv['t'-'a'] = 31;
	conv['b'-'a'] = 32;
	conv['g'-'a'] = 33;
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int K;
		scanf("%d%s",&K,S);
		int len = strlen(S);
		memset(exist,0,sizeof(exist));
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<len-1;++i) {
			addpairs(S[i],S[i+1]);
		}
		int ans = 0;
		for(int i=0;i<34;++i)
			for(int j=0;j<34;++j)
				if(exist[i][j]) {
					++ans;
					++cnt[j];
					--cnt[i];
				}
		int add = 1;
		for(int i=0;i<34;++i)
			if(cnt[i] > 0) {
				ans += cnt[i];
				add = 0;
			}
		ans += add;
		printf("Case #%d: %d\n",cn,ans);
	}
}

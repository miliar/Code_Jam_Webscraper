#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;


int n,m;
char words[10003][20];
char proc[30];

int len[10003];
int have[10003][26];

int si[10003];
inline int sf(int a,int b){
	if(len[a] != len[b]) return len[a] < len[b];
	for(int i = 0 ;i < 26;i ++) {
		if(have[a][proc[i]-'a'] != have[b][proc[i]-'a']){
			return have[a][proc[i]-'a'] < have[b][proc[i]-'a'];
		}
	}
	return a < b;
}

//returns negative score & original position
pair<int,int> dfs(int start,int end,int depth, int point) {
	int rs = si[start], re = si[end];
	if(start == end || depth == 26) {
		pair<int,int> ret(point,rs);
		return ret;
	}
	pair<int,int> ret = make_pair(1,rs);
	int curchar = proc[depth]-'a';
	if(have[re][curchar] != 0 ){
		//something is included
		int lasti = start;
		for(int i = start; i <= end; i ++){
			if(i == end || 
				have[si[i]][curchar] != have[si[i+1]][curchar] ){
				int curpoint = point;
				// not included. penalty
				if(have[si[i]][curchar] == 0) curpoint --;
				pair<int,int> tmp = dfs(lasti,i,depth+1,curpoint);
				if(tmp < ret) {
					ret = tmp;
				}
				lasti = i + 1;
			}
		}
	}else{
		//none was included
		return dfs(start,end,depth+1,point);
	}
	return ret;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		scanf("%d%d",&n,&m);
		for(int i = 0;i < n;i ++){
			scanf("%s",words[i]);
			for(int j = 0;j < 26 ;j++){
				have[i][j] = 0;
			}
			for(int j = 0; words[i][j]; j++) {
				have[i][(words[i][j]-'a')] |= 1<<j;
			}
			len[i] = strlen(words[i]);
		}
		printf("Case #%d:",testcase);
		for(int i = 0; i < m;i ++){
			scanf("%s",proc);
			for(int j = 0;j < n;j ++) {
				si[j] = j;
			}
			sort(si,si+n,sf);
			pair<int,int> ans = make_pair(1,0);
			int lasti = 0;
			for(int i = 0; i < n;i ++){
				if( i + 1 == n || len[si[i]] != len[si[i+1]] ) {
					pair<int,int> ret = dfs(lasti,i,0,0);
					if(ret < ans){
						ans = ret;
					}
					lasti = i + 1;
				}
			}
			printf(" %s",words[ans.second]);
		}
		printf("\n");
	}
	return 0;
}

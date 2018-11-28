#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdio>
#include <algorithm>
#define MAXN 20000

using namespace std;

struct WORD{
	char s[20];
	int pos[30],len,number;
} word[MAXN];
int n,m,test,cur = 1;
int order[30],best,bestans,cnt,l,r;
int sum[30][MAXN];
char ch[30];

void init(){
	printf("Case #%d:",cur);
	scanf("%d%d",&n,&m);
	for ( int i = 0 ; i < n ; i++ ){
		scanf("%s",word[i].s);
		word[i].len = strlen(word[i].s);
		word[i].number = i;
		for ( int j = 0 ; j < 26 ; j++ ){
			word[i].pos[j] = 0;
			for ( int k = 0 ; k < word[i].len ; k++ )
				word[i].pos[j] = word[i].pos[j]*2+(word[i].s[k]=='a'+j);
		}
	}
}

bool cmp(const WORD &q,const WORD &p){
	if (q.len<p.len) return true;
	if (q.len>p.len) return false;
	for ( int i = 0 ; i < 26 ; i++ ){
		if (q.pos[order[i]]<p.pos[order[i]]) return true;
		if (q.pos[order[i]]>p.pos[order[i]]) return false;
	}
	return true;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		init();
		for ( int i = 0 ; i < m ; i++ ){
			scanf("%s",ch);
			for ( int j = 0 ; j < 26 ; j++ ) order[j] = ch[j]-'a';
			sort(word,word+n,cmp);
			for ( int k = 0 ; k < 26 ; k++ ){
				sum[k][0] = 0;
				for ( int p = 0 ; p < n ; p++ )
					sum[k][p+1] = sum[k][p]+(word[p].pos[order[k]]>0);
			}
			best = 0;bestans = -1;
			for ( int j = 0 ; j < n ; j++ ){
				cnt = 0;
				for ( l = 0 ; word[l].len<word[j].len ; l++ );
				for ( r = n-1 ; word[r].len>word[j].len ; r-- );
				for ( int k = 0 ; k < 26 ; k++ ){
					if (sum[k][r+1]-sum[k][l]==0) continue;
					if (word[j].pos[order[k]]==0) cnt++;
					while (word[l].pos[order[k]]!=word[j].pos[order[k]]) l++;
					while (word[r].pos[order[k]]!=word[j].pos[order[k]]) r--;
				}
				if (cnt>bestans || cnt==bestans && word[best].number > word[j].number ){
					best = j;
					bestans = cnt;
				}
			}
			printf(" %s",word[best].s);
		}
		printf("\n");
	}
}

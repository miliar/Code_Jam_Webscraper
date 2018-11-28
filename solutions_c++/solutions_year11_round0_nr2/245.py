#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n,m,test,cur = 1;
char s[1000];
int g[200][200],q,w,p,h[200][200],len;
int ans[1000],tail;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		printf("Case #%d: ",cur);
		scanf("%d",&n);
		memset(g,255,sizeof(g));
		memset(h,255,sizeof(h));
		for ( int i = 0 ; i < n ; i++ ){
			scanf("%s",s);
			q = s[0]-'A';
			p = s[1]-'A';
			w = s[2]-'A';
			g[q][p] = g[p][q] = w;
		}
		scanf("%d",&m);
		for ( int i = 0 ; i < m ; i++ ){
			scanf("%s",s);
			q = s[0]-'A';
			p = s[1]-'A';
			h[q][p] = h[p][q] = 1;
		}
		scanf("%d %s",&len,s);
		for ( int i = tail = 0 ; i < len ; i++ )
			if (tail){
				q = ans[tail-1];
				p = ans[tail++] = s[i]-'A';
				if (g[q][p]!=-1){
					tail--;
					ans[tail-1] = g[q][p];
					continue;
				}
				for ( int j = 0 ; j < tail ; j++ ){
					q = ans[j];
					if (h[q][p]!=-1) tail = 0;
				}
			} else ans[tail++] = s[i]-'A';
		printf("[");
		for ( int i = 0 ; i < tail ; i++ ){
			if (i) printf(", ");
			printf("%c",'A'+ans[i]);
		}
		printf("]\n");
	}
}

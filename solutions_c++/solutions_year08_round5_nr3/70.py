#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#define task "file"

using namespace std;
int test;
int n,m;
int t[1024][11];
char map[20][20];
int mark[1024][11];

int fuck(int mask,int nn){
	if (nn>=n) return 0;
	if (mark[mask][nn]) return t[mask][nn];
	mark[mask][nn]=1;
	for (int i=0;i<m;i++){
		if (((mask>>i)&1) && map[nn][i]=='x') return 0;
		if (((mask>>i)&1) && i>0 && ((mask>>(i-1))&1)) return 0;
		if (((mask>>i)&1) && i<m-1 && ((mask>>(i+1))&1)) return 0;
	}
	int res=0;
	int cnt=0;
	for (int i=0;i<m;i++)
		if (((mask>>i)&1)) cnt++;
	for (int j=0;j<(1<<m);j++){
		int f=1;
		for (int i=0;i<m;i++){
			if (((j>>i)&1) && map[nn+1][i]=='x'){
				f=0;
				break;
			}
			if (((j>>i)&1) && i>0 && ((j>>(i-1))&1)){
				f=0;
				break;
			}
			if (((j>>i)&1) && i<m-1 && ((j>>(i+1))&1)){
				f=0;
				break;
			}
			if (((j>>i)&1) && i>0 && ((mask>>(i-1))&1)){
				f=0;
				break;
			}
			if (((j>>i)&1) && i<m-1 && ((mask>>(i+1))&1)){
				f=0;
				break;
			}
		}
		if (f){
			int cur=cnt+fuck(j,nn+1);	
			if (res<cur) res=cur;
		}	
	}
	t[mask][nn]=res;
	return res;	
}

int main(void){
	freopen(task".in","r",stdin);
	freopen(task".out","w",stdout);
	scanf("%i\n",&test);
	for (int zzz=1;zzz<=test;zzz++){
		printf("Case #%i: ",zzz);
		memset(mark,0,sizeof(mark));
		scanf("%i %i\n",&n,&m);
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				scanf("%c",&map[i][j]);	
			}
			scanf("\n");
		}
		int ans=0;
		for (int i=0;i<(1<<m);i++){
			int cur=fuck(i,0);
			if (cur>ans) ans=cur;
		}
		printf("%i\n",ans);
	}


	return 0;
}

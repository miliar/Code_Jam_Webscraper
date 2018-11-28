#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cassert>
#include <cstring>
#include <cstdlib>

using namespace std;

#define fo(i,n) for(int i=0;i<n;i++)

int needs[2000][4000];
int needc[2000];
int sat[2000];
#define UNMALT 1
#define MALT 2
int value[2000];

void solve(){
	int n,m; // my m,n are the opposite to the problem statement.
	scanf("%d %d",&m,&n);

	memset(needs,0,sizeof(needs));
	memset(needc,0,sizeof(needc));
	memset(sat,0,sizeof(sat));
	memset(value,0,sizeof(value));

	fo(i,n){
		int j;
		scanf("%d",&j);
		while(j--){
			int flav,malt;
			scanf("%d %d",&flav,&malt);
			flav--;
			needs[i][flav*2+malt]=1;
			needc[i]++;
//			printf("%d needs %d\n",i,flav*2+malt);
		}
	}

	while(true){
		int f=-1;
		fo(i,n) if(!sat[i]&&needc[i]==1) {
			fo(j,m*2)if(needs[i][j]){f=j;break;}
			break;
		}
		if(f==-1) break;
//		printf("setting flav = %d\n",f);
		fo(i,n) if(needs[i][f]) sat[i]=1;
		fo(i,n) if(!sat[i]&&needs[i][f^1]) {
			needs[i][f^1]=0;
			if(needc[i]==1) { printf("IMPOSSIBLE\n"); return; }
			needc[i]--;
		}

		int malt=1+(f&1);
		f>>=1;

		if(value[f]&&value[f]!=malt) { printf("IMPOSSIBLE\n"); return; } // this case should never happen anyway
		value[f]=malt;
	}

	fo(i,n) if(!sat[i]) assert(needc[i]>=2);

	fo(i,m) printf("%d%c",max(value[i]-1,0),i==m-1?'\n':' ');

	return;
}

int main(void){
	int t;
	scanf("%d",&t);
	fo(i,t){printf("Case #%d: ",i+1);solve();}
	return 0;
}

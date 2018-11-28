#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct{
	int jenis;
	bool malt;
}data;

int n,m,t,p;
int minim;
vector<data> milk[2000];

int main(){
	int i,j,k,l,jen,mal,hasil;
	data push;
	
	//printf("%d\n",__builtin_popcount(7));
	scanf("%d",&n);
	for (i=0;i<n;i++){
		hasil=-1;
		scanf("%d %d",&m,&p);
		minim=m+2;
		for (j=0;j<p;j++){
			milk[j].clear();
			scanf("%d",&t);
			for (k=0;k<t;k++){
				scanf("%d %d",&jen,&mal);
				push.jenis=jen-1;
				push.malt=mal;
				milk[j].push_back(push);
			}
		}
		
		for (j=1<<m;j>=0;j--){
			int remain=p;
			for (k=0;k<p;k++){
				for (l=0;l<milk[k].size();l++){
					//printf("%d %d\n",j,(j & 1<<milk[k][l].jenis)!=0);
					if (((j & 1<<milk[k][l].jenis)!=0)==milk[k][l].malt) {
						remain--;
						break;
					}
				}

				if (l==milk[k].size()) break;
			}
			if (remain==0) {
				if (minim>__builtin_popcount(j)){
					minim=__builtin_popcount(j);
					hasil=j;
				}
			}
		}
		
		printf("Case #%d:",i+1);
		if (hasil==-1) {
			puts(" IMPOSSIBLE");
			continue;	
		}
		for (j=0;j<m;j++){
			printf(" %d",(hasil & 1<<j)!=0);
		}
		printf("\n");
	}
	return 0;
}

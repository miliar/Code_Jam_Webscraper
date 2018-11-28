#include<cstdio>
#define L 20000
#define R 200
using namespace std;

const int fx[4]={-1,0,0,1};
const int fy[4]={0,-1,1,0};

int fa[L];

int father(int a){return fa[a]==a?a:fa[a]=father(fa[a]);}
bool merge(int a,int b){
	a=father(a);
	b=father(b);
	if (a==b) return false;
	if (a>b) a^=b^=a^=b;
	fa[b]=a;
}

int map[R][R],bh[R][R];
int T,h,w,tmp,i,j,k,nx,ny,I=0,a,low,id;
char ch[L];

int main(){
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&h,&w);
		tmp=0;
		for (i=0;i<h;++i)
		    for (j=0;j<w;++j){
		        scanf("%d",&map[i][j]);
		        bh[i][j]=tmp++;
			}
		for (i=0;i<tmp;++i) fa[i]=i;
		for (i=0;i<h;++i)
		    for (j=0;j<w;++j){
				low=map[i][j];
				id=bh[i][j];
				for (k=0;k<4;++k){
					nx=i+fx[k];
					ny=j+fy[k];
					if (nx<0 || ny<0 || nx>=h || ny>=w) continue;
					if (map[nx][ny]<low) {
						low=map[nx][ny];
						id=bh[nx][ny];
					}
				}
				merge(id,bh[i][j]);
			}
		printf("Case #%d:\n",++I);
		tmp=0;
		for (i=0;i<h;++i,printf("\n"))
		    for (j=0;j<w;++j){
				a=father(bh[i][j]);
				if (a==bh[i][j]) ch[a]=tmp+++'a';
				printf("%c ",ch[a]);
			}
	}
	return 0;
}

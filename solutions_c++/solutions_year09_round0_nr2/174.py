#include <iostream>
#define c(i,j) (((i)-1)*w+(j))
#define legal(i,j) ((i)>0 && (i)<=h && (j)>0 && (j)<=w)
using namespace std;

int map[102][102],test,low,i,j,k,l,d,h,w,fa[20002],hash[20002];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
char who[20002];

int find(int x){
	if (fa[x]==x)return x;
	fa[x]=find(fa[x]);
	return fa[x];
};

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>test;
	for (int t=1;t<=test;++t){
		cin>>h>>w;
		for (i=1;i<=h;++i)for (j=1;j<=w;++j)cin>>map[i][j];
		for (i=0;i<=h*w;++i)fa[i]=i;

		for (i=1;i<=h;++i)
			for (j=1;j<=w;++j){
				low=-1;
				for (d=0;d<4;++d)
					if (legal(i+dx[d],j+dy[d]))
						if (map[i][j]>map[i+dx[d]][j+dy[d]])
							if (low==-1 || map[i+dx[d]][j+dy[d]]<map[i+dx[low]][j+dy[low]])
								low=d;
				if (low>=0)fa[c(i,j)]=c(i+dx[low],j+dy[low]);
			};

		int cnt=0;
		for (i=1;i<=h*w;++i)fa[i]=find(i);
		memset(hash,0,sizeof hash);

		printf("Case #%d:\n",t);
		for (i=1;i<=h;++i){
			for (j=1;j<=w;++j,cout<<' '){
				int z=fa[c(i,j)];
				if (!hash[z])hash[z]=++cnt;
				cout<<(char)('a'+hash[z]-1);
			};
			cout<<endl;
		};
	};
};
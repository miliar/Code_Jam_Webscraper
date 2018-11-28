#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;

typedef long long ll;

struct UnionFind:vector<int>{
	UnionFind(int n){assign(n,-1);}
	int root(int x){return at(x)<0?x:at(x)=root(at(x));}
	void joint(int x,int y){
		x=root(x);y=root(y);
		if(x==y)return;
		if(-at(x)<-at(y))std::swap(x,y);
		at(x)+=at(y);at(y)=x;
	}
};

int t,h,w;
int hi[110][110];

inline int z(int x,int y){return x-1+(y-1)*w;}

main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;++i){
		cin>>h>>w;
		for(int y=1;y<=h;++y)
			for(int x=1;x<=w;++x)
				scanf("%d",&hi[x][y]);
		for(int j=0;j<102;++j)
			hi[0][j]=hi[j][0]=hi[w+1][j]=hi[j][h+1]=1001001001;
		UnionFind uf(w*h);
		for(int x=1;x<=w;++x)for(int y=1;y<=h;++y){
			int tx=-1,ty,thi=hi[x][y];
			if(hi[x][y-1]<thi)tx=x,ty=y-1,thi=hi[x][y-1];
			if(hi[x-1][y]<thi)tx=x-1,ty=y,thi=hi[x-1][y];
			if(hi[x+1][y]<thi)tx=x+1,ty=y,thi=hi[x+1][y];
			if(hi[x][y+1]<thi)tx=x,ty=y+1,thi=hi[x][y+1];
			if(tx!=-1){
				uf.joint(z(x,y),z(tx,ty));
			}
		}
		vector<vector<char> > ans(102,vector<char>(102,0));
		char cnt='a';
		for(int y=1;y<=h;++y)for(int x=1;x<=w;++x){
			int ux=uf.root(z(x,y))%w+1,uy=uf.root(z(x,y))/w+1;
			if(!ans[ux][uy])ans[ux][uy]=cnt++;
		}
		printf("Case #%d:\n",i);
		for(int y=1;y<=h;++y){
			for(int x=1;x<=w;++x){
				int ux=uf.root(z(x,y))%w+1,uy=uf.root(z(x,y))/w+1;
				printf((x==1)?"%c":" %c",ans[ux][uy]);
			}
			cout<<endl;
		}
	}
}

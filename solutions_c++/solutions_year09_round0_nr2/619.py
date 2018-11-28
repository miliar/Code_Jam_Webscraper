#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct UnionFind{
	std::vector<int>parent;
	std::vector<int>level;
	UnionFind(int size):parent(size),level(size){
		for(int i=0;i<size;++i)parent[i]=i;
	}
	void unit(int a,int b){
		int al = look(a);
		int bl = look(b);
		if(level[al] > level[bl]){
			parent[bl] = al;
		}else if(level[al] < level[bl]){
			parent[al] = bl;
		}else{
			parent[al] = bl;
			level[bl] += 1;
		}
	}
	int look(int x){
		if(parent[x] == x)return x;
		return parent[x] = look(parent[x]);
	}
};
int main(){
	int n;cin>>n;
	for(int i=1;i<=n;++i){
		int h,w;
		cin >> h >> w;
		vector<vector<unsigned> >map(h+2,vector<unsigned>(w+2,-1));
		UnionFind uf(h*w);
		for(int y=1;y<=h;++y)
			for(int x=1;x<=w;++x)
				cin >> map[y][x];
		for(int y=1;y<=h;++y)
			for(int x=1;x<=w;++x){				
				unsigned a[5]={map[y][x],map[y-1][x],map[y][x-1],map[y][x+1],map[y+1][x]};
				int i  = min_element(a,a+5)-a;
				int as[5][2]={{y,x},{y-1,x},{y,x-1},{y,x+1},{y+1,x}};
				uf.unit((y-1)*w+(x-1),(as[i][0]-1)*w+(as[i][1]-1));
			}
		vector<unsigned>labels(h*w,-1);
		int id = 0;
		cout << "Case #" << i << ":\n";
		for(int y=0;y<h;++y){
			for(int x=0;x<w;++x){
				int label = uf.look(y*w+x);
				if(labels[label] == -1)
					labels[label] = id++;
				cout << char('a'+labels[label]) << " ";
			}
			cout << endl;
		}
	}
}
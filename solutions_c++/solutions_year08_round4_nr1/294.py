#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>


using namespace std;


const int nmax = 20000;
const int inf  = 100000000;

struct node{
	int val;
	int change;
	int type;
};

node tree[nmax];
int f[nmax][2];

int op(int i,int j,int o){
	if (o == 0) 
		return i | j;
	return i & j;
}

int rec(int k,int v){

	if (f[k][v] > -1) 
		return f[k][v];

	if (tree[k].type == 1){
		if (tree[k].val == v) f[k][v] = 0;
		else f[k][v] = inf;
		return f[k][v];
	}

	int mi = inf;

	for (int i = 0;i <= 1; ++i)
		for (int j = 0;j <= 1; ++j)
			if (op(i,j,tree[k].val) == v)
				mi = min(mi,rec(2*k,i) + rec(2*k+1,j));

	if (tree[k].change){

		for (int i = 0;i <= 1; ++i)
		for (int j = 0;j <= 1; ++j)
			if (op(i,j,!(tree[k].val)) == v)
				mi = min(mi,rec(2*k,i) + rec(2*k+1,j)+1);
	}
	f[k][v] = mi;
	return mi;
}


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){
		int m,v;
		cin >> m >> v;
		memset(f,-1,sizeof(f));

		int k = 0;

		for (int i = 1;i <= (m-1) / 2; ++i){
			int g,c;

			cin >> g >> c;

			++k;
			tree[k].val = g;
			tree[k].change = c;
			tree[k].type = 0;			
		}

		for (int i = 1;i <= (m+1) / 2; ++i){
			++k;
			cin >> tree[k].val;
			tree[k].type = 1;			
		}
		int tt = rec(1,v);
		if (tt < inf)
			cout << "Case #"<<t<<": "<< tt <<endl;	
		else 
			cout << "Case #"<<t<<": "<< "IMPOSSIBLE" <<endl;	
	}

	return 0;
}
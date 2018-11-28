#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

struct node{
	int id, k;
	bool operator < (const node &tn)const {
		k < tn.k;
	}
}p[120];
int cmp(node n1, node n2){
	return n1.k < n2.k;
}

int mat[120][50], N, K;
bool judge(int k1, int k2, int K){
	for(int i = 1; i <= K; ++i)if(mat[k1][i] >= mat[k2][i])return 0;
	return 1;
}

int mat2[120][120];
int vis[120], vm1[120], vm2[120];

void dfs(int k){
	vis[k] = 1;
	for(int i = 0; i < N; ++i)if(!vis[i] && mat2[k][i]){
		dfs(i);break;
	}
}
int path(int x){
	for(int i = 0; i < N; ++i)
		if(mat2[x][i] && !vis[i]){
			vis[i] = 1;
			if(vm2[i] == -1 || path(vm2[i])){
				vm1[x] = i;
				vm2[i] = x;
				return 1;
			}
		}
	return 0;
}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int T, i, j, k;
	cin>>T;
	for(int t = 1; t <= T; ++t){
		cin>>N>>K;
		for(i = 0; i < N; ++i){
			for(j = 1; j <= K; ++j)
				cin>>mat[i][j];
			p[i].id = i;
			p[i].k = mat[i][1];
		}
		sort(p, p+N, cmp);/*cout<<"after sort"<<endl;
		for(i = 0; i < N; ++i)cout<<p[i].id<<' '<<p[i].k<<endl;
		cout<<endl;*/
		int sum = 0;
		memset(mat2, 0, sizeof(mat2));
		for(i = 0; i < N; ++i){
			for(j = i+1; j < N; ++j)if(judge(p[i].id, p[j].id, K)){
				mat2[i][j] = 1;
			}
		}
		memset(vm1, -1, sizeof(vm1));
		memset(vm2, -1, sizeof(vm2));
		int ans = 0;
		for(i = 0; i < N; ++i){
			memset(vis, 0, sizeof(vis));
			if(path(i))++ans;
		}
		cout<<"Case #"<<t<<": "<<N-ans<<endl;
	}
	return 0;
}

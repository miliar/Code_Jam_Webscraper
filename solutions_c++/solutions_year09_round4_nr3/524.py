#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int A[20][30],n,L[20];
vector<int> g[20];
int c[20],d[20];
bool cross(int i, int j, int k) {
	for (int p=1; p<k; p++)
		if (((long long)(A[i][p-1]-A[j][p-1]))*(A[i][p]-A[j][p])<=0)
			return true;
	return false;
}

bool use[20];
void color(int x) {
	memset(use,false, sizeof use);
	for (int i=0; i<g[x].size(); i++) 
		use[c[g[x][i]]] = true;
	for (int i=1; i<=n; i++)
		if (!use[i]) {
			c[x] = i; 
			return;
		}
}

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t; cin>>t;
	for (int o=0; o<t; o++) {
		int k; cin>>n>>k;
		for (int i=0; i<n; i++)
			for (int j=0; j<k; j++)
				cin>>A[i][j];
		for(int i=0; i<n; i++) {
			g[i].clear();
			L[i] = i;
		}
		for(int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (cross(i,j,k)) {
					g[i].push_back(j);
					g[j].push_back(i);
				}
		int res =1000;
		for (int e=0; e<100000; e++) { 
			random_shuffle(L,L+n);
			memset(c,0,sizeof c);
			int r = 0;
			for (int i=0; i<n; i++){
					color(L[i]);
					if (r<c[L[i]]) r = c[L[i]];
				}
			if (r<res) res = r;
		}
		cout<<"Case #"<<o+1<<": "<<res<<endl;
	}
	return 0;
}
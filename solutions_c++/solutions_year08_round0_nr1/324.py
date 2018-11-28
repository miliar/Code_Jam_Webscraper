#include <iostream>
#include <string>

using namespace std;


const int nmax = 102;
const int mmax = 1002;
const int inf = 1000000000;

int f[mmax][nmax];
string a[nmax],b[mmax];


int rec(int i,int j,int n,int m){	
	if (f[i][j] > -1) return f[i][j];
	if (i >= m) return 0;

	if (a[j] == b[i]){
		int mi = inf;
		for (int k = 0;k < n; ++k)
			if (k != j){
				int cur = rec(i+1,k,n,m)+1;
				if (cur < mi) mi = cur;
			}
		f[i][j] = mi;
	}
	else f[i][j] = rec(i+1,j,n,m);
	return f[i][j];
}

int solve(int n,int m){
	int mi = inf;
	memset(f,-1,sizeof(f));

	for (int i = 0;i < n; ++i)
		mi = min(mi,rec(0,i,n,m));
	return mi;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%i\n",&test);

	for (int t = 0;t < test; ++t){
		int n,m;
		scanf("%i\n",&n);
		for (int i = 0;i < n; ++i) getline(cin,a[i]);
		scanf("%i\n",&m);
		for (int i = 0;i < m; ++i) getline(cin,b[i]);
		printf("Case #%i: %i\n",t+1,solve(n,m));
	}


	return 0;
}
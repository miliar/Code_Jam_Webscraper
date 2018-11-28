#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;

const int nmax = 200;
const int mod = 10007;

int a[nmax][nmax],f[nmax][nmax];

bool belong(int x,int y,int n,int m){
	return (x >= 1 && y >= 1 && x <= n && y <= m);
}

int rec(int x,int y,int n,int m){
	if (a[x][y] == 1)
		return 0;

	if (f[x][y] > -1)
		return f[x][y];

	if (x == n && y == m)
		return 1;

	int ans=0;

	if (belong(x+2,y+1,n,m))
		ans = (ans + rec(x+2,y+1,n,m)) % mod;

	if (belong(x+1,y+2,n,m))
		ans = (ans + rec(x+1,y+2,n,m)) % mod;
	
	f[x][y] = ans;
	return ans;
	
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;
	for (int t = 1;t <= test; ++t){
		int n,m,r;
		memset(a,0,sizeof(a));
		memset(f,-1,sizeof(f));
		cin >> n >> m >> r;

		for (int i = 0;i < r; ++i){
			int x,y;
			cin >> x >> y;
			a[x][y] = 1;
		}

		cout << "Case #"<<t<<": "<< rec(1,1,n,m)<<endl;		
	}
	return 0;
}
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int MAXN = 107;
char mp[MAXN][MAXN];
bool flag[2];
int n;
void judge(int x,int y,const int &k) {
	//cout << "pos " << x << " " << y << " " << k<< endl;
	int id;
	if(mp[x][y] == 'R')	id = 0;
	else id = 1;
	int ct = 0;
	for(int i = y ; i<=n&&ct<k ; i ++ ) {
		if(mp[x][i]==mp[x][y]) ct++;
		else break;
	}
	if(ct == k) {
		//cout << "1\n";
		flag[id] = true;
		return;
	}
	ct = 0;
	for(int i = y ; i>=1&&ct<k ; i -- ) {
		if(mp[x][i]==mp[x][y]) ct++;
		else break;
	}
	if(ct == k) {
		//cout << "2\n";
		flag[id] = true;
		return;
	}
	ct = 0;
	for(int i = x  ;  i <= n && ct < k ; i ++  ) {
		if(mp[i][y] == mp[x][y]) ct++;
		else break;
	}
	if(ct == k) {
		//cout <<"3\n";
		flag[id] = true;
		return;
	}
	ct = 0;
	for(int i = x,j = y ; i<=n&&j<=n&&ct<k ; i ++,j++ ) {
		if(mp[i][j] == mp[x][y]) ct++;
		else break;
	}
	if(ct == k) {
		//cout <<"4\n";
		flag[id] = true;
		return;
	}

	ct = 0;
	for(int i = x,j = y ; i<=n&&j>=1&&ct<k ; i ++,j--) {
		if(mp[i][j] == mp[x][y]) ct++;
		else break;
	}
	if(ct == k) {
		//cout <<"5\n";
		flag[id] = true;
		return;
	}
	//cout << "6\n" << endl;
}



int main() {
	int k;
	int t;
//	freopen("A-large.in","r",stdin);
	//freopen("a.txt","w",stdout);
	scanf("%d",&t);
	int var = 0;
	while(t -- ) {
		scanf("%d%d",&n,&k);
		for(int i = 1 ; i <= n ; i ++ ) {
			scanf("%s",mp[i]+1);
		}
		for(int j = n-1 ; j >= 1 ; j -- ) {
			for(int i = 1 ; i <= n ; i ++ ) {
				if(mp[i][j] == '.') continue;
				int s = j,ss = j+1;
				while(ss <= n) {
					if(mp[i][ss] == '.') {
						mp[i][ss] = mp[i][s];
						mp[i][s] = '.';
						s ++;
						ss ++;
					} else break;
				}
			}
		}

		flag[0]=false,flag[1] = false;
		for(int i = 1 ; i <= n ; i ++ ) {
			for(int j = 1 ; j <= n ; j ++ ) {
				if(flag[0]&&flag[1]) break;
				if(mp[i][j] == '.') continue;
				judge(i,j,k);
			}
		}
		printf("Case #%d: ",++var);
		if(false==flag[1]&&flag[0]==false) {
			puts("Neither");
		} else if(flag[0] && flag[1]) {
			puts("Both");
		} else if(flag[0]) {
			puts("Red");
		} else puts("Blue");
	}
	return 0;
}

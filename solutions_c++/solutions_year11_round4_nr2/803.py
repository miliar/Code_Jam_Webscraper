#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <iomanip>
using namespace std;

typedef long long ll;

multiset<pair<int, int> > mp;

int grid[12][12], grid2[12][12];

int check(int n, int g[][12]){
	//check n x n grid
	// check diag
	g[0][0] = g[n - 1][0] = g[0][n - 1] = g[n-1][n-1] = 0;
	
	ll s1, s2;
	s1 = s2 = 0;
	int x, y, x1, x2, y1, y2;
	//cout<<"in check()n = "<<n<<endl;
	for(int i = 1; i <= n - 1; ++i){
		x = 0; y = i;
		while(x < n && y < n){
			s1 += g[x][y] * i;
			x++; y++;
		}
		x = i; y = 0;
		while(x < n && y < n){
			s2 += g[x][y] * i;
			x++; y++;
		}
	}
	if(s1 != s2)return 0;
	s1 = s2 = 0;
	for(int i = 1; i <= n - 1; ++i){
		x = n - 1 - i; y = 0;
		while(x >= 0 && y < n){
			s1 += g[x][y] * i;
			x--; y++;
		}
		x = n - 1; y = i;
		while(x >= 0 && y < n){
			s2 += g[x][y] * i;
			x--; y++;
		}
	}
	if(s1 != s2)return 0;
	s1 = s2 = 0;
	if(n % 2){ // n is odd
		int mid = n / 2;
		for(int i = 1; i <= n/2; ++i){
			x1 = mid - i; y = 0;
			x2 = mid + i;
			while(y < n){
				s1 += g[x1][y] * i;
				s2 += g[x2][y] * i;
				++y;
			}
		}
		if(s1 != s2)return 0;
		s1 = s2 = 0;
		for(int i = 1; i <= n / 2; ++i){
			x = 0; y1 = mid - i;
			y2 = mid + i;
			while(x < n){
				s1 += g[x][y1] * i;
				s2 += g[x][y2] * i;
				++x;
			}
		}
		if(s1 != s2)return 0;
	}else {
		s1 = s2 = 0;
		int mid = n / 2;
		for(int i = 1; i <= n / 2; ++i){
			x1 = mid - i; y = 0;
			x2 = mid + i - 1;
			while(y < n){
				s1 += g[x1][y] * (2 * i - 1);
				s2 += g[x2][y] * (2 * i - 1);
				++y;
			}
		}
		if(s1 != s2)return 0;
		s1 = s2 = 0;
		for(int i = 1; i <= n / 2; ++i){
			x = 0;	y1 = mid - i;
			y2 = mid + i - 1;
			while(x < n){
				s1 += g[x][y1] * (2 * i - 1);
				s2 += g[x][y2] * (2 * i - 1);
				++x;
			}
		}
		if(s1 != s2) return 0;
	}
//	cout<<"after check()n = "<<n<<endl;
	return 1;
}


int main()
{
	int T, r, c, d, k;
	cin>>T;
	string str;
	for(int tt = 1; tt <= T; ++tt){
		cin>>r>>c>>d;
		
		for(int i = 0; i < r; ++i){
			cin>>str;
			for(int j = 0; j < c; ++j){
				grid[i][j] = str[j] - '0' + d;
			}
		}
	//	cout<<"after tt = "<<tt<<endl;
		bool flag = false;
		int n = min(r, c);
		for(k = n; k >= 3 && !flag; --k){
			for(int i = 0; i + k <= r && !flag; ++i)
				for(int j = 0; j + k <= c && !flag; ++j){
					for(int ii = 0; ii < k; ++ii)
						for(int jj = 0; jj < k; ++jj){
							grid2[ii][jj] = grid[i + ii][j + jj];
						}
//					cout<<"in for"<<endl;
					if(check(k, grid2))flag = true;	
				}
		}
		cout<<"Case #"<<tt<<": ";
		if(flag)cout<<k + 1<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
//<<fixed<<setprecision(9)<<sumt<<endl;
	}
	return 0;
}


		

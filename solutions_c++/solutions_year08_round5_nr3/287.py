#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;

const int nmax = 12;

string a[nmax];
int f[1 << nmax][nmax];

bool can(int mask1,int mask2,int n,int m,int pos){
	for (int i = 0;i < m; ++i)
		if ((mask1 & (1 << i)) > 0)
			for (int j = 0;j < m; ++j)
				if ((mask2 & (1 << j)) > 0){
					if (abs(i-j) == 1) return false;					
				}

	int prev = -2;

	for (int j = 0;j < m; ++j)
		if ((mask2 & (1 << j)) > 0){
			if (a[pos][j] == 'x')
				return false;
			if ((prev > -1) && (j - prev) == 1)
				return false;
			prev = j;					
		}
	return true;	
}

int num(int mask,int m){
	int ans = 0;
	for (int j = 0;j < m; ++j)
		if ((mask & (1 << j)) > 0)
			++ans;
	return ans;
}

int rec(int mask,int pos,int n,int m){
	if (f[mask][pos] > -1)
		return f[mask][pos];

	if (pos >= n)
		return 0;

	int ma = 0;

	for (int i = 0;i < (1 << m); ++i)
		if (can(mask,i,n,m,pos)){
			int cur = num(i,m) + rec(i,pos+1,n,m);
			if (cur > ma) 
				ma = cur;
		}
	f[mask][pos] = ma;
	return ma;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%i\n",&test);

	for (int t = 1;t <= test; ++t){
		int n,m;
		memset(f,-1,sizeof(f));
		scanf("%i%i\n",&n,&m);

		for (int i = 0;i < n; ++i)
			getline(cin,a[i]);

		cout << "Case #"<<t<<": "<< rec(0,0,n,m)<<endl;			
	}
	return 0;
}
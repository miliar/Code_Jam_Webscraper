#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 1005;

int f[nmax][nmax][11],g[nmax][nmax];

int rec(int l,int r,int c)
{
	if (l * c >= r) return 0;
	if (f[l][r][c] > -1) return f[l][r][c];

	int ans = 1000000000;
	int sol;

	for (int i = l+1; i < r; ++i)
	{
		int cur = max(rec(l,i,c),rec(i,r,c))+1;
		if (cur < ans) 
		{
			sol = i;
			ans = cur;
		}
	}
	f[l][r][c] = ans;
	g[l][r] = sol;
	return ans;
}
void print(int l,int r,int c,string tt)
{
	cout << tt <<" " << l << " , " << r << endl;
	if (l * c >= r) return;
	int sol = g[l][r];
	print(l,sol,c,tt+"--");
	print(sol,r,c,tt+"--");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	memset(f,-1,sizeof(f));
	for (int test = 1;test <= nn; ++test){
		int l,r,c;

		cin >> l >> r >> c;

		
		
		printf("Case #%i: %i\n",test,rec(l,r,c));
		//print(l,r,c,"");
	}
	
	return 0;
}
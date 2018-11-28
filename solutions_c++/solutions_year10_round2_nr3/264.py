#include <iostream>
#include <set>
#include <string>
#include <cstring>
using namespace std;

typedef long long LL;

LL f[505][505];
int compose[505][505];

void Solve(int n,int index){
	if(f[n][index] != -1)return;
	if(index == 1)
	{
		f[n][index] = 1;
	}
	else
	{
		int i,ans;
		ans = 0;
		for(i = index-1; i >= 1; i--){
			Solve(index,i);
			ans += ((compose[n-index-1][index-i-1])*(f[index][i]))%100003;
			ans %= 100003;
		}

		f[n][index] = ans;
	}
}

int main(){
// 	FILE *fin = stdin;
// 	FILE *fout = stdout;
	FILE *fin = fopen("C-large.in","r");
	FILE *fout = fopen("RoundBC.out","w");
	for (int i = 0; i <= 502; ++i) compose[i][0] = compose[i][i] = 1;
	for (int i = 1; i <= 502; ++i) for (int j = 1; j < i; ++j) compose[i][j] = (compose[i-1][j] + compose[i-1][j-1])%100003;

	int t,tt,m,n,i,j;
	for(i = 0; i < 505; i++)
		for(j = 0; j < 505; j++)
			f[i][j] = -1;

	for(i = 2;i <= 505; i++)
	for(j = 1; j < i; j++)
		Solve(i,j);
/*	Init();*/

	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		int ans = 0;
		int i,j;

		fscanf(fin,"%d",&n);
		ans = 0;
		for(i = 1; i < n; i++)
			ans += f[n][i];

		fprintf(fout,"Case #%d: %d\n",tt,ans%100003);

	}

	return 0;
}
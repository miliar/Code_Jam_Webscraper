// A.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>

using namespace std;

char s[110][110];

double a[110], b[110], c[110];
int cnt[110];

void Solve()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i<n; ++i)
		scanf("%s", s[i]);
	for(int i = 0; i<n; ++i){
		a[i] = 0;
		cnt[i] = 0;
		for(int j = 0; j<n; ++j){
			if(s[i][j] != '.'){
				cnt[i]++;
				a[i] += s[i][j]-'0';
			}
		}
	}
	for(int i = 0; i<n; ++i){
		b[i] = 0;
		for(int j = 0; j<n; ++j){
			if(s[i][j] != '.'){
				b[i] += (a[j]-(s[j][i]-'0'))/(cnt[j]-1);
			}
		}
		b[i] /= cnt[i];
	}
	for(int i = 0; i<n; ++i){
		a[i] /= cnt[i];
		c[i] = 0;
		for(int j = 0; j<n; ++j){
			if(s[i][j] != '.'){
				c[i] += b[j];
			}
		}
		c[i] /= cnt[i];
	}
	for(int i = 0; i<n; ++i){
		printf("%.12f\n", a[i]*0.25+b[i]*0.5+c[i]*0.25);
	}
}

int main()
{
// 	freopen("A-small-attempt0.in", "r", stdin);
// 	freopen("A-small.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: \n", i);
		Solve();
	}
	fclose(stdout);
	return 0;
}


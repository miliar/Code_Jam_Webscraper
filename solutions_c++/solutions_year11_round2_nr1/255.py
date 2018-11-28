#include<iostream>
using namespace std;

const int maxn = 100 + 10;
char a[maxn][maxn];
int n, tot[maxn];
double wp[maxn], owp[maxn], oowp[maxn];

void solve()
{
	//cout << "here" << endl;
	scanf("%d\n", &n);
	int x, y;
	for (int i = 0; i < n; i++) {
		scanf("%s\n", a[i]);		
		y = 0;
		tot[i] = 0;
		for (int j = 0; j < n; j++) {
			if (a[i][j] != '.')
				tot[i]++;
			if (a[i][j] == '1')
				y++;
		}
		//cout << tot[i] << endl;
		wp[i] = (double)y / tot[i];		
		//cout << wp[i] << " ";
	}	
	//cout << endl;
	for (int i = 0; i < n; i++) {
		owp[i] = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] != '.') {			
				if (a[i][j] == '1')
					owp[i] += (wp[j] * tot[j]) / (tot[j] - 1);
				else owp[i] += (wp[j] * tot[j] - 1) / (tot[j] - 1);
				//if (i == 1) cout << owp[i] << "!" ;
			}
		owp[i] /= tot[i];
		//cout << owp[i] << " " ;
	}
	//cout << endl;
	for (int i = 0; i < n; i++) {
		oowp[i] = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] != '.')
				oowp[i] += owp[j];
		oowp[i] /= tot[i];
		//cout << oowp[i] << " " ;
	}
	//cout << endl;
	for (int i = 0; i < n; i++)
		printf("%.10lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
}

int main()
{
	int t, T;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		solve();
	}
}
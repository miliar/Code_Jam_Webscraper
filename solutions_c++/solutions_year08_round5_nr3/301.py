#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("C-small-attempt0.in");
ofstream fout("c.out");

const int maxm = 11;
int two[maxm], d[maxm];

bool check(int i)
{
	int k;
	for (k = 0;k < maxm - 1;k ++)
		if ((d[k] & i) == d[k])
			return false;
	
	return true;
}

int main()
{
	int num, c, m, n, tot, i,j,k, tmp, best;
	char s[maxm][maxm];
	int v[1025], o[1025], ans[maxm][1024], stat[maxm][1024], l[maxm], seat[maxm];
	cin >> c;
	tot = 0;
	for (i = 0;i < maxm;i ++)
		two[i] = (1 << i);
	for (i= 0;i < maxm - 1;i ++)
		d[i] = two[i] + two[i + 1];
	memset(o, 0, sizeof(o));
		
	for (i = 0;i <= 1023;i ++)
		if (check(i)) {
			v[tot] = i;
			for (k = 0;k <maxm;k ++)
				if ((two[k] & i) > 0) o[tot] ++;
			tot ++;			
		}
	v[tot] = 1024;
	for (num= 1;num <= c;num ++)
	{
		
		cin >> m >> n;
		memset(seat, 0, sizeof(seat));
		for (i = 0;i < m;i ++) {
			cin >> s[i];
			for (k = 0;k < n;k ++)
				if (s[i][k] == 'x')
					seat[i] += two[k];
		//	cout << seat[i] << endl;
		}
		memset(ans, 0, sizeof(ans));
		memset(stat, 0, sizeof(stat));
		memset(l, 0, sizeof(l));

		k = 1 << n;
		for (i = 0;v[i] < k;i ++)
			if ((v[i] & seat[0]) == 0) {				
				ans[0][l[0]] = o[i];
				stat[0][l[0]] = v[i];
				l[0] ++;
			}
		for (j = 1;j < m;j ++)
			for (i = 0;v[i] < k;i ++)
				if ((v[i] & seat[j]) == 0) {
					best = 0;
					for (tmp = 0;tmp < l[j - 1];tmp ++)
						if ((((stat[j - 1][tmp] * 2) & v[i]) == 0) && ((stat[j - 1][tmp] & (v[i] * 2)) == 0) )
						{
							if (best < o[i] + ans[j - 1][tmp]) {
								best = o[i] + ans[j - 1][tmp];
								stat[j][l[j]] = v[i];
								//ans[j][l[j]] = o[i] + ans[j - 1][tmp];
								
							}
						}
					if (best > 0) {
						ans[j][l[j]] = best;
	//					cout << j << " " << l[j] << " " << stat[j][l[j]] <<" " << ans[j][l[j]] << endl;
						l[j] ++;
						
					}			
					
				}
		best = 0;
		for (i = 0;i < l[m - 1];i ++)
			if (best < ans[m - 1][i])
				best = ans[m - 1][i];
		cout << "Case #" << num <<": " << best << endl;
	}
	return 0;
}


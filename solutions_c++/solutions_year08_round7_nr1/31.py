#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("A-large.in");
ofstream fout("a.out");

const int maxm = 10 + 5;
const int maxn = 1000 + 5;
const int maxl = 23;

char r[maxn][maxl];
char s[maxn][maxm][maxl];
int t[maxn], m[maxn], n;


void check(int k)
{
	int tmp[maxm], stmp, i, j , z = 0;
	//cout << k << " " << m[k] << endl;
	for (i = 0;i < m[k];i ++) {
		if (s[k][i][0] <= 'z' && s[k][i][0] >= 'a') {
			tmp[i] = 0;
		} else {
			for (j = 0;j < n;j ++)
				if (strcmp(s[k][i], r[j]) == 0) break;
			if (t[j] == 0) check(j);
			tmp[i] = t[j];
			z ++;
		}
		//cout << tmp[i] << " ";
	}
	//cout << k << ":";for (i = 0;i < m[k];i ++) cout << tmp[i] << " ";
	for (i = 0;i < m[k];i ++)
		for (j = i + 1;j < m[k];j ++)
			if (tmp[i] < tmp[j]) {
				stmp = tmp[i];
				tmp[i] = tmp[j];
				tmp[j] = stmp;
			}
	for (i = 0;i < m[k];i ++) {
	
		if (tmp[i] > 0) {
			if (tmp[i] + i> t[k])
				t[k] = tmp[i] + i;
		}
	}
	//if (t[k] == 0) t[k] = 1;
	if (t[k] < z + 1)
		t[k] = z + 1;

	//cout << k << " " << t[k] << endl;
}

int main()
{
	int c, k,i,j;
	cin >> c;
	for (k = 1;k <= c;k ++)
	{
		cin >> n;
		memset(t,0,sizeof(t));
		for (i = 0;i < n;i ++) {
			cin >> r[i];
			cin >> m[i];
			for (j = 0;j < m[i];j ++)
				cin >> s[i][j];
		}
		check(0);
		cout << "Case #" << k << ": " << t[0] << endl;
	}
	cout.close();
    return 0;
}

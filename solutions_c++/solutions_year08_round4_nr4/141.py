#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout

ifstream fin("D-small-attempt0.in");
ofstream fout("d.out");


const int maxn = 1005;
const int maxk = 5;
int best, k, p[maxk], used[maxk], len;
char s[maxn];

void check(int dep)
{
	int i, now, j;
	char tmp;
	if (dep == k) {
		now = 1;
		tmp = s[p[0]];
		for (i = 0;i < len ;i += k) {
			for (j = 0;j < k;j ++)
				if (s[i + p[j]] != tmp) {
					tmp = s[i + p[j]];
					now ++;
				}
		}
		if (now < best)
			 best = now;					
					
	} else {
	for (i = 0;i < k;i ++)
		if (used[i] == 0) {
			used[i] = 1;
			p[dep] = i;
			check(dep + 1);
			used[i] = 0;
		}
	}
}

int main()
{
	int num, n;
	

	cin >> n;
	for (num= 1;num <= n;num ++)
	{
		cin >> k;
		cin >> s;
		len = strlen(s);
		best = strlen(s) + 1;
		memset(used, 0, sizeof(used));
		check(0);
		cout << "Case #" << num << ": " << best << endl;
	}
	return 0;
}


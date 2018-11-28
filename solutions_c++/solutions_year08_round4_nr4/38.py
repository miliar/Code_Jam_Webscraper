#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
#define fil(a, b) memset(a,b,sizeof(a))

char s[100000];
int d[16][16][16];
int p[16];
int a[1<<16][16][16];
int lbin[1<<16];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	lbin[0]=0;
	for (int i = 1; i < (1<<16); i++)
		lbin[i] = lbin[i / 2] + (i&1);
	for (int ti = 1; ti <= t; ti++){
		int k;
		scanf("%d", &k);
		scanf("%s", s);
		int len=strlen(s);
		int res = len;
		for (int i = 0; i < k ; i++)
			for (int p1 = 0; p1 < k; p1++)
			for (int p2 = 0; p2 < k; p2++)
				if (p1 != p2){
					int &cur = d[i][p1][p2];
					cur =0;
					if (i < k -1){
						for (int j = 0; j < len; j+=k)
							if (s[j+p1] != s[j+p2])
								cur++;
					} else {
						for (int j = k; j < len; j+=k)
							if (s[j - k + p1] == s[j + p2])
								cur--;
					}
				}
		fil(a,127);
		for (int i = 0; i < k; i++)
			a[1<<i][i][i] = len / k;
		for (int i = 1; i < (1<<k); i++)
		for (int j = 0; j < k; j++)
		for (int q = 0; q < k; q++)
			if (a[i][j][q]<res){
				int z = lbin[i] - 1;
				for (int w = 0; w < k; w++)
				if (!((i>>w)&1))
					a[i | (1<<w)][j][w] = min(a[i | (1<<w)][j][w], a[i][j][q] + d[z][q][w]);
			}
		for (int i = 0; i < k; i++)
		for (int j = 0; j < k ;j++)
		if (a[(1<<k) -1][i][j] <= len)
			res = min(res, a[(1<<k) - 1][i][j]+d[k-1][j][i]);
		printf("Case #%d: %d\n", ti, res);
	}
	return 0;
}
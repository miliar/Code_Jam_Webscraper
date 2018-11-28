#include <stdio.h>
#include <string>
#define Mod 10000
using namespace std;
string a, d;
int c[19];
void process()
{
	int i, j;

	memset(c,0,sizeof(c));
	for (i = 0; i < d.size(); i++) {
		c[0] += d[i]==a[0];
		if (c[0] >= Mod) c[0] -= Mod;
		for (j = 1; j < a.size(); j++) {
			c[j] += c[j-1]*(d[i]==a[j]);
			if (c[j] >= Mod) c[j] -= Mod;
		}
	}
	printf("%04d\n", c[18]);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	char str[512];

	a = "welcome to code jam";
	scanf("%d\n",&T);
	for (t = 1; t <= T; t++) {
		gets(str);
		d = str;
		printf("Case #%d: ", t);
		process();
	}
	return 0;
}
#include <iostream>
#include <cstring>

using namespace std;

#define MOD 10000

int N;
char line[505];
char out[10], addz[10];
int num[505][19], c[19];
char goal[] = "welcome to code jam";

void input () {
	scanf ("%d", &N);
}

void solve () {
	int len, tot;
	gets (line);
	for (int i=1;i<=N;i++) {
		gets (line);
		len = strlen (line);
		memset (c, 0, sizeof(c));
		memset (num, 0, sizeof(num));
		for (int j=0;j<len;j++) {
			for (int k=0;k<19;k++)
				if (goal[k]==line[j]) {
					if (k==0)
						num[j][k] = 1, c[k]=(c[k]+1)%MOD;
					else
						num[j][k] = c[k-1], c[k]=(c[k]+c[k-1])%MOD;
				}
		}
		tot = 0;
		for (int j=0;j<len;j++)
			tot = (tot+num[j][18])%MOD;
		sprintf (out, "%d", tot);
		strcpy (addz, "");
		for (int j=4;j>strlen(out);j--)
			strcat (addz, "0");
		strcat (addz, out);
		printf ("Case #%d: %s\n", i, addz);
	}
}

void output () {

}

int main () {
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	input ();
	solve ();
	output ();
	return 0;
}

#include <stdio.h>
#include <string>

char s[500];
int l, n, q, C, i, j, k, t;
char a[5100][20];
int b[20][30];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.ans", "w", stdout);
    scanf("%d %d %d ", &l, &n, &q);
    for (i=0; i<n; i++) scanf("%s", a[i]);
    for (C=1; C<=q; C++)
    {
    	scanf("%s", s); t = 0;
    	memset(b, 0, sizeof(b));
    	for (i=0; i<l; i++)
    	{
         	if (s[t]=='(')
         	{
              	t ++;
              	while (s[t]!=')') { b[i][s[t]-'a'] = 1; t ++; }
         	} else b[i][s[t]-'a'] = 1;
         	t ++;
    	}
    	k = n;
    	for (i=0; i<n; i++) for (j=0; j<l; j++) if (b[j][a[i][j]-'a']==0) { k --; break; }
    	printf("Case #%d: %d\n", C, k);
    }
}


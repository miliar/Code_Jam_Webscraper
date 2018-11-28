#include <stdio.h>
#include <algorithm>

using namespace std;

int btn[110], rbt[110];
int t[2], p[2];

int main()
{
	int T, i, ans, n, cas=0;
	char str[10];
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			scanf("%s%d", str, &btn[i]);
			if (str[0]=='O') rbt[i]=0;
			else rbt[i]=1;
		}
		t[0]=t[1]=0;
		p[0]=p[1]=1;
		for (i=0; i<n; i++)
		{
		  t[rbt[i]]=1+max(t[rbt[i]]+abs(p[rbt[i]]-btn[i]),  t[1-rbt[i]]);
		  p[rbt[i]]=btn[i];
		}
		printf("Case #%d: %d\n", ++cas, max(t[0], t[1]));
	}
	return 0;
}
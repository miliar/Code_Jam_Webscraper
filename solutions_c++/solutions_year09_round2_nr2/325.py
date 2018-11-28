#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nt;
	char s[25];
	scanf("%d",&nt);
	for (int i=0;i<nt;i++)
	{
		memset(s,0,sizeof(s));
		scanf("%s",s);
		int l = strlen(s);
		int ind = next_permutation(s,s+l);
		if (!ind)
		{
			swap(s[0],s[l-1]);
			for (int j=1;j<l;j++)
				if (s[j]!='0' && s[j]<s[0])
					swap(s[0],s[j]);
			sort(s+1,s+l);
			printf("Case #%d: %c0%s\n",i+1,s[0],s+1);
		}
		else
			printf("Case #%d: %s\n",i+1,s);
	}
	return 0;
}

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char ch[2000];

int main()
{
	int text, i, cs = 0;
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	scanf("%d", &text);
	getchar();
	while(text--)
	{
		memset(ch, '\0', sizeof(ch));
		scanf("%s", ch);
		int len = strlen(ch);
		if(next_permutation(ch, ch+len) == false)
		{
			int j, k;
			char max = '9';
			for(j = 0; j < len; j++)
				if(ch[j] != '0' && ch[j] < max)
				{
					max = ch[j];
					k = j;
				}
			char tmp = ch[k];
			ch[k] = ch[0];
			ch[0] = tmp;
			sort(ch+1, ch+len);
			for(j = len-1; j >= 1; j--)
				ch[j+1] = ch[j];
			ch[1] = '0';
		}
		printf("Case #%d: %s\n", ++cs, ch);
	}
	return 0;
}
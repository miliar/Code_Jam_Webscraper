#include <stdio.h>
#include <string.h>

char a[3][200] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char b[3][200] = {"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};

char m[30];

int main()
{
	freopen ("/home/nirvanan/code jam/C-small-attempt1.in", "r", stdin);
	freopen ("/home/nirvanan/code jam/out.txt", "w", stdout);
	
	int a, b;
	
	int t, tt = 1;
	
	scanf("%d", &t);
	
	while (t--) {
		scanf("%d%d", &a, &b);
		
		int sum = 0;
		for (int i = a; i < b; i++)
			for (int j = i + 1; j <= b; j++) {
				char l[10];
				
				sprintf(l, "%d", i);
				int len = strlen(l);
				
				for (int k = 0; k < len; k++) {
					char c = l[0];
					
					for (int q = 0; q < len - 1; q++)
						l[q] = l[q + 1];
					l[len - 1] = c;
					
					int temp;
					
					sscanf(l, "%d", &temp);
					if (temp == j) {
						sum++;
						break;
					}
				}
			}
		printf("Case #%d: %d\n", tt++, sum);
	}
	return 0;
}

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
	int C;
	scanf("%d", &C);
	
	for (int ca=0; ca<C; ca++)
	{
		int k;
		scanf("%d", &k);

		char s[60000];
		scanf("%s", &s);
		
		int len = strlen(s);
		int ss = len / k;
		
		int p[16];
		
		for (int i=0; i<k; i++)
			p[i] = i;
		
		int ans = 100000;
		while (1)
		{
			char t[60000];
			for (int seg=0; seg<ss; seg++)
				for (int i=0; i<k; i++)
					t[seg*k+i] = s[seg*k+p[i]];
					
			int cnt = 1;
			for (int i=1; i<len; i++)
				if (t[i] != t[i-1])
					cnt++;
			if (cnt < ans)
				ans = cnt;				
			if (!next_permutation(p, p+k))
				break;
		}
	
		printf("Case #%d: %d\n", ca+1, ans);
	}
}

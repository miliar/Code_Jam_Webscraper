#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int solve()
{
	int N, S, p;
	
	int conf = 0, pos = 0;
	
	scanf("%d %d %d", &N, &S, &p);
	
	for (int t = 0; t < N; t++) {
		int ti = 0;
		scanf("%d", &ti);
		
		bool t_normal = false;
		bool t_surp = false;
		
		for (int i = 0; i <= 10; i++)
			for (int j = 0; j <= 10; j++)
				for (int k = 0; k <= 10; k++)
					if (i + j + k == ti && (i >= p || j >= p || k >= p)) {
						int mdiff = max(max(abs(i - j), abs(i - k)), abs(j - k));
						if (mdiff == 2)
							t_surp = true;
						else if (mdiff < 2)
							t_normal = true;
					}
		
		if (t_normal)
			conf++;
		else if (t_surp)
			pos++;
	}
	
	return conf + min(pos, S);
}

int main()
{
	int T = 0;
	scanf("%d", &T);
	
	for (int i = 0; i < T; i++) {
		printf("Case #%d: %d\n", i + 1, solve());
	}
}
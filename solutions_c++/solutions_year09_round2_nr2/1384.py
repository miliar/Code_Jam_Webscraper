#include <cstdio>
#include <cstring>

using namespace std;

int cc[2][10], N, cas;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w",stdout);

	scanf("%d", &cas);
	for(int c = 1; c <= cas; c ++) {
		scanf("%d", &N);
		
		for(int i = 1; i <= 9; i ++)
			cc[0][i] = 0;
		for(int s = N; s; s /= 10)
			cc[0][s % 10] ++;
		for(int i = N + 1; ; i ++) {
			for(int j = 1; j <= 9; j ++)
				cc[1][j] = 0;
			for(int s = i; s; s /= 10)
				cc[1][s % 10] ++;
			for(int j = 1; j <= 9; j ++)
				if(cc[0][j] != cc[1][j])
					goto NEXT;
			printf("Case #%d: %d\n", c, i);
			break;
NEXT:;
		}
	}

	return 0;
}
#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

#define myabs(x) (x > 0 ? x : (-(x)))
int main()
{
	int T;
	scanf("%d", &T);
	int N, preO, preB, posO, posB, ans, pos, tim;
	char str[5];
	for (int ncas = 1; ncas <= T; ncas++) {
		preO = preB = 0;	posO = posB = 1;
		scanf("%d", &N);
		tim = 0;
		for (int i = 0; i < N; i++) {
			scanf("%s%d", str, &pos);
			if (strcmp(str, "O") == 0) {
				int canmove = tim - preO;
				int move = myabs(pos - posO);
				if (canmove < move) {
					tim += move - canmove;
				}
				tim += 1;
				preO = tim;	posO = pos;
			} else {
				int canmove = tim - preB;
				int move = myabs(pos - posB);
				if (canmove < move) {
					tim += move - canmove;
				}
				tim += 1;
				preB = tim;	posB = pos;
			}
		}
		printf("Case #%d: %d\n", ncas, tim);
   	}
	return 0;
}

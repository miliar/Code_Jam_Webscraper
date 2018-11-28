#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char linha[512];
int tam;

int bt (int num, char c, int pos)
{
	//printf ("%d - %c - %d\n", num, c, pos);
	if (num == 19 && linha[pos] == c) return 1;
	// printf ("%d - %c - %c - %d\n", num, c, linha[pos], pos);
	if (c != linha[pos]) return 0;

	int ans = 0;
	
	for (int i = pos + 1; i <= tam; i++)
	{
		if (num == 1) ans += bt(2, 'e', i);
		else if (num == 2) ans += bt(3, 'l', i);
		else if (num == 3) ans += bt(4, 'c', i);
		else if (num == 4) ans += bt(5, 'o', i);
		else if (num == 5) ans += bt(6, 'm', i);
		else if (num == 6) ans += bt(7, 'e', i);
		else if (num == 7) ans += bt(8, ' ', i);
		else if (num == 8) ans += bt(9, 't', i);
		else if (num == 9) ans += bt(10, 'o', i);
		else if (num == 10) ans += bt(11, ' ', i);
		else if (num == 11) ans += bt(12, 'c', i);
		else if (num == 12) ans += bt(13, 'o', i);
		else if (num == 13) ans += bt(14, 'd', i);
		else if (num == 14) ans += bt(15, 'e', i);
		else if (num == 15) ans += bt(16, ' ', i);
		else if (num == 16) ans += bt(17, 'j', i);
		else if (num == 17) ans += bt(18, 'a', i);
		else if (num == 18) ans += bt(19, 'm', i);
		//else if (num == 19)	ans += bt(20, '$', i);

		ans %= 10000;
	}

	return ans;
}

int main (void)
{
	int ans, lines;

	scanf ("%d ", &lines);

	for (int caso = 1; caso <= lines; caso++)
	{
		gets (linha);
		ans = 0;

		tam = strlen(linha);
		for (int i = 0; i < tam; i++)
		{
			ans += bt(1, 'w', i);
			ans %= 10000;
		}

		printf ("Case #%d: %04d\n", caso, ans);
	}

	return 0;
}

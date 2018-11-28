#include <iostream>
#include <algorithm>
using namespace std;

char text[510];
char wcj[] = "welcome to code jam";
int WL = strlen(wcj), TLEN;

int getCount(int i, int j)
{
	if(j >= WL) return 1;

	int count = 0;
	for(; i < TLEN - WL + j; ++i) {
		if(text[i] == wcj[j]){
			count += getCount(i+1, j+1);
		}
	}

	return (count < 10000) ? count : count%10000;
}

int main()
{
	freopen("C-small-attempt0.in.txt", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);

	int N, X, amount;

	fgets(text, 505, stdin);
	sscanf(text, "%d", &N);

	X = 0;
	while (N--)
	{
		fgets(text, 505, stdin);
		TLEN = strlen(text);
		amount = getCount(0, 0);

		printf("Case #%d: %04d\n", ++X, amount);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
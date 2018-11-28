#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void go(char *s)
{
	int n = strlen(s);
	n--;
	int x = n-1;
	while( s[x] >= s[x+1] )
		x--;

	int li = x+1;
	int y = x+1;
	while( y <= n )
	{
		if( s[y] > s[x] && s[y] < s[li] )
			li = y;
		y++;
	}

	swap( s[x], s[li] );

	sort( &s[x+1], &s[n+1] );
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		char auxS[100];
		auxS[0] = '0';
		scanf("%s", &auxS[1]);

		go(auxS);

		printf("Case #%d: ", k);
		if( auxS[0] != '0' )
			printf("%s\n", auxS);
		else
			printf("%s\n", &auxS[1]);
	}
}
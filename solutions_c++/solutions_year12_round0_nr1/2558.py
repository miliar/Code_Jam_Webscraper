#include<iostream>
#include<cstdio>
#include<cstring>
#define MAX 110
using namespace std;

int main()
{
	char map[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
	int t;
	scanf("%d", &t );
	for( int i = 1; i <= t; i++ )
	{
		getchar();
		char str[MAX];
		scanf("%[^\n]", str );
		printf("Case #%d: ", i );
		for( int j = 0; str[j]; j++ )
		printf("%c", (str[j] >= 'a' && str[j] <= 'z') ? map[ str[j] - 'a' ]: str[j] );
		printf("\n");
	}
	return 0;
}

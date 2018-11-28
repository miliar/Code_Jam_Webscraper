#include <stdio.h>
#include <memory.h>
#include <vector>
using namespace std;

char word[20][5005];
bool tag[20][30];
int len, d;

bool isLet( char c )
{
	if( c<='z' && c>='a' ) return true;
	return false;
}

void read( int i )
{
	char c;
	while( true )
	{
		c = getchar();
		if( c == '(' || isLet(c) ) break;
	}
	if( c != '(' )
	{
		tag[i][ c-'a' ] = true;
		return;
	}
	while( true )
	{
		c = getchar();
		if( c == ')' ) break;
		tag[i][ c-'a' ] = true;
	}
}

int match()
{
	int i, j, sum = 0;
	for(i=0; i<d; ++i)
	{
		for(j=0; j<len; ++j)
		{
			if( !tag[j][ word[i][j]-'a' ] ) break;
		}
		if( j == len ) sum++;
	}
	return sum;
}

int main()
{
	int n, i, j;
	freopen("D:\\Download\A-small-attempt0.in", "r", stdin);
	freopen("D:\\Download\out.txt", "w", stdout);
	scanf("%d %d %d", &len, &d, &n);
	for(i=0; i<d; ++i) scanf("%s", word[i]);
	for(i=0; i<n; ++i)
	{
		memset(tag, 0, sizeof(tag));
		for(j=0; j<len; ++j) read(j);
		printf("Case #%d: %d\n", i+1, match());
	}
	return 0;
}
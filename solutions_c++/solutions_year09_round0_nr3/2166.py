#include <iostream>

#define MAX_C 600

using namespace std;

const int final=19;
int m[final][MAX_C];
char nextc[] = "welcome to code jam";
char inp[MAX_C+1];

void initm()
{
	for(int i=0; i<final; ++i)
		for(int j=0; j<MAX_C; ++j)
			m[i][j] = -1;
}

void inline add(int &n)
{
	if(n==9999)
		n = 0;
	else
		++n;
}

void inline add(int &n, const int &toadd)
{
	n = (n+toadd)%10000;
}

int state_find(int i, int state)
{
	if(m[state][i] != -1)
		return m[state][i];

	int savepos = i, n=0;
	while(inp[i] != '\0')
	{
		while(inp[i]!='\0' && inp[i]!=nextc[state])
			++i;
		if(inp[i] != '\0')
		{
			if(state+1 < final)
				add(n, state_find(i, state+1));
			else
				add(n);
			++i;
		}
	}
	return m[state][savepos] = n;
}

int main( void )
{
	int N;
	scanf("%d", &N);
	gets(inp);
	for(int i=1; i<=N; ++i)
	{
		initm();
		int c = 0;
		gets(inp);
		int a = state_find(0, 0);
		printf("Case #%d: %04d\n", i, a);
	}
	return 0;
}

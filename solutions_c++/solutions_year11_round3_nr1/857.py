#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
using namespace std;

const int MAX_N = 64;

int r, c;
char s[MAX_N][MAX_N];

void input()
{
	scanf("%d%d", &r, &c);

	for(int i=1; i<=r; i++)
		scanf("%s", s[i]+1);
}

bool solve()
{
	for(int i=1; i<=r; i++)
		for(int j=1; j<=c; j++)
			if(s[i][j]=='#') {
				if(s[i+1][j]!='#' || s[i][j+1]!='#' || s[i+1][j+1]!='#')
					return 0;

				s[i][j] = '/';
				s[i][j+1] = '\\';
				s[i+1][j] = '\\';					
				s[i+1][j+1] = '/';
			}
			
	return 1;
}

void output(int t, bool b)
{
	printf("Case #%d:\n", t);
	
	if(!b) printf("Impossible\n");
	else {
		for(int i=1; i<=r; i++)
			printf("%s\n", s[i]+1);
	}
}

int main()
{
	int i, t;
	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		input();
		output(i, solve());
	}
	
	return 0;
}

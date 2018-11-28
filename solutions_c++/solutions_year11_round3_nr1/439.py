#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int nCase=1, T, R, C ;
bool succ = true;
char m[52][52];

void input() {
	succ = true;
	memset(m, 0, sizeof(m) );
    scanf("%d%d", &R, &C);
    for(int i=0;i<R;++i) {
		scanf("%s", &m[i]);
	}
}

void calc() {
	for(int i=0;i<R;++i) {
		for(int j=0;j<C;++j) {
			if( m[i][j] == '#' ) {
				if( m[i+1][j]=='#' && m[i][j+1]=='#' && m[i+1][j+1]=='#' ) {
					m[i][j] = m[i+1][j+1] = '/';
					m[i+1][j] = m[i][j+1] = '\\';
				} else {
					succ = false;
					return;
				}
			}
		}
	}
}

void output() {
	if( !succ ) {
		printf("Impossible\n");
	} else {
		for(int i=0;i<R;++i) {
			printf("%s\n", m[i]);
		}
	}
}

int main()
{
	scanf("%d", &T);
	while(T-->0) {
		
		input();
		calc();
		printf( "Case #%d:\n", nCase++);
		output();
	}
	return 0;
}

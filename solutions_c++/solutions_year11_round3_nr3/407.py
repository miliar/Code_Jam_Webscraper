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

int nCase=1, T;
int N, L, H;
int p[100];

void input() {
	scanf("%d%d%d", &N, &L, &H);
	for(int i=0;i<N;++i) {
		scanf("%d", &p[i]);
	}
}

int calc() {
	for(int i=L;i<=H;++i) {
        bool succ = true;
		for(int j=0;j<N;++j) {
			if( i%p[j]==0 || p[j]%i==0 ) {}
			else {
				succ = false;
				break;
			}
		}
		if(succ) return i;
	}
	return -1;
}


int main()
{
	scanf("%d", &T);
	while(T-->0) {
	    input();
		printf( "Case #%d: ", nCase++);
		int res = calc();
		if ( res==-1 ) printf("NO\n");
		else printf("%d\n", res);
	}
	return 0;
}

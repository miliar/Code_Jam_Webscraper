#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int N;
char ins[1000];
int d[20][505];
const char welcome[20] = "welcome to code jam";

int getd(int a, int b)
{
	if( d[a][b] != -1 ) {
		return d[a][b];
	}
	else {
		int re = 0;
		for( int i=0; i<b; i++ ) {
			if( ins[i]==welcome[a-1] ) {
				re = (re + getd(a-1,i))%1000;
			}
		}
		d[a][b] = re;
		return d[a][b];
	}
}

void process()
{
	int l = strlen(ins);
	for(int i=0; i<19; i++) {
		for(int j=0; j<l; j++ ) {
			d[i][j] = -1;
		}
	}

	for( int i=0; i<l; i++ ) {
		if( ins[i]=='w' ) {
			d[0][i] = 1;
		}
		else {
			d[0][i] = 0;
		}
	}

	int ans=0;
	for( int i=0; i<l; i++ ) {
		if( ins[i] == 'm' ) {
			ans += getd(18, i);
		}
	}

	printf("%04d\n", ans);
}

int main()
{
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("C.out", "wt", stdout);

	cin>>N;
	cin.getline(ins, 1000);
	for( int i=0; i<N; i++ ) {
		cin.getline(ins, 1000);
		printf("Case #%d: ", i+1);
		process();
	}

	return 0;
}
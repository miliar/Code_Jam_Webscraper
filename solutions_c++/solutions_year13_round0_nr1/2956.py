// A 
#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

int main() {
	int t,i,j,z=1;
	freopen("output.txt","w",stdout);
	FILE *fo = fopen("A-large.in","rt");
	char a[5][5];
	fscanf(fo,"%d",&t);
	while(t--) {
		int X=0,o=0;
		int x_cnt,o_cnt,jam_cnt=0;
		for ( i=0; i<4; i++ )
			fscanf(fo,"%s",a[i]);

		
		for ( i=0; i<4; i++ ) {
			x_cnt=0; o_cnt=0;
			for ( j=0; j<4; j++ ) {
				if ( a[i][j]=='X' ) x_cnt++;
				else if ( a[i][j]=='T' ) {x_cnt++; o_cnt++;}
				else if ( a[i][j]=='O' ) o_cnt++;
				else jam_cnt++;
			}
			if ( o_cnt==4 ) o=1;
			else if ( x_cnt==4 ) X=1;
		}

		for ( i=0; i<4; i++ ) {
			x_cnt=0; o_cnt=0;
			for ( j=0; j<4; j++ ) {
				if ( a[j][i]=='X' ) x_cnt++;
				else if ( a[j][i]=='T' ) {x_cnt++; o_cnt++;}
				else if ( a[j][i]=='O' ) o_cnt++;
			}
			if ( o_cnt==4 ) o=1;
			else if ( x_cnt==4 ) X=1;
		}

		x_cnt=0; o_cnt=0;
		for ( i=0; i<4; i++ ) {
			if ( a[i][i]=='X' ) x_cnt++;
			else if ( a[i][i]=='T' ) {x_cnt++; o_cnt++;}
			else if ( a[i][i]=='O' ) o_cnt++;
		}
		if ( o_cnt==4 ) o=1;
		else if ( x_cnt==4 ) X=1;

		x_cnt=0; o_cnt=0;
		for ( i=0; i<4; i++ ) {
			if ( a[i][3-i]=='X' ) x_cnt++;
			else if ( a[i][3-i]=='T' ) {x_cnt++; o_cnt++;}
			else if ( a[i][3-i]=='O' ) o_cnt++;
		}
		if ( o_cnt==4 ) o=1;
		else if ( x_cnt==4 ) X=1;


		printf("Case #%d: ",z++);
		if ( jam_cnt==0 && X==0 && o==0 ) printf("Draw\n");
		else if ( X==1 ) printf("X won\n");
		else if ( o==1 ) printf("O won\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
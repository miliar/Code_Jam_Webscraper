#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <string.h>

using namespace std;

int T,r,c;
bool res;
char m[55][55];

int main () {
	freopen ("input","r",stdin);
	freopen ("output","w",stdout);
	scanf ("%d",&T);
	for (int z=0; z<T; z++) {
		scanf ("%d%d",&r,&c);
		for (int i=0; i<r; i++) scanf ("%s",m[i]);
		for (int i=0; i<r; i++) {
			for (int j=0; j<c; j++) {
				if (m[i][j]=='#') {
					if (m[i][j+1]=='#' && m[i+1][j]=='#' && m[i+1][j+1]=='#') {
						m[i][j]='/';
						m[i][j+1]='\\';
						m[i+1][j]='\\';
						m[i+1][j+1]='/';
					} else {
						res=true;
						break;
					}
				}
			}
			if (res) break;
		}
		printf ("Case #%d:\n",z+1);
		if (res) printf ("Impossible\n"); else {
			for (int i=0; i<r; i++) {
				printf ("%s\n",m[i]);
			}
		}
		res=false;
	}
	return 0;
}
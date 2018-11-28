// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <vector>
using namespace std;

long long v[100][100];

static int dx[] = {2,1};
static int dy[] = {1,2};
char *doD(char **&toks)
{
	bool b[100][100] = {0};
	memset(v, 0, sizeof(v));
	int H = atoi(*toks++);
	int W = atoi(*toks++);
	int R = atoi(*toks++);
	for (int i=0; i<R; i++) {
		int y = atoi(*toks++)-1;
		int x = atoi(*toks++)-1;
		b[x][y] = true;
	}
	v[W-1][H-1] = 1;
	for (int i=W-2; i>=0; i--) {
		for (int j=H-2; j>=0; j--) {
			if (b[i][j])
				continue;
			long long mv = 0;
			for (int k=0; k<2; k++) {
				int x2=i + dx[k];
				int y2=j+dy[k];
				if (x2>=W || y2>=H)
					continue;
				mv = (mv + v[x2][y2]) % 10007;
			}
			v[i][j] = mv;
		}
	}
//	for (int i=0; i<H; i++) {
//		for (int j=0; j<W; j++) {
//			printf("%4d ", v[j][i]);
//		}
//		printf("\n");
//	}
	static char buf[1024];
	sprintf(buf, "%d", v[0][0]);
	return buf;
}
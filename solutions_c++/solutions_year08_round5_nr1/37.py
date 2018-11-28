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

static int dx[] = {0, 1, 0, -1};
static int dy[] = {-1, 0, 1, 0};
static bool ve[7000][7000] = {0};
static bool he[7000][7000] = {0};
static bool counted[7000][7000] = {0};
char *doA(char **&toks)
{
	memset(ve, 0, sizeof(ve));
	memset(he, 0, sizeof(he));
	memset(counted, 0, sizeof(counted));
	int L = atoi(*toks++);
	int x=3500, y=3500;
	int d=0;
	int x0=x, y0=y, x1=x, y1=y;
	for (int i=0; i<L; i++) {
		char *path = *toks++;
		int T = atoi(*toks++);
		for (int i=0; i<T; i++) {
			for (char *s=path; *s; s++)
			{
				if (*s == 'F') {
					if (dy[d]==-1) {
						assert(!ve[x][y-1]);
                        ve[x][y-1] = 1;
					} else if (dy[d]==1) {
						assert(!ve[x][y]);
						ve[x][y] = 1;
					} else if (dx[d]==-1) {
						assert(!he[x-1][y]);
						he[x-1][y] = 1;
					} else if (dx[d]==1) {
						assert(!he[x][y]);
						he[x][y] = 1;
					}
					x+=dx[d];
					y+=dy[d];
					x0 = min(x, x0);
					y0 = min(y, y0);
					x1 = max(x, x1);
					y1 = max(y, y1);
				} else if (*s == 'R') {
					d = (d+1)%4;
				} else if (*s=='L') {
					d = (d+3)%4;
				} else {
					assert(0);
				}
			}
		}
	}
#if 0
	for (int j=y0; j<=y1; j++) {
		for (int i=x0; i<=x1; i++) {
			printf(" %d", he[i][j]);
		}
		printf("\n");
		for (int i=x0; i<=x1; i++) {
			printf("%d ", ve[i][j]);
		}
		printf("\n");
	}
#endif
	static char buf[1024];
	int ret=0;
	for (int i=y0-1; i<=y1+1; i++) {
		bool b2=false;
		bool b=false;
		int c=0;
		int r0;
		for (int j=x0-1; j<=x1+1; j++) {
			if (ve[j][i]) {
				if (!b) {
					b = true;
					if (c) {
						ret+=c;
						for (int k=r0; k<j; k++) {
							counted[k][i] = 1;
						}
					}
				} else {
					b = false;
					c = 0;
					r0 = j;
					b2=true;
				}
			}
			if (b2)
			{
				if (!counted[j][i]) {
					c++;
				}
			}
		}
	}
	for (int i=x0-1; i<=x1+1; i++) {
		bool b2=false;
		bool b=false;
		int c=0;
		for (int j=y0-1; j<=y1+1; j++) {
			if (he[i][j]) {
				if (!b) {
					b = true;
					if (c)
						ret+=c;
				} else {
					b = false;
					c = 0;
					b2=true;
				}
			}
			if (b2)
			{
				if (!counted[i][j]) {
					counted[i][j]=1;
					c++;
				}
			}
		}
	}
	sprintf(buf, "%d", ret);
	return buf;
}
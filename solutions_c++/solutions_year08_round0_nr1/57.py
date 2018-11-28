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


char *doA(char **&toks)
{
	int Qs[1001] = {0};
	int S, Q;
	int dp[1001][101] = {0};

	S = atoi(*toks++);
	char **se = toks;
	toks += S;
	Q = atoi(*toks++);
	for (int i=0; i<Q; i++) {
		bool b=false;
		for (int j=0; j<S; j++) {
			if (stricmp(se[j], toks[i])==0) {
				Qs[i] = j;
				b = true;
				break;
			}
		}
		assert(b);
	}
	toks += Q;
	for (int i=Q-1; i>=0; i--) {
		for (int j=0; j<S; j++) {
			if (Qs[i] == j) {
				int m = -1;
				for (int k=0; k<S; k++) if (k!=j) {
					if (m==-1 || dp[i+1][k] < m)
						m = dp[i+1][k];
				}
				dp[i][j] = m + 1;
			} else {
				dp[i][j] = dp[i+1][j];
			}
		}
	}
	int m=-1;
	for (int i=0; i<S; i++) {
		if (m==-1 || dp[0][i]<m)
			m = dp[0][i];
	}
	static char buf[1024];
	sprintf(buf, "%d", m);

	return buf;
}


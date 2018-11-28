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

typedef struct Event
{
	int time;
	char *t;
	int dA, dB;
} Event;

int __cdecl cmpStr(const void *a, const void *b)
{
	Event *ea = (*(Event**)a);
	Event *eb = (*(Event**)b);
	int r = ea->time - eb->time;
	if (r!=0)
		return r;
	if (ea->dA > 0 || ea->dB > 0)
		return -1;
	if (eb->dA > 0 || eb->dB > 0)
		return 1;
	return 0;
}



char *doB(char **&toks)
{
	int T = atoi(*toks++);
	int NA = atoi(*toks++);
	int NB = atoi(*toks++);
	char **ta = toks;
	toks += NA*2;
	char **tb = toks;
	toks += NB*2;
	Event **events=NULL;
	for (int i=0; i<NA*2; i++) {
		Event *e = callocStruct(Event);
		int h, m;
		sscanf(ta[i], "%d:%d", &h, &m);
		e->time = m + h*60 + ((i%2)?T:0);
		e->t = ta[i];
		e->dA = (i%2)?0:-1;
		e->dB = (i%2)?1:0;
		arrayPush(&events, e);
	}
	for (int i=0; i<NB*2; i++) {
		Event *e = callocStruct(Event);
		int h, m;
		sscanf(tb[i], "%d:%d", &h, &m);
		e->time = m + h*60 + ((i%2)?T:0);
		e->t = tb[i];
		e->dA = (i%2)?1:0;
		e->dB = (i%2)?0:-1;
		arrayPush(&events, e);
	}

	qsort(events, arrayGetSize(&events), 4, cmpStr);
	int iA=0, cA=0;
	int iB=0, cB=0;
	for (int i=0; i<arrayGetSize(&events); i++) {
		Event *e = events[i];
		if (cA + e->dA < 0) {
			iA++;
			cA++;
		}
		if (cB + e->dB < 0) {
			iB++;
			cB++;
		}
		cA+=e->dA;
		cB+=e->dB;
	}

	static char buf[1024];
	sprintf(buf, "%d %d", iA, iB);
	return buf;
}

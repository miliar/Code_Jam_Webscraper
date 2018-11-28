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

/*
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

*/

#define float double

float R;
float t;
float r;
float g;
float s;

bool isInCircle(float x, float y)
{
	return x*x+y*y <= 1;
}

bool hits(float x, float y)
{
	float m = fmod(x, s);
	if (m<r || m>g+r)
		return true;
	m = fmod(y, s);
	if (m<r || m>g+r)
		return true;
	return false;
}

float dist(float x1, float y1, float x2, float y2)
{
	float dx = x2 - x1;
	float dy = y2 - y1;
	return sqrt(dx*dx + dy*dy);
}

float area(float x1, float y1, float x2, float y2, float x3, float y3)
{
	float a = dist(x1, y1, x2, y2);
	float b = dist(x2, y2, x3, y3);
	float c = dist(x3, y3, x1, y1);
	return 0.25 * sqrt(
		(a+b+c)*(b+c-a)*(c+a-b)*(a+b-c));
}

float overlap(float x, float y)
{
	// What area of the square at x,y, w=g, h=g
	// is inside the circle at 0,0, radius 1.0?
	float x2 = x + g, y2 = y+g;
	float A=0;
	if (isInCircle(x2, y2))
		return g*g; // Entirely inside
	if (!isInCircle(x, y))
		return 0; // Entirely outside
	if (isInCircle(x, y2))
	{
		// Hits top edge
		float ix = sqrt(1 - y2*y2);
		A += (ix - x) * (y2 - y);
		x = ix;
	}
	if (isInCircle(x2, y))
	{
		float iy = sqrt(1 - x2*x2);
		A += (iy - y) * (x2 - x);
		y = iy;
	}
	if (!isInCircle(x2, y))
	{
		x2 = sqrt(1 - y*y);
	}
	if (!isInCircle(x, y2))
	{
		y2 = sqrt(1 - x*x);
	}
	// Now have an arc centered at x, y
	float dc = dist(x, y2, x2, y);
	float da = dist(0, 0, x, y2);
	float db = dist(0, 0, x2, y);
	float theta = acos((-dc*dc + da*da + db*db)/ (2 * da * db));
	float aarc = theta/2;
	float tria = area(0, 0, x, y, x, y2);
	float trib = area(0, 0, x, y, x2, y);
	float dA = aarc - tria - trib;
	assert(dA + 1e7 > 0);
	assert(dA < (y2 - y)*(x2 - x) + 1e7);
	A += dA;
	return A;
}

char *doC(char **&toks)
{
	float f = atof(*toks++);
	R = atof(*toks++);
	t = atof(*toks++);
	r = atof(*toks++);
	g = atof(*toks++);
	r+=f;
	t+=f;
	g-=f*2;
	f = 0;
	if (g<=0)
		return "1";
	if (t>=R)
		return "1";
	if (r>=R)
		return "1";
	// Normalize
	float lR = R - t;
	float pAdd = (M_PI*R*R - M_PI*lR*lR) / (M_PI*R*R);
	R = 1;
	t/=lR;
	r/=lR;
	g/=lR;

	s = g + 2*r;

	// Monte carlo works fine for any number of strings... just a bit slow...
	/*
	float yy=0, nn=0;
	RandMersenne *rm = randMersenneCreate();
	for (int i=0; i<10000000000; i++) {
		float x = randMersenneStep(rm) / (double)0xFFFFFFFF;
		float y = randMersenneStep(rm) / (double)0xFFFFFFFF;
		if (!isInCircle(x, y))
			continue;
		if (hits(x, y))
			yy++;
		else
			nn++;
	}
	float p = yy / (yy+nn);
	*/

	// Ah, didn't notice that part of the question, only 2000 strings!
	int ns = (int)ceil(1 / s);
	float totalA=0;
	for (int i=0; i<ns; i++) {
		for (int j=0; j<ns; j++) {
			float x = i*s + r;
			float y = j*s + r;
			float A = overlap(x, y);
			totalA += A;
		}
	}
	float p = 1 - (totalA * 4 / M_PI);
	p = pAdd + (1-pAdd)*p;
	static char buf[10];
	sprintf(buf, "%1.6f", p);
	return buf;
}

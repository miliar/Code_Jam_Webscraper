/*
 * QA_speakingInTongues.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: Ashok
 */

#include <cstdio>
using namespace std;

/* MACROS */
#define INFILENAME "D:\\09_Projects\\codeJam\\2012\\qa-small-attempt0.in"
#define OUTFILENAME "D:\\09_Projects\\codeJam\\2012\\qa-small-attempt0.out"

/* STATIC VARIABLES */
static int noTC;

const char map[27] = {	'y',
		'h',
		'e',
		's',
		'o',
		'c',
		'v',
		'x',
		'd',
		'u',
		'i',
		'g',
		'l',
		'b',
		'k',
		'r',
		'z',
		't',
		'n',
		'w',
		'j',
		'p',
		'f',
		'm',
		'a',
		'q'};

/* FUNCTION DECLARATIONS */
static void init(void);
static void exec(int tc);

/*==================================================*/

int main()
{
	init();
	getchar();
	for(int tc = 0; tc < noTC; tc++)
	{
		exec(tc+1);
	}
	return 0;
}

static void init(void)
{
	freopen(INFILENAME, "r", stdin);
	freopen(OUTFILENAME, "w", stdout);
	scanf("%d", &noTC);
}

static void exec(int tc)
{
	char inStr[101], outStr[100];
	int i;
	gets(inStr);
	for(i = 0; inStr[i] != '\0'; i++){
		if(inStr[i] == ' '){
			outStr[i] = ' ';
		}
		else {
			outStr[i] = map[inStr[i] - 'a'];
		}
	}
	outStr[i] = '\0';
	printf("Case #%d: %s\n", tc, outStr);
}

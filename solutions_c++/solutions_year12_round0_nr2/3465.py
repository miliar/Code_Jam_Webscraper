/*
 * QB_DancingWithGooglers.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: Ashok
 */

#include <cstdio>
using namespace std;

/* MACROS */
#define INFILENAME "D:\\09_Projects\\codeJam\\2012\\qb-large.in"
#define OUTFILENAME "D:\\09_Projects\\codeJam\\2012\\qb-large.out"

/* STATIC VARIABLES */
static int noTC;

/* FUNCTION DECLARATIONS */
static void init(void);
static void exec(int tc);

/*==================================================*/

int main()
{
	init();
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
	int noGoog, noSup, best, pts[100], i, noBest, s;
	scanf("%d %d %d", &noGoog, &noSup, &best);
	for(i = 0; i < noGoog; i++){
		scanf("%d", &pts[i]);
	}
	noBest = 0;
	for(i = 0; i < noGoog; i++){
		if(pts[i]%3 == 0){
			s = pts[i]/3;
			if(s >= best){
				noBest++;
			}
			else{
				if(pts[i] > 0){
					s++;
					if(s >= best){
						if(noSup > 0){
							noBest++;
							noSup--;
						}
					}
				}
			}
		}
		else if(pts[i]%3 == 1){
			s = (pts[i]-1)/3;
			if((s+1) >= best){
				noBest++;
			}
		}
		else {
			s = (pts[i] - 2)/3;
			if((s+1) >= best){
				noBest++;
			}
			else if((s+2) >= best){
				if(noSup > 0){
					noBest++;
					noSup--;
				}
			}
		}
	}
	printf("Case #%d: %d\n", tc, noBest);
}

/*
 * QC_RecycledNum_2.cpp
 *
 *  Created on: 14-Apr-2012
 *      Author: Ashok
 */

#include <cstdio>
#include <cmath>
using namespace std;

/* MACROS */
#define INFILENAME "D:\\09_Projects\\codeJam\\2012\\qC-small-attempt0.in"
#define OUTFILENAME "D:\\09_Projects\\codeJam\\2012\\qC-small-attempt0.out"

/* STATIC VARIABLES */
static int noTC;

/* FUNCTION DECLARATIONS */
static void init(void);
static void exec(int tc);
static int splitDgts(int i, int d[]);

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
	int ans, a, b, ar[7], dgts;
	int n,m;
	ans = 0;
	scanf("%d %d", &a, &b);
	for(n = a; n < b; n++){
		dgts = splitDgts(n, ar);
		for(int j = 0; j < dgts-1; j++){
			m = (n % int(pow(10,j+1)))*int(pow(10,dgts-j-1)) + n/int(pow(10,j+1));
			if(m <= b){
				if(m > n){
					ans++;
					//printf("%3d, %3d, %d\n",n, m, j);
				}
			}
		}
	}
	printf("Case #%d: %d\n", tc, ans);
}

static int splitDgts(int i, int d[]){
	int j;
	for(j = 0; i > 0; j++){
		d[j] = i%10;
		i = i/10;
	}
	return j;
}

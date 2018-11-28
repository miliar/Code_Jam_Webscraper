#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

#define MAXN 128
#define TIME 1440

int sa[TIME], sb[TIME];
vector<int> nexta[TIME], nextb[TIME];
int addA, addB;
int A, B, T, tc;

int mi(int h, int m) { return h * 60 + m;}

int main()
{
	int i, h1, m1, h2, m2, waita, waitb, ansa, ansb, x, j;

	scanf("%d", &tc);
	FOR(x, tc)
	{
		ZERO(sa); ZERO(sb);
		scanf("%d %d %d", &T, &A, &B);
		waita = 0; waitb = 0;
		ansa = 0; ansb = 0;
		FOR(i, TIME) { nexta[i].clear(); nextb[i].clear(); }
		FOR(i, A)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2); 
			sa[mi(h1, m1)]++;
			nexta[mi(h1, m1)].push_back(mi(h2, m2) + T);
		}
		FOR(i, B)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2); 
//			fprintf(stderr, "%02d:%02d = %d\n", h1, m1, mi(h1, m1));
			sb[mi(h1, m1)]++;
			nextb[mi(h1, m1)].push_back(mi(h2, m2) + T);
		}
		FOR(i, TIME)
		{
/*			if (i == 540 || i == 600 || i == 660 || i == 722) 
			{
				fprintf(stderr, "%d %d %d %d\n", waita, waitb, ansa, ansb);
			}*/
			if (sa[i] < 0) waita -= sa[i];
			if (sb[i] < 0) waitb -= sb[i];
			if (sa[i] > 0) 
			{ 
				if (waita > sa[i]) waita -= sa[i]; 
				else { sa[i] -= waita; waita = 0; ansa += sa[i]; } 
			}
			if (sb[i] > 0) 
			{ 
				if (waitb > sb[i]) waitb -= sb[i]; 
				else { sb[i] -= waitb; waitb = 0; ansb += sb[i]; } 
			}
			FOR(j, nexta[i].size()) sb[nexta[i][j]]--;
			FOR(j, nextb[i].size()) sa[nextb[i][j]]--;
/*			if (i == 540 || i == 600 || i == 660 || i == 722) 
			{
				fprintf(stderr, "%d %d %d %d\n", waita, waitb, ansa, ansb);
			}*/
		}

		printf("Case #%d: %d %d\n", x + 1, ansa, ansb);
	}
	return 0;
}


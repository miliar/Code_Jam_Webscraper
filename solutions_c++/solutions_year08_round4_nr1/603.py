/* kaneko-A.cc
 */
#include <algorithm>
#include <cstdio>
using namespace std;
const int MAXM = 10000;
int N, M, V;
int gate[MAXM], changeable[MAXM], value[MAXM];
int true_table[MAXM], false_table[MAXM];

void solve()
{
    fill(true_table, true_table+M, MAXM);
    fill(false_table, false_table+M, MAXM);
    for (int i=(M-1)/2; i<M; ++i) {
	if (value[i]) true_table[i] = 0;
	else false_table[i] = 0;
    }
    for (int i=(M-1)/2-1; i>=0; --i) {
	int tl = true_table[2*(i+1)-1], tr = true_table[2*(i+1)];
	int fl = false_table[2*(i+1)-1], fr = false_table[2*(i+1)];

	// printf("node %d gate %d l %d r %d\n", i+1, gate[i], 2*(i+1), 2*(i+1)+1);
	if (gate[i]) { // and
	    true_table[i] = min(MAXM, tl + tr);
	    false_table[i] = min(fl, fr);
	    if (changeable[i])
		true_table[i] = min(true_table[i], 1+min(tl, tr));
	} else { // or gate
	    true_table[i] = min(tl, tr);
	    false_table[i] = min(MAXM, fl + fr);
	    if (changeable[i])
		false_table[i] = min(false_table[i], 1+min(fl, fr));
	}
    }
}

int main()
{
    scanf("%d", &N);
    for (int t=0; t<N; ++t) {
	scanf("%d%d", &M, &V);
	fill(changeable, changeable+M, 0);
	for (int i=0; i<(M-1)/2; ++i) scanf("%d%d", gate+i, changeable+i);
	for (int i=0; i<(M+1)/2; ++i) scanf("%d", value+(M-1)/2+i);
	solve();
#if 0
	for (int i=0; i<M; ++i)
	    printf("node %d true %d false %d\n", i+1, true_table[i], false_table[i]);
#endif
	if (V) {
	    if (true_table[0] < MAXM) {
		printf("Case #%d: %d\n", t+1, true_table[0]);
		continue;
	    }
	} else {
	    if (false_table[0] < MAXM) {
		printf("Case #%d: %d\n", t+1, false_table[0]);
		continue;
	    }
	}
	printf("Case #%d: IMPOSSIBLE\n", t+1);
    }
}

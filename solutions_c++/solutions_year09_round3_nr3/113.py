#include <cstdio>
#include <queue>
using namespace std;

int P, Q;
int locs[10009];
int segs[10009];
int total = 0;
int table[128][128];
int table2[128][128];

int calc2(int s, int e)
{
    if(s + 1 == e)
        return segs[s];
    else if(table2[s][e])
	return table2[s][e];
    else
        return table2[s][e] = segs[e - 1] + 1 + calc2(s, e - 1);
}

int calc(int s, int e)
{
    if(s + 1 >= e)
	return 0;
    else if(table[s][e])
        return table[s][e] - 1;
    else 
    {
	int v = INT_MAX;
        for(int i = s; i < e - 1; i++)
	    v = min(v, calc(s, i + 1) + calc(i + 1, e));
	v += calc2(s, e) - 1;
	return (table[s][e] = v)++;
    }
}
int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
 total = 0;

	scanf("%d%d", &P, &Q);
        for(int i = 0, last = 0; i < Q; i++)
	{
	    scanf("%d", locs + i);
            segs[total++] = locs[i] - last - 1;
	    
            last = locs[i];
	}

	segs[total++] = P - locs[Q - 1];
memset(table, 0, sizeof(table));
memset(table2, 0, sizeof(table2));
        printf("Case #%d: %d\n", t, calc(0, total));
    }
    return 0;
}

#include <cstdio>
#include <cstring>
using namespace std;

const int SIZE = 2048;
int N;
int ps[SIZE];
int table[SIZE];

void go(int l, int r, int p, int bound)
{
//    printf("%d %d %d %d\n", l, r, p, bound);
    if(l == r)
	table[l] = bound;
    else 
    {
	if(ps[l] > r)
	{
	     table[l] = bound;
	     go(l + 1, r, p, bound - 1);
	}
	else
	{
	    go(ps[l], r, p, bound);	 
	    go(l, ps[l] - 1, ps[l], table[ps[l]]  - ((table[ps[ps[l]]] - table[ps[l]]) * (long long)(ps[l] - l) + ps[ps[l]] - ps[l] - 1) / (ps[ps[l]] - ps[l]));
	}
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int testnum = 1; testnum <= T; testnum++)
    {
	memset(table, -1, sizeof(table));
	printf("Case #%d:", testnum);

	scanf("%d", &N);
	for(int i = 1; i < N; i++)
	    scanf("%d", ps + i);

	bool check = true;
	for(int i = 1; i < N; i++)
	{
	    if(ps[i] <= i)
		check = false;

	    for(int j = i + 1; j < ps[i]; j++)
		if(ps[j] > ps[i])
		    check = false;
	}

	if(!check)
	    puts(" Impossible");
	else
	{

	    table[N] = 1000000000;
    	    table[N + 1] = table[N] + 1;
	    ps[N] = N + 1;
	    go(1, N - 1, N, 1000000000 - 1);

	    for(int i = 1; i <= N; i++)
		printf(" %d", table[i]);
	    printf("\n");
	}
	    

    }

    return 0;
}

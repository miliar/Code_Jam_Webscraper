#include <cstdio>

#define N 64

char a[N][N];
int T, n;


void solve(int test)
{

    int i, j, k,t,sum = 0;

    for(i = 1; i <= n; ++i)
    {
	for(j = n; j >= 1; --j)
	    if(a[i][j] == '1') break;

	int ok = 0,p= -1;

	if(j > i)
	{
	    for(k = i+1; k <= n; ++k)
	    {
		for(t = n; t >= 1; --t)
		    if(a[k][t] == '1') break;

		if(t <= i) 
		{
		    ok = 0;
		    p = k;
		    break;
		}
	    }

	    if(p != -1)
	    {
		sum += p - i;

		char ax[N];
		for(k = 1; k <= n; ++k)
		    ax[k] = a[p][k];

		for(k = p -1; k >= i; --k)
		    for(t = 1; t <= n; ++t)
			a[k+1][t] = a[k][t];

		for(k = 1; k <= n; ++k)
		    a[i][k] = ax[k];	    


	    }

	}

    }

    /*
    for(i = 1; i <= n; ++i)
    {
	for(j = 1; j <= n; ++j)
	    printf("%c ", a[i][j]);
	printf("\n");
    }

    printf("\n");
*/
    printf("Case #%d: %d\n",test, sum);

}



int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d\n", &T);
    for(int t = 1 ; t <= T; ++t)
    {
	scanf("%d\n", &n);
	int i,j;
	for(i = 1; i <= n; ++i)
	    gets(a[i]);

	for(i = 1; i <= n; ++i)
	    for(j = n; j >= 1; --j) a[i][j] = a[i][j-1];

	solve(t);

    }

    return 0;
}


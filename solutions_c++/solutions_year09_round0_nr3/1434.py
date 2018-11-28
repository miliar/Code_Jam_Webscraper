#include <cstdio>
#include <algorithm>
#include <cstring>
#define mod 10000

using namespace std;


int dp[32][502];
int nr[32][502];

int T, n, m;
char b[502];
char a[32]=" welcome to code jam";


int memo(int i, int j)
{
    if(i == 0 || j == 0) return 1;
    if(nr[i][j] != -1) return nr[i][j];
    

    nr[i][j] = 0;
    if(a[i] == b[j]) 
    {
	nr[i][j] = memo(i-1, j-1);
    }

    else
    {
	if(dp[i][j-1] >= dp[i-1][j])
	    nr[i][j] += memo(i, j-1), nr[i][j] %= mod;
	if(dp[i-1][j] >= dp[i][j-1])
	    nr[i][j] += memo(i-1, j), nr[i][j] %= mod;
    }

}


void solve(int test)
{
    
    int i, j,k,t;

    n = strlen(a) - 1;
    m = strlen(b);

    for(i = m; i ; --i)
	b[i] = b[i-1];

    //dp[0][0]=1;
//    for(i = 1; i <= m; ++i)
//	if(b[i] == a[1]) dp[1][i] = 1;

    


    for(i = 1; i <= n; ++i)
	
       for(j = 1; j <= m; ++j)
       {
	    if(a[i] == b[j])
		dp[i][j] = dp[i-1][j-1]  + 1;
	    else
		dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
     
       }

//  for(i = 0; i <= n; ++i)
//	for(j = 0; j <= m; ++j)
	// nr[i][j] = -1;
	    //   if(dp[1][j] == 1) nr[1][j] = 1;
//	    else nr[i][j] = -1;

 
    for(i = 1; i <= m; ++i)
	if(b[i] == a[1])
	nr[1][i] = 1;

	
    for(i = 2; i <= n; ++i)
	for(j = 1; j <= m; ++j)
	    if(a[i] == b[j])
	    {
		nr[i][j] = 0;

		for(k = i-1; k >= 1; --k)
		    for(t = j-1; t >= 1; --t)
			if(a[k] == b[t])
			    if(dp[i][j] == dp[k][t] + 1)
				nr[i][j] += nr[k][t], nr[i][j] %= mod;

	    }

	    
    int sol = 0;

    for(i = 1; i <= n; ++i)
	for(j = 1; j <= m; ++j)
	    if(dp[i][j] == 19)
		sol += nr[i][j], sol %= mod;

    int nrzero = 0;
    if(sol < 10000)
    {
	int nr =0;
	int p =sol;
	while(p) ++nr, p /= 10;
	nrzero = 4 - nr;
    }

    if(sol == 0) nrzero = 3;
    printf("Case #%d: ",test);
    for(i = 1; i <= nrzero;++i)printf("0");


    
   printf("%d\n",sol);
    /*
    printf("%d %d\n", n, m);
    for(j = 0; j <= m; ++j) printf("%c  ", b[j]);

    printf("\n");
    for(i = 1; i <= n; ++i)
    {
	printf("%c ", a[i]);
	for(j = 1; j <= m; ++j)
	    printf("%2d ",nr[i][j]);
	printf("\n");
    }
    printf("\n\n");
    printf("%d\n", dp[n][m]);

    */
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d\n", &T);
    for(int t = 1; t <= T; ++t)
    {
	for(int j = 0; j <= 500; ++j) b[j] = 0;
	memset(dp, 0, sizeof(dp));
	
	memset(nr, 0, sizeof(nr));
	gets(b);
	solve(t);

    }

    return 0;
}


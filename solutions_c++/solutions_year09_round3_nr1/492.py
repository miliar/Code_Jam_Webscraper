#include <cstdio>
#include <cstring>

char a[64];
int x[64];
int used[256];

void solve(int test)
{
    memset(x, 0, sizeof(x));
    memset(used, -1, sizeof(used));

    int i;

    x[0] = 1;
    used[a[0]] = 1;

    int n = strlen(a);
    int nr = 0;

    for(i = 1; i < n; ++i)
    {
	if(used[a[i]] == -1)
	{
	    used[a[i]] = nr;
	    if(nr == 0) nr += 2;
	    else ++nr;
	}

	x[i] = used[a[i]];

    }
 
    
    int b  = 0;

    for(i = 0; i < n; ++i)
       if(x[i] > b) b =x[i];

    ++b;

     long long sol = x[n-1];

    long long pw = b;

    for(i = n-2; i >= 0; --i)
    {
//	printf("%d %lld\n", x[i], pw);
	if(x[i])sol += (long long) x[i] * (long long)pw;
	pw = (long long)pw *(long long) b;

    }	
    
    printf("Case #%d: %lld\n", test,sol);

}



int main()
{
    int T;

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d\n", &T);

    for(int t = 1; t <= T; ++t)
    {
	scanf("%s\n", &a);
	solve(t);

    }



    return 0;
}



//c small
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int a[102];
int T, n, m;
int perm[102];
int Q[102];


void solve(int test)
{
    memset(a, 0, sizeof(a));
    memset(perm, 0, sizeof(perm));
    
   int i,v, sol = 0;
    int solMin = 0x3f3f3f3f;

   for(i = 1; i <= m; ++i)
       perm[i] = i;

   do
   {
       memset(a, 0, sizeof(a));

       sol = 0;
       for(i = 1; i <= m; ++i)
       {
	   v = Q[perm[i]];
	   a[v] = 1;

	   int j;

	   for(j = v-1; j >= 1 && a[j] == 0; --j)
	       ++sol;

	   for(j = v +1; j <= n && a[j] == 0; ++j)
	       ++sol;


       }

       if(solMin > sol) solMin = sol;
   }while(next_permutation(perm+1,perm+m+1));

   printf("Case #%d: %d\n", test, solMin);

}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d\n", &T);

    for(int t = 1; t <= T; ++t)
    {
	scanf("%d %d\n", &n, &m);
	for(int i =1; i <= m; ++i)
	    scanf("%d ", &Q[i]);

	solve(t);


    }

    return 0;
}



#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	int m=0;
	int t;
	for(int j=0; j<n; j++)
	{
	    scanf("%d", &t);
	    if(t >= 3*p-2)
		m++;
	    else if(s > 0 && t >= max(1, 3*p-4))
	    {
		m++;
		s--;
	    }
	    //printf("%d %d\n", t, m);
	}
	   printf("Case #%d: %d\n",i,  m);
    }
    return 0;
}

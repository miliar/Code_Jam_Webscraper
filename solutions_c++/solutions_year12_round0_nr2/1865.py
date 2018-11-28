#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    FILE *fin = fopen("B-large.in","r");
    FILE *fout = fopen("B-large.out","w");

    int T;
    int n, s, p, x, ans, p1, p2;

    fscanf(fin, " %d ", &T);
    for(int t = 1; t <= T; t++)
    {
        ans = 0;
        fscanf(fin, " %d %d %d ", &n, &s, &p);
        p1 = p > 1 ? p-1 : 0;
        p2 = p > 2 ? p-2 : 0;
        for(int i = 0; i < n; i++)
        {
            fscanf(fin, " %d ", &x);
	if(x >= p+p1+p1)
	{
	    ans++;
	}
	else if(x >= p+p2+p2 && s)
	{
	    ans++;
	    s--;
	}
        }
        fprintf(fout, "Case #%d: %d\n", t, ans);
    }
    return 0;
}

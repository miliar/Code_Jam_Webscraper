#include <algorithm>
using namespace std;

#include <stdio.h>

int k;
int len;
char s[10240];
char sp[10240];

int Min(int a, int b)
{
	return a<b?a:b;
}

void Read()
{
	scanf("%d %s", &k, &s);
	len = strlen(s);
}

int GetCurVal()
{
	int val = 1;

	for (int i=1; i<len; i++)
		if(sp[i-1] != sp[i])
			val++;

	return val;
}

int Solve()
{
	int ans = 999999999;
	int i;
    int perm[8];
    
	for (i=0; i<k; i++)
		perm[i] = i;

    do
    {
        for(i=0; i<len/k; i++)
		{
            for(int j=0; j<k; j++)
				sp[i*k+j] = s[i*k+perm[j]];
		}

        int cur = GetCurVal();
		if(ans > cur)
			ans = cur;
    }
	while(next_permutation(perm, perm+k));
    
	return ans;
}

int main()
{
	freopen("4.in", "rt", stdin);
	freopen("4.out", "wt", stdout);

	int t;
	int n;

	scanf("%d", &n);
	for (t=1; t<=n; t++)
	{
		Read();		
		printf("Case #%d: %d\n", t, Solve());
	}
	return 0;
}


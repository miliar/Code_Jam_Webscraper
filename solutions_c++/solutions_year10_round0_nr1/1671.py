#include <iostream>

using namespace std;


int main()
{
	int nCase, c;
	int n, k;
	int res[32];

 	freopen("A-large.in","r", stdin );
 	freopen("A-large.out","w", stdout );

	res[0] = 0;
	res[1] = 1;
	for(int i=2; i<=30; i++)
		res[i] = res[i-1]*2+1;

	scanf("%d", &nCase);
	for(c=1; c<=nCase; c++)
	{
		scanf("%d%d", &n, &k);
		if(k%(res[n]+1)==res[n])
			printf("Case #%d: ON\n", c);
		else
			printf("Case #%d: OFF\n", c);
	}
	return 0;
}
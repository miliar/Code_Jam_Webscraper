#include <cstdio>
#include <algorithm>

using namespace std;

int calc(int A, int B)
{
	int rep = 0;
	int c1,c2,c3;


	int truc = max(A, 10);
	for (int i = truc; i <= B && i <= 100; i++)
	{
		c1 = i/10;
		c2 = i%10;
		if (c2 != 0 && 10*c2+c1 > i && 10*c2+c1 <= B)
			rep++;
	}
	int s, s2;

	for (int i = max(A, 100); i <= B; i++)
	{
		c1 = i/100;
		c2 = (i/10)%10;
		c3 = i%10;
		s = c3*100+c1*10+c2;
		s2 = c2*100+c3*10+c1;

		if (c3 != 0 && s > i && s <= B)
		{
			rep++;
		}

		if (c2 != 0 && s2 > i && s2 <= B && s2 != s)
		{
			rep++;
		}


	}
	return rep;
}


int main()
{
	freopen("truc.out", "w", stdout);
	freopen("truc.in", "r", stdin);
    int nbCas;
    scanf("%d", &nbCas);
    int A,B;

    for (int cas = 1; cas <= nbCas; cas++)
    {
    	scanf("%d %d", &A, &B);
    	printf("Case #%d: %d\n", cas, calc(A,B));
    }







    return 0;
}

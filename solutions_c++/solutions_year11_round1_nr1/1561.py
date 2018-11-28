#include <cstdio>

int gcd(int a, int b)
{
	return b == 0 ? a : gcd(b, a % b);
}
int lcm(int a, int b)
{
	return a / gcd(a, b) * b;
}

void reduce(int &X, int &Y)
{
	int D = gcd(X, Y);
	X /= D;
	Y /= D;
}


int main(){
	int T, PG, PD, N, t = 0;
	for (scanf("%d", &T); T > 0; --T)
	{
		scanf("%d%d%d", &N, &PD, &PG);
		int FG = 100;
		int FD = 100;
		reduce(FG, PG);
		reduce(FD, PD);
// printf("%d/%d, %d/%d\n", PG, FG, PD, FD);
		printf("Case #%d: ", ++t);
		if (FD > N || PD != 0 && PG == 0 || PD != FD && PG == FG)
		{
			printf("%s\n", "Broken");
		}
		else
		{
			printf("%s\n", "Possible");
		}
	}
	return 0;
}
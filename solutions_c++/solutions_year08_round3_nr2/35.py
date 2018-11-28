#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

char digits[64];
char sign[64];
long long res;

void input(void)
{
	scanf("%s\n", digits);
}

void calc(void)
{
	long long val=0, num=0;
	char lastSign = 1;

	for(int i = 0; digits[i]; ++i)
	{
		if(sign[i])
		{
			val += num*lastSign;
			num = 0;
			lastSign = sign[i];
		}
		num = num*10 + digits[i]-'0';
	}
	val += num*lastSign;
	if(val%2==0 || val%3==0 || val%5==0 || val%7==0)
	{
		++res;
	}
}

void rec(int pos)
{
	if(!digits[pos])
	{
		calc();
		return;
	}
	for(sign[pos] = -1; sign[pos]<=1; ++sign[pos])
	{
		rec(pos+1);
	}
}

int main(void)
{
	int N, i;
	
	sign[0] = 0;
	scanf("%d\n", &N);
	fprintf(stderr, "cases=%d\n", N);
	for(i = 1; i <= N; ++i)
	{
		fprintf(stderr, "%d\n", i);
		input();
		res=0;
		rec(1);
		printf("Case #%d: %Ld\n", i, res);
	}
	return 0;
}

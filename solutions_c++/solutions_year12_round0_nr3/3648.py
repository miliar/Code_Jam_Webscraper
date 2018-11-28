#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

const int N = 2000222;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a > b ? a : b;
}

int Used[N], Ans;
int a, b;

int GetVal(int n, int digit)
{
	int m = n;
	int tmp;
	int w = 1;
	int ret = 0;
	
	while(m > 0)
	{
		m /= 10;
		w *= 10;
		tmp = n/w + n%w*digit/w;
		
		if(tmp < n && tmp*10 > digit && Used[tmp] != n)
		{
			if(tmp >= a)Ans ++;
			Used[tmp] = n;
		}
	}
	return ret;
}

void GetAns()
{
	int i, digit;
	digit = 10;
	Ans = 0;
	for(i = a; i <= b; i ++)
	{
		Used[i] = -1;
		while(i >= digit)digit *= 10;
		GetVal(i, digit);
	}
}

int main()
{
	int i, j, k;
	int T, cc = 0;
	
	scanf("%d", &T);
	while(T --)
	{
		scanf("%d %d", &a, &b);
		GetAns();
		printf("Case #%d: %d\n", ++cc, Ans);
		//printf("%d %d\n", Sum[1][b], Sum[0][a-1]);
	}
	return 0;
}

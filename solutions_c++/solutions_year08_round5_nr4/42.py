#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const	int		M = 10007;
const	int		limitSize = 20;

struct	Tpoint
{
	int	x , y;
};

bool	operator < (const Tpoint& A , const Tpoint& B)
{
	if (A.x == B.x) return A.y < B.y;
	return	A.x < B.x;
}

int		H , W;
int		n , p;
Tpoint		list	[limitSize];
Tpoint		S	[limitSize];

int		first	[M + 10];

void	preCalc()
{
	first[0] = 1;
	for (int i = 1; i < M; i ++)
		first[i] = first[i - 1] * i % M;
}


void	init()
{
	scanf("%d%d%d" , &H , &W , &n);
	for (int i = 0; i < n; i ++)
	{
		scanf("%d%d" , &list[i].x , &list[i].y);
	}
	sort(list , list + n);
}

int	countM(int v)
{
	int	cc = 0;
	while (v)
	{
		cc += v / M;
		v /= M;
	}
	return	v;
}

int	powMod(int a , int n)
{
	int	ret = 1;
	int	w = a;

	while (n)
	{
		if (n & 1) ret = ret * w % M;
		w = w * w % M;
		n >>= 1;
	}

	return	ret;
}

int	getMod(int v)
{
	return	first[v % M] * powMod(first[M - 1] , v / M) % M;
}

inline	int	fix(int v)
{
	return	(v % M + M) % M;
}

int	gcd(int a , int b , int& x , int& y)
{
	if (b == 0)
	{
		x = 1 , y = 0;
		return a;
	}
	else
	{
		int	x0 , y0;
		gcd(b , a % b , x0 , y0);
		x = y0 % M;
		y = fix( x0 - a / b * y0 % M );

		return	1;
	}
}

int	calc(int r , int c)
{
	if (r <= 0 || c <= 0) return 0;
	if ((2 * c - r) % 3) return 0;

	int	x , y;
	y = (2 * c - r) / 3;
	x = c - y * 2;

	if (x < 0 || y < 0) return 0;
	if (x == 0 || y == 0) return 1;
	
	if (countM(x + y) > countM(x) + countM(y)) return 0;

	int	b = getMod(x + y);
	int	a = getMod(x) * getMod(y) % M;

	gcd(a , M , x , y);

	x = ( x % M + M ) % M; 
	
	return fix( x * b );
}

int	calc()
{
	if (p == 0 && H == 1 && W == 1) return 1;
	S[p + 1].x = H;
	S[p + 1].y = W;

	int	ret = 1;
	for (int i = 0; i <= p; i ++)
		ret = ret * calc(S[i + 1].x - S[i].x , S[i + 1].y - S[i].y) % M;

	return	ret;
}

void	solve()
{
	int	ret = 0;

	int	stat , top = 1 << n;
	int	i;

	S[0].x = 1; S[0].y = 1;
	for (stat = 0; stat < top; stat ++)
	{
		for (i = 0 , p = 0; i < n; i ++)
			if (stat & (1<<i))
			{				
				S[ ++ p ] = list[i];
			}
		if (p % 2)
			ret = fix(ret - calc());
		else	ret = (ret + calc()) % M;
	}

	ret = fix(ret);

	printf("%d\n" , ret);
}

int	main()
{
	freopen("D-small-attempt0.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	preCalc();

	int		cntCase , t;
	scanf("%d" , &cntCase);
	for (t = 1; t <= cntCase; t ++)
	{
		init();
		printf("Case #%d: " , t);
		solve();
	}

	return 0;
}

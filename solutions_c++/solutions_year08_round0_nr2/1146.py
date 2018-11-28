#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const	int	limitSize	= 200 + 10;

struct	Tline
{
	int	st , ed;
	int	dir;

	void	read()
	{
		read_time( st );
		read_time( ed );
	}

	void	read_time(int& t)
	{
		char	buf	[100];
		scanf("%s" , buf);

		t = ((buf[0] - '0') * 10 + (buf[1] - '0')) * 60
			+ ((buf[3] - '0') * 10 + (buf[4] - '0'));
	}
};

bool	operator < (const Tline& A , const Tline& B)
{
	return	A.st < B.st;
}

int		na , nb;
int		T;

Tline		list	[limitSize];

void	init()
{
	scanf("%d" , &T);
	scanf("%d%d" , &na , &nb);

	for (int i = 0; i < na; i ++)
	{
		list[i].read();
		list[i].dir = 0;
	}
	for (int i = 0; i < nb; i ++)
	{
		list[na + i].read();
		list[na + i].dir = 1;
	}
}

bool		done	[limitSize];

void	solve()
{
	int	n = na + nb;
	sort(list , list + n);

	memset(done , 0 , sizeof(done));

	int	i;
	int	left = n;
	int	p;
	int	cc[2];

	cc[0] = cc[1] = 0;
	while (left)
	{
		for (p = 0; p < n; p ++)
			if (! done[p]) break;
		cc[ list[p].dir ] ++;

		while (p < n)
		{
			left --;
			done[p] = 1;
			for (i = p + 1; i < n; i ++)
				if (! done[i] && list[i].dir != list[p].dir && list[i].st >= list[p].ed + T)
					break;
			p = i;
		}
	}

	printf("%d %d\n" , cc[0] , cc[1]);
}

int	main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int	cntCase , t;
	scanf("%d" , &cntCase);

	for (t = 1; t <= cntCase; t ++)
	{
		init();

		printf("Case #%d: " , t);
		solve();
	}

	return 0;
}

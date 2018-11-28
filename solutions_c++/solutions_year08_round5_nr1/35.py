#include <cstdio>
#include <cstring>

const	int		base		= 3010;
const	int		limitSize	= 6050;

int		top	[limitSize] , bottom[limitSize];
int		left	[limitSize] , right[limitSize];

int		U , D , L , R;
int		x , y , nx , ny , dir;

char		str	[100];

long long	area;
int		dx[] = {0 , 1 , 0 , -1};
int		dy[] = {1 , 0 , -1 , 0};

void	init()
{
	x = y = U = D = L = R = base; dir = 0;
	
	int	i;
	for (i = 0; i < limitSize; i ++)
		top[i] = bottom[i] = left[i] = right[i] = base;


	area = 0;
	int	t , k;
	scanf("%d" , &t);
	while ( t -- )
	{
		scanf("%s%d" , str , &k);
		while (k --)
		{
			for (i = 0; str[i]; i ++)
			{
				if (str[i] == 'R') dir = (dir + 1) % 4;
				else if (str[i] == 'L') dir = (dir + 3) % 4;
				else
				{
					nx = x + dx[dir];
					ny = y + dy[dir];
					area += (long long)x * ny - (long long)y * nx;

					if ( nx < left[ny] ) left[ny] = nx;
					if ( nx > right[ny] ) right[ny] = nx;
					if ( ny < top[nx] ) top[nx] = ny;
					if ( ny > bottom[nx] ) bottom[nx] = ny;

					if ( ny < U ) U = ny;
					if ( ny > D ) D = ny;
					if ( nx < L ) L = nx;
					if ( nx > R ) R = nx;
					x = nx; y = ny;

					//printf("Path : %d %d\n" , x - base , y - base);
				}
			}
		}
	}
}

void	solve()
{
	area /= 2; if (area < 0) area = - area;

	
	int	tot = 0;
	
	int	x , y;
	for (x = L; x < R; x ++)
	{
		for (y = U; y < D; y ++)
		{
			if ( left[y] <= x + 0.5 && x + 0.5 <= right[y]
				&& left[y + 1] <= x + 0.5 && x + 0.5 <= right[y + 1]				
				|| top[x] <= y + 0.5 && y + 0.5 <= bottom[x]
				&& top[x + 1] <= y + 0.5 && y + 0.5 <= bottom[x + 1] ) {
					//printf("%d %d\n" , x - base , y - base);	
				tot ++;
			}
		}
	}

	tot -= area;

	printf("%d\n" , tot);
}

int	main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

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

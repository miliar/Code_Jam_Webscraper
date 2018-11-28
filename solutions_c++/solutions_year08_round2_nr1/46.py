#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 100100;
struct Tnode{
	int x, y;
} p[MAXN];

bool operator < (const Tnode&a, const Tnode&b)
{
	if (a.x!=b.x)
		return a.x<b.x;
	else
		return a.y<b.y;	
}

int n;
__int64 f[3][3];

void init()
{
	__int64 A, B, C, D, xx, yy, M, X, Y;
	int i;
	
	scanf("%d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n, &A, &B, &C, &D, &xx, &yy, &M);
	X=xx; Y=yy;
	p[0].x=X; p[0].y=Y;
	for (i=1; i<n; i++){
		X=(A*X+B)%M;
		Y=(C*Y+D)%M;
		p[i].x=X; p[i].y=Y;
	}
	
}

void work()
{
	int i, j, k, a0, a1, b0, b1, c0, c1;
	__int64 s;
	
	sort(p, p+n);
	memset(f, 0, sizeof(f));
	for (i=0; i<n; i++)
		if (i==0 || (p[i].x!=p[i-1].x || p[i].y!=p[i-1].y)){
			f[p[i].x%3][p[i].y%3]++;	
		}	

	s=0;
	for (i=0; i<9; i++)
		for (j=i; j<9; j++)
			for (k=j; k<9; k++){
				a0=i/3; a1=i%3;
				b0=j/3; b1=j%3;
				c0=k/3; c1=k%3;
				if ((a0+b0+c0)%3==0 && (a1+b1+c1)%3==0){
					if (i!=j && j!=k)
						s+=(f[a0][a1]*f[b0][b1]*f[c0][c1]);	
					else
					if (i==j && j!=k)
						s+=(f[a0][a1]*(f[a0][a1]-1)/2)*f[c0][c1];
					else
					if (i!=j && j==k)
						s+=f[a0][a1]*(f[b0][b1]*(f[b0][b1]-1)/2);
					else
						s+=f[a0][a1]*(f[a0][a1]-1)*(f[a0][a1]-2)/6;
				}
					
			}
	printf("%I64d\n", s);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas=0, t;
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	
	return 0;
}

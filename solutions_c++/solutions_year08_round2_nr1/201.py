#include <cstdio>
#include <vector>

using namespace std;

typedef struct _data
{
	long long x, y;
} Dat;

vector <Dat> tree;
long long dynamic[3][100000][3][3];

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int q=1;q<=T;q++)
	{
		tree.clear();
		memset(dynamic, 0, sizeof(dynamic));

		long long n, A, B, C, D, x, y, M;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x ,&y, &M);
		for(int i=0;i<n;i++)
		{
			Dat temp;
			temp.x=x, temp.y=y;
			tree.push_back(temp);
			x=(A*x+B)%M;
			y=(C*y+D)%M;
		}

		for(int i=0;i<n;i++) 
		{
			if(i!=0) for(int j=0;j<3;j++) for(int k=0;k<3;k++) dynamic[0][i][j][k]+=dynamic[0][i-1][j][k];
			dynamic[0][i][tree[i].x%3][tree[i].y%3]++;
		}

		for(int i=1;i<n;i++)
		{
			for(int j=0;j<3;j++) for(int k=0;k<3;k++) 
			{
				dynamic[1][i][j][k]+=dynamic[1][i-1][j][k];								
				dynamic[1][i][(j+tree[i].x)%3][(k+tree[i].y)%3]+=dynamic[0][i-1][j][k];
			}
		}

		for(int i=2;i<n;i++)
		{
			for(int j=0;j<3;j++) for(int k=0;k<3;k++)
			{
				dynamic[2][i][j][k]+=dynamic[2][i-1][j][k];
				dynamic[2][i][(j+tree[i].x)%3][(k+tree[i].y)%3]+=dynamic[1][i-1][j][k];								
			}
		}		

		printf("Case #%d: %lld\n", q, dynamic[2][n-1][0][0]);
	}
	return 0;
}
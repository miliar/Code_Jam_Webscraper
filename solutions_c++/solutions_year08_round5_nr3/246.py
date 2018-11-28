#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <boost/foreach.hpp>

using namespace std;
using namespace boost;

int X, Y;
char MAP[100][100];
int DP[100][1055];

bool isval( int row, int n){
	int pre = 0;
	int a;
	for(int i=0;i<X;i++){
		a = n & 0x01;
		if( a + pre == 2)
			return false;
		if( a == 1 && MAP[i+1][row] == 'x')
			return false;
		pre = a;
		n >>= 1;
	}
	return true;
}
int countMan(int n)
{
	int sum = 0;
	for(int i=0;i<X;i++){
		sum += n & 0x01;
		n >>= 1;
	}
	return sum;
}
bool isconval( int n, int m){
	int bb[100] = {0};
	int *cc;
	cc = bb+2;
	for(int i=0;i<X;i++){
		cc[i] = m & 0x01;
		m >>= 1;
	}
	for(int i=0;i<X;i++){
		int a = n & 0x01;
		n >>= 1;
		if( a == 0)
			continue;
		if( cc[i-1] == 1 || cc[i+1] == 1)
			return false;
	}
	return true;
}
int main()
{
	int caseN;

	scanf("%d", &caseN);
	for(int cc=0; cc<caseN;cc++){
		scanf("%d%d\n", &Y, &X);
		for(int i=1;i<=Y;i++){
			for(int j=1;j<=X;j++){
				scanf(" %c ", &MAP[j][i]);
			}
		}
		int count = 1 << X;
		memset(DP, 0, sizeof(DP));
		for(int y=1;y<=Y;y++){
			for(int i=0;i<count;i++){
				if( isval(y,i) == false)
					continue;
				for(int j=0;j<count;j++){
					if( isconval( i, j) )
						DP[y][i] = max(DP[y][i], DP[y-1][j] + countMan(i));
				}
			}
		}
		/*
		for(int y=1;y<=Y;y++){
			for(int i=0;i<count;i++){
				printf("%3d", DP[y][i]);
			}
			printf("\n");
		}
		*/
		int ans = 0;
		for(int i=0;i<count;i++)
			ans = max( ans, DP[Y][i]);
		printf("Case #%d: %d\n", cc+1, ans);
	}
	return 0;
}

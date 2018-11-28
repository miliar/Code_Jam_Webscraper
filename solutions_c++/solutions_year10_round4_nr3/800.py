#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int test, p;
int a[101][101], b[101][101];
int xx1, xx2, yy1, yy2;

bool check()
{
	for (int i = 1; i <= 100; i++)
		for (int j = 1; j <= 100; j++)
			if (a[i][j]==1) return false;
	return true;
}

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%i", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%i: ",tt);
		scanf("%i", &p);

		for (int i = 0; i <= 100; i++)
			for (int j = 0; j <= 100; j++)
				a[i][j] = 0;

		for (int i = 0; i < p; i++) {
			scanf("%i %i %i %i", &xx1, &yy1, &xx2, &yy2);

			for (int j = yy1; j <= yy2; j++)
				for (int k = xx1; k <= xx2; k++)
					a[j][k]=1;
		}
		
		int sum = 0;
		while (!check()) {
			sum++;
			for (int i = 1; i <= 100; i++)
				for (int j = 1; j <= 100; j++)
					if (a[i-1][j]==1 && a[i][j-1]==1) b[i][j]=1;
					else if (a[i-1][j]==0 && a[i][j-1]==0) b[i][j]=0;
					else b[i][j]=a[i][j];

			for (int i = 1; i <= 100; i++)
				for (int j = 1; j <= 100; j++)
					a[i][j]=b[i][j];
		}
		printf("%i\n",sum);
	}

	return 0;
}
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

struct tmas{int x,y;};

bool fun(tmas a, tmas b)
{
	return a.x < b.x;
}

int test, p, c;
int a[11];
tmas b[2000];
bool fl[11][2000];

int solve(int miss, int num, int row)
{
	if (fl[row][num]) return 0;
	fl[row][num]=1;
	if (row == p-1) 
		return (miss==0);
	if (miss>0) return solve(miss-1, num/2, row+1);
	else return solve(0, num/2, row+1)+1;
}

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	a[0] = 1;
	for (int i = 1; i <= 10; i++)
		a[i] = a[i-1]*2;

	scanf("%i", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%i: ",tt);
		scanf("%i", &p);
		for (int i = 0; i < a[p]; i++) {
			scanf("%i", &b[i].x);
			b[i].y = i;
		}
		for (int i = 0; i < p; i++)
			for (int j = 0; j < a[p-i-1]; j++) {
				scanf("%i", &c);
				fl[i][j] = 0;
			}

		sort(b,b+a[p],fun);

		int sum = 0;
		for (int i = 0; i < a[p]; i++) 
			sum += solve(b[i].x, b[i].y/2, 0);
		
		printf("%i\n",sum);
	}

	return 0;
}
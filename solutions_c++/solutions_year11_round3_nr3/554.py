#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 1000
#define BIT(x) (1<<(x-1))
using namespace std;
#define min(a,b) (((a) < (b)) ? (a) : (b))
int num[MAX];
int N;
int L,H;
int flag;
void readdata()
{
	int i;
	flag = 0;
	scanf("%d%d%d", &N, &L, &H);
	for (i=0; i<N; ++i) {
		scanf("%d", &num[i]);
	}
}

void solve()
{
	int i,j;
	int n;
	for (i = L; i<=H; ++i) {
		
		for (j=0; j<N; ++j) {
			if (i > num[j]) {
				if (i % num[j] != 0)
					break;
			} else {
				if (num[j] % i != 0)
					break;
			}
		}
		if (j == N) {
			flag = i;
			break;
		}
	}

}

void output()
{
	if (flag == 0)
		printf("NO\n");
	else
		printf("%d\n", flag);
}
int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("small.out", "w", stdout);
	int nt, it;
	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		readdata();
		solve();
		printf("Case #%d: ",it);
		output();
		
	}
	return 0;
}
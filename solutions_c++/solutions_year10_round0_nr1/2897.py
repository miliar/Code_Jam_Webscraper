#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int n, k;
bool isOn;
int ans;

void determine()
{
	ans = k % (int) pow(2, n);
	isOn = ans == pow(2,n) - 1;
}

int main()
{
	int t, nCase = 0;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
	{
		isOn = false;
		scanf("%d %d", &n, &k);
		determine();
		if(isOn) printf("Case #%d: ON\n", ++nCase);
		else printf("Case #%d: OFF\n", ++nCase);
	}
}

#include <iostream>
#include <algorithm>
using namespace std;

bool p[105];
int q[105];
int ans = 0x7777777;
int P, Q;

int getm(int pos)
{
	int res = 0;
	int i = pos-1;
	while(i >= 0 && !p[i]) {
		res++;
		i--;
	}
	i = pos+1;
	while(i < P && !p[i])
	{
		res++;
		i++;
	}
	return res;
}

void work()
{
	int qq[105];
	for(int i = 0; i < Q; i++)
	{
		qq[i] = i;
	}
	do
	{
		memset(p, false, sizeof(p));
		int tmp = 0;
		for(int i = 0; i < Q; i++)
		{
			p[q[qq[i]]] = true;
			tmp += getm(q[qq[i]]);
		}
		if(tmp < ans) ans = tmp;
		
	}while(next_permutation(qq, qq+Q));
}

int main()
{
	int tcase;
	freopen("cin.txt", "r", stdin);
	freopen("cout.txt", "w", stdout);
	scanf("%d", &tcase);
	for(int t = 1; t <= tcase; t++)
	{
		scanf("%d%d", &P, &Q);
		for(int i = 0; i < Q; i++) 
		{
			scanf("%d", &q[i]);
			q[i]--;
		}
		ans = 0x7777777;
		work();
		printf("Case #%d: %d\n",t,  ans);
	}
	return 0;
}

/***

45
8 1
3
20 3
3 6 14

*/

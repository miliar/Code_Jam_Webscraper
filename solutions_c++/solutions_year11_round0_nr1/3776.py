#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define MAX 105
struct OP
{
	int index;
	int button;
};
OP a[MAX], b[MAX];
int ca, cb;
int posa, posb;
int n, ans;

void solve()
{
	int cnt = 1;
	int ia, ib;
	ia = ib = 0;
	while(cnt <= n)
	{
		int add;
		if(a[ia].index == cnt)
		{
			add = abs(posa - a[ia].button) + 1;
			ans += add;
			posa = a[ia].button;
			cnt++;
			ia++;
			int tmp = abs(posb - b[ib].button);
			if(tmp <= add)
			{
				posb = b[ib].button;
			}
			else 
			{
				if(posb < b[ib].button)
					posb += add;
				else posb -= add;
			}
		}
		else
		{
			add = abs(posb - b[ib].button) + 1;
			posb = b[ib].button;
			ans += add;
			cnt++;
			ib++;
			int tmp = abs(posa - a[ia].button);
			if(tmp <= add)
				posa = a[ia].button;
			else
			{
				if(posa < a[ia].button)
					posa += add;
				else posa -= add;
			}
		}
	}
}
int main(void)
{
	int cas;
	freopen("A-large.in", "r", stdin);
	freopen("A-small-attempt3.out", "w", stdout);
	scanf("%d", &cas);
	int t;
	for(t = 1; t <= cas; t++)
	{
		scanf("%d", &n);
		int i, j;
		for(i = 0; i <= n; i++)
			a[i].index = -1, b[i].index = -1;
		posa = posb = 1;
		ca = cb = ans = 0;
		for(i = 1; i <= n; i++)
		{
			char ch;
			int button;
			scanf("\n%c %d", &ch, &button);
			if(ch == 'O')
			{
				a[ca].index = i;
				a[ca++].button = button;
			}
			else 
			{
				b[cb].index = i;
				b[cb++].button = button;
			}
		}
		solve();
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
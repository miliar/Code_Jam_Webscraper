#include<iostream>
#include<algorithm>
#include<functional>
using namespace std;

#define MAXN 31

int T, N, S, p;
int t[MAXN];

int ans;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d\n", &T);
	for(int te=1;te<=T;++te)
	{
		scanf("%d %d %d", &N, &S, &p);
		for(int i=0;i<N;++i)
		{
			scanf("%d", t+i);
		}
		sort(t, t+N, greater<int>());
		ans = 0;
		for(int i=0;i<N;++i)
		{
			if(t[i]<3*p-4)
			{
				break;
			}
			if(t[i]/3>=p)
			{
				ans++;
				continue;
			}
			if(p-1>=0 && t[i]>=max(3*p-2, 0))
			{
				ans++;
				continue;
			}
			if(p-2>=0 && S>0)
			{
				S--;
				ans++;
				continue;
			}
		}
		printf("Case #%d: %d\n", te, ans);
	}
	return 0;
}

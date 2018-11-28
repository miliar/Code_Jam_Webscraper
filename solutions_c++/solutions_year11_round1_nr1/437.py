#include <cstdio>
#include <iostream>

using namespace std;
long long n,gd,gn;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int N;
	scanf("%d",&N);
	for (int I=1;I<=N;++I)
	{
		cin>>n>>gd>>gn;
		if (gn==100 && gd!=100 || gn==0 && gd!=0)
		{
			printf("Case #%d: Broken\n", I);
			continue;
		}
		if (n>=100)
		{
			printf("Case #%d: Possible\n", I);
			continue;
		}
		bool done=false;
		for (int i=1;i<=n && i<=100; ++i)
		{
			int j=i*gd/100;
			if (j*100==i*gd)
				done=true;
		}
		if (done)
			printf("Case #%d: Possible\n", I);
		else
			printf("Case #%d: Broken\n", I);
	}
	return 0;
}

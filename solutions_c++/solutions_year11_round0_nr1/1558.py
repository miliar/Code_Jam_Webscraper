#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;

int T, N;
string R[200];
int P[200];

int i, j, k;

int calc()
{
	int ans=0;
	int to,tb;
	int po,pb;
	int dt;
	to = tb = 0;
	po = pb = 1;

	for(int i=0;i<N;i++)
	{
		if(R[i] == string("O"))
		{
			dt = abs(P[i] - po);
			if(to < tb)
				dt = dt > (tb - to) ? dt + to - tb : 0;

			ans += dt + 1;
			to = ans;
			po = P[i];
		}
		else
		{
			dt = abs(P[i] - pb);
			if(tb < to)
				dt = dt > (to - tb) ? dt + tb - to : 0;

			ans += dt + 1;
			tb = ans;
			pb = P[i];
		}
	}
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for( k = 1; k <= T; k++ )
	{
		scanf("%d",&N);
		for( i = 0; i < N; i++ )
		{
			cin>>R[i]>>P[i];
		}

		printf("Case #%d: ",k);
		printf("%d\n",calc());
	}
	return 0;
}
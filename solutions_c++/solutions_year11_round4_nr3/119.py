#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;
#define oo 1000005
bool mk [oo];
long long N;
int M;
int Q,q[oo];

inline void Readin()
{
	cin >> N;
}

inline void Prepare()
{
	for (int i=2;i<=1000001;++i)
		if (!mk[i])
		{
			q[++Q]=i;
			for (int j=i+i;j<=1000001;j+=i)
				mk[j]=true;
		}
}

inline void Solve()
{
	int ans=0;
	
	for (int i=1;i<=Q;++i)
		if (q[i]*(long long)q[i] > N) break;
		else{
			long long t = q[i]*(long long)q[i];
			while (t <= N)
			{
				t*=q[i];
				++ans;
			}
		}
	
	printf("%d\n",ans + (N>1));
}

int main()
{
	//freopen("i.txt","r",stdin);

	int Test,Case = 0;
	Prepare();
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	return 0;
}

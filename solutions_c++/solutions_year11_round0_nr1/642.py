#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<stack>
#include<list>

using namespace std;
int T;

int n;
char cnum[1000];
int num[1000];
int pto,ptb,pt;
int poso,posb;

void solve()
{
	pto = ptb = pt = 1;
	poso = posb = 1;
	int ans = 0;
	while(cnum[pto] != 'O' && pto <= n)
		pto++;
	while(cnum[ptb] != 'B' && pto <= n)
		ptb++;
	while(pt <= n)
	{
		ans++;

		int npt = pt;
		if(pto <= n)
		{
			if(poso == num[pto])
			{
				if(pto == pt)
				{
					pto++;
					while(cnum[pto] != 'O' && pto <= n)
						pto++;
					npt++;
				}
			}
			else
			{
				if(num[pto] > poso)poso++;
				else poso--;
			}
		}
		
		if(ptb <= n)
		{
			if(posb == num[ptb])
			{
				if(ptb == pt)
				{
					ptb++;
					while(cnum[ptb] != 'B' && ptb <= n)
						ptb++;
					npt++;
				}
			}
			else
			{
				if(num[ptb] < posb)posb--;
				else posb++;
			}
		}
		pt = npt;
	}
	cout<<ans<<endl;
}

int main()
{
	freopen("f:\\GJ\\in.txt","r",stdin);
	freopen("f:\\GJ\\out.txt","w",stdout);

////////////////////////////////////////////////////////////////////

	cin>>T;
	int cases;
	for(cases = 1;cases <= T;cases++)
	{
		printf("Case #%d: ",cases);
		cin>>n;
		for(int i = 1;i <= n;i++)
			cin>>cnum[i]>>num[i];
		solve();
	}

////////////////////////////////////////////////////////////////////

	fclose(stdout);	
	return 0;
}
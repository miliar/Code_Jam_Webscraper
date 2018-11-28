#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef long long int lli;
class freecellstatistics
{
	private:
		lli n;
		int pd,pg;
		bool sol;
		bool _solve()
		{
			if((pd<100)&&(pg==100)) return false;
			if((pd>0)&&(pg==0)) return false;
			lli d1;
			if(pd<=pg)
			{
				for(d1=n;d1>0;--d1)
				{
					if((d1*pd)%100==0)
					{
						return true;
					}
				}
				return false;
			}
			else
			{
				for(d1=1;d1<=n;++d1)
				{
					if((d1*pd)%100==0)
					{
						return true;
					}
				}
				return false;
			}
		}
	public:
		freecellstatistics() {}
		void input()
		{
			scanf("%lld%d%d",&n,&pd,&pg);
		}
		void solve()
		{
			sol=_solve();
		}
		void output(int caseno)
		{
			printf("Case #%d: %s\n",caseno,(sol?"Possible":"Broken"));
		}
};
int main(void)
{
	int nt;
	scanf("%d",&nt);
	for(int znj=1;znj<=nt;++znj)
	{
		freecellstatistics task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}

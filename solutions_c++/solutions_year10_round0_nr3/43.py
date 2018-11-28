#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
typedef long long int lli;
const int inf=0x3f3f3f3f;
const double ERR=1e-9;
class themepark
{
	private:
		int r,cap,n;
		vector<int> gs;
	public:
		themepark() {}
		void input()
		{
			scanf("%d%d%d",&r,&cap,&n);
			gs.resize(n);
			for(int f=0;f<n;++f)
			{
				scanf("%d",&(gs.at(f)));
			}
		}
		lli solve()
		{
			lli sol=0l;
			vector<bool> vis(n,false);
			vector<lli> lsol(n,0l);
			vector<int> lit(n,0);
			int lgi=0;
			for(int z=0;z<r;++z)
			{
				if(vis.at(lgi))
				{
					vis.clear();
					vis.resize(n,false);
					int rrs=(r-z)/(z-lit.at(lgi));
					z+=rrs*(z-lit.at(lgi));
					sol+=rrs*(sol-lsol.at(lgi));
				}
				if(z<r)
				{
					vis.at(lgi)=true;
					lsol.at(lgi)=sol;
					lit.at(lgi)=z;
					lli cc=0l;
					for(int gc=0;(cc+gs.at(lgi)<=cap)&&(gc<n);lgi=(lgi+1)%n,++gc)
					{
						cc+=gs.at(lgi);
					}
					sol+=cc;
				}
			}
			return sol;
		}
};
int main(void)
{
	int znj;
	scanf("%d",&znj);
	for(int i=0;i<znj;++i)
	{
		themepark task;
		task.input();
		printf("Case #%d: %lld\n",i+1,task.solve());
	}
	return 0;
}

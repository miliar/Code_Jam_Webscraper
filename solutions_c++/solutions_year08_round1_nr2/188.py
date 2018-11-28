#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define NMAX 2000
#define MMAX 2000

int like1[MMAX];
set<int> like0[MMAX];
short sol[NMAX];
int n,m;

bool solve()
{
	memset(sol,-1,sizeof(sol));

	while(true)
	{
		bool bm=false;
		for(int i=0;i<m;i++)
		{
			if(like0[i].empty())
			{
				if(like1[i]==-1) return false;
				if(like1[i]!=-2)
				{
					sol[like1[i]]=1;
					for(int ii=0;ii<m;ii++)
					{
						like0[ii].erase(like1[i]);
					}
					like1[i]=-2;
					bm=true;
				}
			}
		}

		if(!bm)
		{
			for(int j=0;j<n;j++) if(sol[j]==-1) sol[j]=0;
			return true;
		}
	}
}

int main()
{
	int cc;
	cin>>cc;
	for(int ci=1;ci<=cc;ci++)
	{
		cin>>n>>m;
		int et;
		memset(like1,-1,sizeof(like1));

		int i;
		for(i=0;i<m;i++)
		{
			like0[i].clear();
			cin>>et;
			int ej,ef;
			while(et--)
			{
				cin>>ej>>ef;
				if(ef==1) like1[i]=ej-1;
				else like0[i].insert(ej-1);
			}
		}

		bool br=solve();

		cout<<"Case #"<<ci<<":";
		if(!br) cout<<" IMPOSSIBLE"<<endl;
		else
		{
			for(i=0;i<n;i++) cout<<" "<<sol[i];
			cout<<endl;
		}
	}

	return 0;
}

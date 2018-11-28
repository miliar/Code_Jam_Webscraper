#include <stdio.h>
#include <vector>
using namespace std;
vector<vector<pair<int,int> > > req;
vector<int> meth;
vector<bool> meet;
vector<int> pos1;
int N,M;
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	int T,nT;
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d%d",&N,&M);
		meth.clear();
		meth.assign(N,0);
		meet.clear();
		meet.assign(M,false);
		pos1.clear();
		pos1.assign(M,-1);
		int i,P,j,a,b;
		req.clear();
		for (i=0;i<M;i++)
		{
			req.push_back(vector<pair<int,int> >());
			scanf("%d",&P);
			for (j=0;j<P;j++)
			{
				scanf("%d%d",&a,&b);
				a--;
				req[i].push_back(make_pair(a,b));
				if (b==1)
					pos1[i]=a;
			}
			if (P==0)
				if (req[i][0].second==1)
				{
					meth[req[i][0].first]=1;
					meet[i]=true;
				}
		}
		bool gsat=false;
		while (!gsat)
		{
			gsat=true;
			bool nsat;
			for (i=0;i<M;i++) if (!meet[i])
			{
				nsat=false;
				for (j=0;j<req[i].size();j++)
					if (meth[req[i][j].first]==req[i][j].second)
					{
						nsat=true;
						break;
					}
				if (!nsat)
				{
					gsat=false;
					if (pos1[i]==-1)
						goto endw;
					meth[pos1[i]]=1;
				}
			}
		}
endw:
		printf("Case #%d:",nT-T);
		if (gsat)
		{
			for (i=0;i<N;i++) printf(" %d",meth[i]);
			printf("\n");
		}
		else
			printf(" IMPOSSIBLE\n");
	}
	fclose(stdin);
	fclose(stdout);
}
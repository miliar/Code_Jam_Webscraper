#include<iostream>
#include<vector>
using namespace std;
int dh[]={-1,0,0,1};
int dw[]={0,-1,1,0};
int visit[109][109];
int sink[109][109];
int to[109][109];
char ans[40009];
vector<pair<int,int> > next[109][109];
int h,w;
void dfs(int i,int j,int val)
{//cout<<i<<" "<<j<<"---------"<<val<<" "<<next[i][j].size()<<endl;
	to[i][j]=val;
	visit[i][j]=1;
	int k;
	for(k=0;k<next[i][j].size();k++)
	{
		pair<int,int> t=next[i][j][k];
		if(visit[t.first][t.second]==0)
			dfs(t.first,t.second,val);
	}
}
int main()
{
	int T,ca=0;
	freopen("B-large.in","r",stdin);
	freopen("Big_b.out","w",stdout);
	scanf("%d",&T);
	while(T-->0)
	{
		scanf("%d%d",&h,&w);
		int v[109][109];
		memset(visit,0,sizeof (visit));
		
		int i,j,k,d,th,tw;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				next[i][j].clear();
		memset(sink,-1,sizeof (sink));
		ca++;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				scanf("%d",&v[i][j]);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				int ta=-1,tb=-1;
				int tv=v[i][j];
				int val=v[i][j];
				for(d=0;d<4;d++)
				{
					th=i+dh[d];
					tw=j+dw[d];
					if(th>=0&&th<h&&tw>=0&&tw<w)
					{
						if(v[th][tw]<val)
						{
							val=v[th][tw];
							ta=th;
							tb=tw;
						}
					}
				}
				if(ta==-1)
					continue;
				//cout<<ta<<" "<<tb<<" "<<i<<"!!!!!!!!!!"<<j<<endl;
				next[ta][tb].push_back(make_pair(i,j));
			//	for(int aa=0;aa<next[ta][tb].size();aa++)
			//		cout<<aa<<"++++++++++"<<next[ta][tb][aa].first<<" "<<next[ta][tb][aa].second<<endl;
				sink[i][j]=0;
			}
		int now=0;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				if(visit[i][j]==0&&sink[i][j]==-1)
					dfs(i,j,now++);
			}
	//	cout<<"--------1"<<endl;
		memset(ans,0,sizeof (ans));
		char start='a';
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				if(ans[to[i][j]]==0)
				{
					ans[to[i][j]]=start;
					start++;
				}
			}
		printf("Case #%d:\n",ca);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(j>0)
					printf(" ");
				printf("%c",ans[to[i][j]]);
			}
			printf("\n");
		}
	}
//	while(3);
}

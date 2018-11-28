# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

int S,M;

bool isgood(int x,int y)
{
	if(x<1||x>=S*2)return false;
	if(x<=S)return ((y>0)&&(y<S+x));
	else return ((y<S*2)&&((x-y)<S));
}

map<int,int>piecemap;
int neigh[][2]={{-1,-1},{-1,0},{0,1},{1,1},{1,0},{0,-1}};

int findparent(int u)
{
	if(piecemap[u]==u)return u;
	return(piecemap[u]=findparent(piecemap[u]));
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d%d",&S,&M);
		bool flag=false;

		piecemap.clear();
		int corners[][2]={{1,1},{1,S},{S,2*S-1},{2*S-1,2*S-1},{2*S-1,S},{S,1}};
		int req=3*S*S-3*S+1;
		bool bridge=false,fork=false,ring=false;
		
		for(int m=1;m<=M;m++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			
			if(flag)continue;
			
			int u=a*1000+b;
			piecemap[u]=u;
			
			for(int i=0;i<6;i++)
			{
				int aa=a+neigh[i][0],bb=b+neigh[i][1];
				if(!isgood(aa,bb))continue;
				int v=aa*1000+bb;
				if(piecemap.count(v)==0)continue;
				piecemap[findparent(u)]=findparent(v);
			}
			
			for(int i=1;i<6;i++)
			{
				int u=corners[i][0]*1000+corners[i][1];
				if(piecemap.count(u)==0)continue;
				for(int j=0;j<i;j++)
				{
					int v=corners[j][0]*1000+corners[j][1];
					if(piecemap.count(v)==0)continue;
					if(findparent(u)==findparent(v)){bridge=true;goto BPP1;}
				}
			}
			
			BPP1:
			
			map<int,int>forkmap;set<int>edgeforkset;set<int>::iterator sit;
			forkmap.clear();
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=1000+i;
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=i*1000+(i+S-1);
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=(S+i-1)*1000+(2*S-1);
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=(2*S-1)*1000+(S+i-1);
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=(i+S-1)*1000+i;
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			edgeforkset.clear();
			for(int i=2;i<S;i++)
			{
				int u=i*1000+1;
				if(piecemap.count(u))edgeforkset.insert(findparent(u));
			}
			for(sit=edgeforkset.begin();sit!=edgeforkset.end();sit++)
			{
				int u=*sit;
				if(forkmap.count(u))forkmap[u]++;
				else forkmap[u]=1;
				if(forkmap[u]==3){fork=true;goto BPP2;}
			}
			
			BPP2:
			
			char seen[120000];
			for(int i=0;i<120000;i++)seen[i]=0;
			queue<int>bfsqueue;
			while(!bfsqueue.empty())bfsqueue.pop();
			int tot=0;
			
			for(int i=1;i<=S;i++)
			{
				int u=1000+i;
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
				u=i*1000+(i+S-1);
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
				u=(S+i-1)*1000+(2*S-1);
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
				u=(2*S-1)*1000+(S+i-1);
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
				u=(i+S-1)*1000+i;
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
				u=i*1000+1;
				if((!seen[u])&&(piecemap.count(u)==0))seen[u]=true,bfsqueue.push(u),tot++;
			}
			
			while(!bfsqueue.empty())
			{
				u=bfsqueue.front();bfsqueue.pop();
				int a=u/1000,b=u%1000;
				for(int i=0;i<6;i++)
				{
					int aa=a+neigh[i][0],bb=b+neigh[i][1];
					if(!isgood(aa,bb))continue;
					int v=aa*1000+bb;
					if((seen[v]==true)||(piecemap.count(v)!=0))continue;
					seen[v]=true,bfsqueue.push(v),tot++;
				}
			}
			
			if(tot+m!=req)ring=true;
			
			if(bridge||fork||ring)
			{
				flag=true;
				if(bridge&&fork&&ring)printf("Case #%d: bridge-fork-ring in move %d\n",t,m);
				else if(bridge&&fork)printf("Case #%d: bridge-fork in move %d\n",t,m);
				else if(bridge&&ring)printf("Case #%d: bridge-ring in move %d\n",t,m);
				else if(fork&&ring)printf("Case #%d: fork-ring in move %d\n",t,m);
				else if(bridge)printf("Case #%d: bridge in move %d\n",t,m);
				else if(fork)printf("Case #%d: fork in move %d\n",t,m);
				else if(ring)printf("Case #%d: ring in move %d\n",t,m);
			}
		}
		
		if(!(bridge||fork||ring))printf("Case #%d: none\n",t);
	}
	return 0;
}

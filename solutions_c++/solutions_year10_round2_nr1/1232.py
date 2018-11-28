#include<iostream>
#include<cstring>
#include<vector>
#include<map>

using namespace std;
vector<int> zz[240];
class ts
{
public:
	char ch[50];
	int s;
	bool operator<(const ts &b)const
	{
		int a=s;
		if(b.s<s)
			a=b.s;
		int i;
		for(i=0;i<a;i++)
			if(ch[i]!=b.ch[i])
				break;
			return ch[i]<b.ch[i];
	}
	void set()
	{
		s=strlen(ch);
	}
};
char ch[120];
map<ts,int> pp;
int main()
{
//	freopen("C:\\as.txt",r,stdin);
	freopen("C:\\out.txt","w",stdout);
	int cas;
	int n,m,s,s1,u,t;
	cin>>cas;
	int cc=0;
	while(cas--)
	{
		cc++;
          pp.clear();
		scanf("%d %d",&n,&m);
		int i,j,k;
		for(i=0;i<=n+m;i++)
          zz[i].clear();
		ts tem;
		int ind=0;
		for(i=1;i<=n;i++)
		{
			scanf("%s",ch);
			s=strlen(ch);

			for(j=0;j<s;j++)
			{
				if(ch[j]=='/')
				{
					k=j+1;
					u=0;
					while(ch[k]&&ch[k]!='/')
					{

						tem.ch[u++]=ch[k];
						k++;
					}
					tem.ch[u]=0;
					tem.set();
					t=pp[tem];
					if(t==0)
					{
                     t=pp[tem]=++ind;
					}
					 zz[i].push_back(t);
					j=k-1;
				}
			}
		}


		int key=0;
		for(i=1;i<=m;i++)
		{
			
		  scanf("%s",ch);
		  s=strlen(ch);
		  	for(j=0;j<s;j++)
			{
				if(ch[j]=='/')
				{
					k=j+1;
					u=0;
					while(ch[k]&&ch[k]!='/')
					{

						tem.ch[u++]=ch[k];
						k++;
					}
	            tem.ch[u]=0;
					tem.set();
					t=pp[tem];
					if(t==0)
					{
                     t=pp[tem]=++ind;
					}
					 zz[n+i].push_back(t);
					j=k-1;
				}
			}
			k=n+i;
			int inf=zz[k].size();
			for(j=1;j<k;j++)
			{
				for(u=0;u<zz[j].size()&&u<zz[k].size();u++)
					if(zz[j][u]!=zz[k][u])
						break;
					if(inf>zz[k].size()-u)
						inf=zz[k].size()-u;
			}
			key+=inf;
		}
		printf("Case #%d: %d\n",cc,key);

	}
	return 0;
}


 

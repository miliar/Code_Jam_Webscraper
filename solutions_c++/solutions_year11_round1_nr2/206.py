#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
long long m,n,tt;
int num[1010];
struct gg
{
	char c[20];
	int id;
};
gg tp;
char d[30];
vector <gg> g[20];
bool use[200][20];
bool nouse[200];
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>n>>m;
		for (int i=0;i<20;++i)
		{
			g[i].clear();
		}
		printf("Case #%d: ",kk);
		for (int aa=1;aa<=n;++aa)
		{
			cin>>tp.c;
			tp.id=aa;
			int len=strlen(tp.c);
			g[len].push_back(tp);
		}		
		for (int aa=1;aa<=m;++aa)
		{
			cin>>d;
			int ans=-1,tpans;
			string ans1;
			for (int i=0;i<=15;++i)
			{
				if (g[i].size()==0)
				{
					continue;
				}
				else if (g[i].size()==1)
				{
					if (ans<0)
					{
						ans=0;
						ans1=g[i][0].c;
						tpans=g[i][0].id;
					}
					else if (ans==0 && tpans>g[i][0].id)
					{
						ans1=g[i][0].c;
						tpans=g[i][0].id;
					}
				}
				else
				{
					string aim;
					int tid;
					for (int bb=0;bb<g[i].size();++bb)
					{					
						int t=0;						
						memset(nouse,0,sizeof(nouse));
						int rest[200];
						memset(rest,0,sizeof(rest));
						for (int j=0;j<g[i].size();++j)
						{
							for (int k=0;k<i;++k)
							{
								rest[g[i][j].c[k]]=1;
							}
						}
						for (int j=0;j<26;++j)
						{
							char ch=d[j];
							if (!rest[ch])
							{
								continue;
							}
							int f=0;
							vector<int> p[200];
							for (int k=0;k<g[i].size();++k)
							{
								if (!nouse[k])
								{
									for (int l=0;l<i;++l)
									{
										if (g[i][k].c[l]==ch)
										{
											p[k].push_back(l);
										}
									}
								}								
							}
							for (int k=0;k<g[i].size();++k)
							{
								if (p[k].size()==p[bb].size())
								{
									for (int q=0;q<p[k].size();++q)
									{
										if (p[k][q]!=p[bb][q])
										{
											nouse[k]=1;
											break;
										}
									}
								}
								else
								{
									nouse[k]=1;
								}
							}
							if (p[bb].size()==0)
							{
								t++;
							}
							memset(rest,0,sizeof(rest));
							int ta=0;
							for (int l=0;l<g[i].size();++l)
							{
								if (!nouse[l])
								{
									ta++;
									for (int k=0;k<i;++k)
									{
										rest[g[i][l].c[k]]=1;
									}
								}								
							}
							if (ta==1)
							{
								break;
							}
						}
						if (ans<t)
						{
							ans=t;
							ans1=g[i][bb].c;
							tpans=g[i][bb].id;
						}
						else if (ans==t && tpans>g[i][bb].id)
						{
							ans1=g[i][bb].c;
							tpans=g[i][bb].id;
						}


					}
					
				}
				
			}
			if (aa!=m)
			{
				cout<<ans1<<" ";
			}
			else
			{
				cout<<ans1<<endl;
			}
		}	
	}	
	return 0;	
}
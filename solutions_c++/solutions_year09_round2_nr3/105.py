#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<queue>
using namespace std;
struct dat{
	int x,y;
}dir[4]={{0,1},{0,-1},{1,0},{-1,0}};
struct data{
	int x,y,sum;
	string s;
};
string ans[60];
int need[60],w;
bool nd[60],is[11][11][400][20];
string ss[11][11][400][20];
char c[30][30],tt[10];
bool ok(int x,int y)
{
	if(x>=0&&x<w&&y>=0&&y<w)
		return true;
	return false;
}
int main()
{
	int cas,dd=0,Q,cnt,i,j,lim;
	queue<data> q;
	data now,t,t2;
	scanf("%d",&cas);
	while(dd<cas)
	{
		scanf("%d%d",&w,&Q);
		memset(nd,0,sizeof(nd));
		memset(is,0,sizeof(is));
		lim=999999;
		for(i=0;i<=50;i++)
			ans[i]="";
		for(i=0;i<w;i++)
			scanf("%s",c[i]);
		for(cnt=i=0;i<Q;i++)
		{
			scanf("%d",&need[i]);
			if(!nd[need[i]])
			{
				nd[need[i]]=true;
				cnt++;
			}
		}
		for(i=0;i<w;i++)
			for(j=0;j<w;j++)
				if(c[i][j]!='-'&&c[i][j]!='+')
				{
					t.x=i;
					t.y=j;
					t.sum=c[i][j]-'0';
					tt[0]=c[i][j];
					t.s=(string)tt;
					q.push(t);
					is[t.x][t.y][t.sum+200][t.s.size()/2]=true;
					ss[t.x][t.y][t.sum+200][t.s.size()/2]=t.s;
					if(nd[t.sum])
					{
						if(ans[t.sum].size()==0)
						{
							cnt--;
							ans[t.sum]=t.s;
						}
						else if(ans[t.sum]>t.s)
							ans[t.sum]=t.s;
					}
				}
		while(!q.empty())
		{
			now=q.front();
			q.pop();
			if(ss[now.x][now.y][now.sum+200][now.s.size()/2]!=now.s)
				continue;
			for(i=0;i<4;i++)
				if(ok(now.x+dir[i].x,now.y+dir[i].y))
				{
					t=now;
					t.x=now.x+dir[i].x;
					t.y=now.y+dir[i].y;
					tt[0]=c[t.x][t.y];
					t.s+=string(tt);
					if(c[t.x][t.y]=='+')
					{
						for(j=0;j<4;j++)
							if(ok(t.x+dir[j].x,t.y+dir[j].y))
							{
								t2=t;
								t2.x=t.x+dir[j].x;
								t2.y=t.y+dir[j].y;
								tt[0]=c[t2.x][t2.y];
								t2.s+=string(tt);
								t2.sum=t.sum+c[t2.x][t2.y]-'0';
								if(t2.sum>0&&nd[t2.sum])
								{
									if(ans[t2.sum].size()==0)
									{
										cnt--;
										ans[t2.sum]=t2.s;
										if(cnt==0)
											lim=t2.s.size();
									}
									else if(ans[t2.sum].size()>t2.s.size())
										ans[t2.sum]=t2.s;
									else if(ans[t2.sum].size()==t2.s.size()&&ans[t2.sum]>t2.s)
										ans[t2.sum]=t2.s;
								}
								if(t2.s.size()<=lim)
								{
									if(!is[t2.x][t2.y][t2.sum+200][t2.s.size()/2])
									{
										is[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=true;
										ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=t2.s;
										q.push(t2);
									}
									else
									{
										if(t2.s<ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2])
										{
											ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=t2.s;
											q.push(t2);
										}
									}
								}
							}
					}
					else if(c[t.x][t.y]=='-')
					{
						for(j=0;j<4;j++)
							if(ok(t.x+dir[j].x,t.y+dir[j].y))
							{
								t2=t;
								t2.x=t.x+dir[j].x;
								t2.y=t.y+dir[j].y;
								tt[0]=c[t2.x][t2.y];
								t2.s+=string(tt);
								t2.sum=t.sum-c[t2.x][t2.y]+'0';
								if(t2.sum>0&&nd[t2.sum])
								{
									if(ans[t2.sum].size()==0)
									{
										cnt--;
										ans[t2.sum]=t2.s;
										if(cnt==0)
											lim=t2.s.size();
									}
									else if(ans[t2.sum].size()>t2.s.size())
										ans[t2.sum]=t2.s;
									else if(ans[t2.sum].size()==t2.s.size()&&ans[t2.sum]>t2.s)
										ans[t2.sum]=t2.s;
								}
								if(t2.s.size()<=lim)
								{
									if(!is[t2.x][t2.y][t2.sum+200][t2.s.size()/2])
									{
										is[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=true;
										ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=t2.s;
										q.push(t2);
									}
									else
									{
										if(t2.s<ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2])
										{
											ss[t2.x][t2.y][t2.sum+200][t2.s.size()/2]=t2.s;
											q.push(t2);
										}
									}
								}
							}
					}
				}
		}
		cout<<"Case #"<<++dd<<":"<<endl;
		for(i=0;i<Q;i++)
			cout<<ans[need[i]]<<endl;
	}
}

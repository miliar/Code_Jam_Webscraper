#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)

#define N 14

const int moves[4][2]={{-1,0},{1,0},{0,1},{0,-1}};

typedef pair<char,char> PCC;
typedef vector<PCC> VC;

struct event
{
	VC pos;
	int val;
	bool con;
	event() {}
	event(VC Pos,int Val,bool Con) {pos=Pos;val=Val;con=Con;}
	bool operator<(event a) const {return (val>a.val);}
};

inline char abs(char a)
{
	return (a>=0?(a):(-a));
}

int t,test;
int r,c,i,j,k,l,val;
int a[N][N],b[N][N];
map<VC,int> f;
VC start,finish,tek,next;
priority_queue<event> q;
bool flag,con,con2,flag1;
bool used[5];

void dfs(VC &pos,char j)
{
	used[j]=1;
	for(char i=0;i<k;i++)
		if(!used[i] && abs(pos[i].first-pos[j].first)+abs(pos[i].second-pos[j].second)==1)
			dfs(pos,i);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
    scanf("%d",&test);
    forr(t,1,test)
    {
		scanf("%d%d",&r,&c);
		fprintf(stderr,"%d\n",t);
		getchar();
		forr(i,0,r+1)
		{
			a[i][0]='#';
			a[i][c+1]='#';
		}
		forr(i,0,c+1)
		{
			a[0][i]='#';
			a[r+1][i]='#';
		}
		forr(i,1,r)
		{
			forr(j,1,c)
				scanf("%c",&a[i][j]);
			getchar();
		}
		k=0;
		start.clear();
		forr(i,1,r)
			forr(j,1,c)
				if(a[i][j]=='o' || a[i][j]=='w')
				{
					++k;
					start.push_back(make_pair(i,j));
				}
		finish.clear();
		forr(i,1,r)
			forr(j,1,c)
				if(a[i][j]=='x' || a[i][j]=='w')
					finish.push_back(make_pair(i,j));
		while(!q.empty())
			q.pop();
		f.clear();
		sort(start.begin(),start.end());
		sort(finish.begin(),finish.end());	
		q.push(event(start,0,1));
		f[start]=0;
		flag=0;
		while(!q.empty())
		{
			tek=q.top().pos;
			val=q.top().val;
			con=q.top().con;
			/*forr(i,1,r)
				forr(j,1,c)
				{
					b[i][j]=a[i][j];
					if(a[i][j]!='.' && a[i][j]!='#')
						b[i][j]='.';
				}
			rep(i,k)
				b[tek[i].first][tek[i].second]='o';
			fprintf(stderr,"%d\n",val);
			forr(i,1,r)
			{
				forr(j,1,c)
					fprintf(stderr,"%c",b[i][j]);
				fprintf(stderr,"\n");
			}*/
			q.pop();
			if(val>f[tek])continue;
			rep(i,k)
				rep(j,4)
				{
					flag1=(a[tek[i].first+moves[j][0]][tek[i].second+moves[j][1]]!='#');
					l=0;
					while(l<k && !(tek[i].first+moves[j][0]==tek[l].first && tek[i].second+moves[j][1]==tek[l].second))l++;
					flag1=(flag1 && (l==k));
					if(j<2)
						flag1=(flag1 && a[tek[i].first-moves[j][0]][tek[i].second]!='#');else
						flag1=(flag1 && a[tek[i].first][tek[i].second-moves[j][1]]!='#');
					if(j<2)
					{
						l=0;
						while(l<k && !(tek[i].first-moves[j][0]==tek[l].first && tek[i].second==tek[l].second))l++;
					}else
					{
						l=0;
						while(l<k && !(tek[i].first==tek[l].first && tek[i].second-moves[j][1]==tek[l].second))l++;
					}
					flag1=(flag1 && (l==k));
					if(flag1)
					{
						next=tek;
						next[i].first+=moves[j][0];
						next[i].second+=moves[j][1];
						memset(used,0,sizeof(used));
						dfs(next,0);
						l=0;
						while(l<k && used[l])l++;
						con2=(l==k);
						if(!con2 && !con)continue;
						sort(next.begin(),next.end());
						if((f[next]==0 || f[next]>val+1) && next!=start)
						{
							f[next]=val+1;
							q.push(event(next,val+1,con2));
						}
					}
				}
			if(tek==finish)
			{
				printf("Case #%d: %d\n",t,f[tek]);
				flag=1;
				break;
			}
		}
		if(!flag)
			printf("Case #%d: %d\n",t,-1);
    }
    return 0;
}

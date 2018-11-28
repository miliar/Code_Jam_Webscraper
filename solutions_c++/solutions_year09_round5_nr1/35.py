#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
#define maxn 15
#define maxstat 1000000
#define x first
#define y second
#define debug 0

typedef pair<int,int> Tbox;
typedef vector<Tbox> Tstat;

const int dx[]={0,1,0,-1};
const int dy[]={1,0,-1,0};

Tstat q[maxstat],Box,Tar;
int n,m,ans,father[maxn];
char s[maxn][maxn];
bool mark[maxn][maxn];
map <Tstat,int> hash;

inline bool range(int x,int y)
{
	return x>=0 && y>=0 && x<n && y<m;
}

inline void addBox(int x,int y)
{
	Box.push_back(make_pair(x,y));
}

inline void addTar(int x,int y)
{
	Tar.push_back(make_pair(x,y));
}

inline int find(int x)
{
	if (x==father[x]) return x;
	return father[x]=find(father[x]);
}

inline bool check(Tstat &x)
{
	int n=x.size();
	for (int i=0;i<n;++i)
		father[i]=i;
	for (int i=0;i<n;++i)
		for (int j=0;j<n;++j)
		if (abs(x[i].x-x[j].x)+abs(x[i].y-x[j].y)==1)
			father[find(i)]=find(j);
	for (int i=1;i<n;++i)
	if (find(i)!=find(0)) return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d%d",&n,&m);
		Box.clear();Tar.clear();
		for (int i=0;i<n;++i)
		{
			scanf("%s",&s[i]);
			for (int j=0;j<m;++j)
			{
				if (s[i][j]=='o' || s[i][j]=='w') addBox(i,j);
				if (s[i][j]=='x' || s[i][j]=='w') addTar(i,j);
			}
		}
		sort(Box.begin(),Box.end());
		sort(Tar.begin(),Tar.end());
		if (Box==Tar) ans=0;
		else
		{
			memset(mark,false,sizeof(mark));
			q[0]=Box;
			hash.clear();
			hash[Box]=1;
			for (int h=0,tail=1;h<tail;++h)
			{
				Tstat cur=q[h];
				bool fl=check(cur);
				if (debug)
				{
					for (int i=0;i<cur.size();++i)
						printf("%d %d\n",cur[i].x,cur[i].y);
					puts("__________________");
					if (cur[0].x==2 && cur[0].y==3 && cur[1].x==2 && cur[1].y==4)
						puts(""); 
				}
				int now=hash[cur];
				for (int i=0;i<cur.size();++i)
					mark[cur[i].x][cur[i].y]=true;
				for (int i=0;i<cur.size();++i)
				{
					for (int k=0;k<4;++k)
					{
						int sx=cur[i].x-dx[k],sy=cur[i].y-dy[k];
						if (!range(sx,sy) || s[sx][sy]=='#' || mark[sx][sy]) continue;
						int tx=cur[i].x+dx[k],ty=cur[i].y+dy[k];
						if (!range(tx,ty) || s[tx][ty]=='#' || mark[tx][ty]) continue;
						
						Tstat tmp=cur;
						tmp[i].x=tx;tmp[i].y=ty;
						if (tmp[0]==tmp[1])
							puts("");
						if (!fl && !check(tmp)) continue;
						sort(tmp.begin(),tmp.end());
						if (!hash.count(tmp))
						{
							hash[tmp]=now+1;
							if (tmp==Tar) goto Break;
							q[tail++]=tmp;
						}
					}
				}
				for (int i=0;i<cur.size();++i)
					mark[cur[i].x][cur[i].y]=false;
			}
			Break:;
			if (!hash.count(Tar)) ans=-1;
			else ans=hash[Tar]-1;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	
	return 0;
}

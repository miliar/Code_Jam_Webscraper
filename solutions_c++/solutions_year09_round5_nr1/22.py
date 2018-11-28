#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define oo 20
#define ss 7000005
#define Mod 6999997
#define inf 1000000000
const int dx[]={0,0,1,-1};
const int dy[]={1,-1,0,0};
int Test,Case;
char s[oo][oo];
struct Tpnt
{
	int x,y;
};
struct Tque
{
	Tpnt a[5];
}	q[ss],S,T;
int f[ss];
int head,tail;
bool mk[ss];
int N,M,K,St,Ta;

inline bool comp(const Tpnt& A,const Tpnt& B)
{
	if (A.x==B.x) return A.y<B.y;
	return A.x<B.x;
}

inline int Hash(Tque& A)
{
	int res=0;
	sort(A.a,A.a+K,comp);
	for (int i=0;i<K;++i)
		res=(res*N*M+(A.a[i].x-1)*M+A.a[i].y)%Mod;
	
	return res;
}

inline void Readin()
{
	scanf("%d%d",&N,&M);
	for (int i=1;i<=N;++i)
		scanf("%s",s[i]+1);
}

inline void Prepare()
{
	int u=0,v=0;
	for (int i=1;i<=N;++i)
		for (int j=1;j<=M;++j)
		{
			if (s[i][j]=='o' || s[i][j]=='w')
			{
				S.a[u].x=i;
				S.a[u].y=j;
				u++;
			}
			if (s[i][j]=='x' || s[i][j]=='w')
			{
				T.a[v].x=i;
				T.a[v].y=j;
				v++;
			}
		}
	K=u;	
	St=Hash(S);
	Ta=Hash(T);
}

inline bool Check1(const Tque& v,int i,int dx,int dy)
{
	Tpnt A=v.a[i];
	A.x-=dx;
	A.y-=dy;
	if (A.x<1 || A.x>N || A.y<1 || A.y>M) return false;
	if (s[A.x][A.y]=='#') return false;
	for (int j=0;j<K;++j)
		if (i!=j && A.x==v.a[j].x && A.y==v.a[j].y) return false;
	A.x+=dx*2;
	A.y+=dy*2;
	if (A.x<1 || A.x>N || A.y<1 || A.y>M) return false;
	if (s[A.x][A.y]=='#') return false;
	for (int j=0;j<K;++j)
		if (i!=j && A.x==v.a[j].x && A.y==v.a[j].y) return false;
	return true;
}

int DFS(bool mk[],const Tpnt a[],int v)
{
	int res=1;
	mk[v]=true;
	for (int i=0;i<K;++i)
		if (!mk[i] && (a[i].x==a[v].x && abs(a[i].y-a[v].y)==1 || a[i].y==a[v].y && abs(a[i].x-a[v].x)==1))
			res+=DFS(mk,a,i);
	return res;
}

inline bool Check2(const Tque& v)
{
	bool mk[5]={};
	return DFS(mk,v.a,0)==K;
}

inline void Solve()
{
	head=0,tail=1;
	q[0]=S;
	memset(f,63,sizeof f);
	memset(mk,0,sizeof mk);
	f[Hash(S)]=0;
	mk[Hash(S)]=true;
	
	while (head!=tail)
	{
		Tque u=q[head++],v,w;
		int U=Hash(u);
		if (head==7000000) head++;
		
		for (int i=0;i<K;++i)
			for (int j=0;j<4;++j)
			{
				v=u;
				if (!Check1(v,i,dx[j],dy[j])) continue;
				v.a[i].x+=dx[j];
				v.a[i].y+=dy[j];
				if (Check2(v))
				{
					if (f[Hash(v)]>f[U]+1)
					{
						f[Hash(v)]=f[U]+1;
						if (!mk[Hash(v)])
						{
							mk[Hash(v)]=true;
							q[tail++]=v;
							if (tail==7000000) tail++;
						}
					}
				}
				else{
					w=v;
					for (int i=0;i<K;++i)
					for (int j=0;j<4;++j)
					{
						v=w;
						if (!Check1(v,i,dx[j],dy[j])) continue;
						v.a[i].x+=dx[j];
						v.a[i].y+=dy[j];
						if (!Check2(v)) continue;
						if (f[Hash(v)]>f[U]+2)
						{
							f[Hash(v)]=f[U]+2;
							if (!mk[Hash(v)])
							{
								mk[Hash(v)]=true;
								q[tail++]=v;
								if (tail==7000000) tail++;
							}
						}
					}
				}
			}
		mk[U]=false;
	}
	
	if (f[Hash(T)]>inf) puts("-1");
	else printf("%d\n",f[Hash(T)]);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		
		Readin();
		Prepare();
		Solve();
	}
	
	return 0;
}

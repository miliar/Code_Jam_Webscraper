#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn (105)
#define abs(x) ((x)<0?(-(x)):(x))
using namespace std;

int test,n,a[maxn][maxn],aa[maxn][maxn],T[maxn];
bool row[maxn],col[maxn];

inline int Length(int i)
{
	if (i<=n) return i;
		else return 2*n-i;
}
inline int Calc(int i,int mid)
{
	return 2*mid-i;
}
inline bool Check(int i,int j,int ii,int jj,int len)
{
	if (len==0) return true;
	return a[i][j]==a[ii][jj] && Check(i,j+1,ii,jj+1,len-1);
}
inline bool Check_(int i,int j,int ii,int jj,int len)
{
	if (len==0) return true;
	return aa[i][j]==aa[ii][jj] && Check_(i,j+1,ii,jj+1,len-1);
}
int main()
{
	//freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++)
	{
		printf("Case #%d: ",cnt);
		scanf("%d",&n);
		memset(a,0,sizeof(a));
		memset(aa,0,sizeof(aa));
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		memset(T,0,sizeof(T));
		for (int i=1;i<=2*n-1;i++)
		{
			int len=Length(i);
			for (int j=1;j<=len;j++) 
			{
				scanf("%d",&a[i][j]);
				int k=(j-1)*2+abs(n-i)+1;
				aa[k][++T[k]]=a[i][j];
			}
		}
		for (int i=1;i<=2*n-1;i++)
		{
			bool can=true;
			for (int j=1;j<=2*n-1 && can;j++) if (j!=i)
			{
				int k=Calc(j,i);
				if (k>2*n-1 || k<1) continue;
				int lena=Length(j),lenb=Length(k);
				bool ok=true;
				if (lena<lenb && !Check(j,1,k,1+(lenb-lena)/2,lena)) ok=false;
				if (lena>=lenb && !Check(j,1+(lena-lenb)/2,k,1,lenb)) ok=false;
				if (!ok) can=false;
			}
			row[i]=can;
		}
		for (int i=1;i<=2*n-1;i++)
		{
			bool can=true;
			for (int j=1;j<=2*n-1 && can;j++) if (j!=i)
			{
				int k=Calc(j,i);
				if (k>2*n-1 || k<1) continue;
				int lena=Length(j),lenb=Length(k);
				bool ok=true;
				if (lena<lenb && !Check_(j,1,k,1+(lenb-lena)/2,lena)) ok=false;
				if (lena>=lenb && !Check_(j,1+(lena-lenb)/2,k,1,lenb)) ok=false;
				if (!ok) can=false;
			}
			col[i]=can;
		}
		int best=-1;
		for (int i=1;i<=2*n-1;i++) if (row[i])
			for (int j=1;j<=2*n-1;j++) if (col[j])
			{
				//int ans=max(max(i,2*n-1-i+1),max(j,2*n-1-j+1));
				//if (best==-1 || best>ans) best=ans;
				int x=i-1,y=j-1;
				int A=max(abs(x-y),abs(x+y-2*n+2));
				int tmp;
				if (!(n%2))
					if(!(A%2)) tmp=(n/2+A/2)*2;
						else tmp=1+2*(n/2+A/2);
				else 
					if (!(A%2)) tmp=1+2*(n/2+A/2);
						else tmp=2*(n/2+A/2+1);
				if (best==-1 || best>tmp) best=tmp;
			}
		printf("%d\n",best*best-n*n);
	}
	return 0;
}

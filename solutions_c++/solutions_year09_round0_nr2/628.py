#include<iostream>
using namespace std;
#define MAXN 30005 
int Parent[MAXN], Rank[MAXN]; 
int vist[MAXN]; 
void make_set(int x) 
{    	Parent[x] = x;   vist[x]=1;  Rank[x] = 0;   } // 合并x,y所在的集合，并返回交集 
// 返回到元素i所属的集合的代表元素, 同时进行路径压缩 
int FindSet(int i) 
{	
	if( ( i == -1 ) || ( i >= MAXN ) )  
	{
		return -1; 	
	}
	else 
	{ 
		if(( Parent[i] != -1 ) && ( Parent[i] != i ) ) 
			Parent[i] = FindSet( Parent[i] ); // 这句话进行路径压缩*/ 
		return Parent[i]; 		
	}
} 
int Union(int x, int y) 
{
	x = FindSet( x ); // 找到x所在的树的根 
	y = FindSet( y ); // 找到y所在的树的根 
	if( x == y ) 		
		return x; // -1表示空集 
	if( x == -1 ) 		
		return y; 
	if( y == -1 )		
		return x; 
	if( Rank[x] > Rank[y] ) 
	{ // 将较低的树合并到较高的树上 
		Parent[y] = x; 		
		vist[x]=vist[x]+vist[y]; 		
		return x;	
	}
	else 
	{
	 	Parent[x] = y; 	 	
		vist[y]=vist[x]+vist[y]; 	 	
		if( Rank[x] == Rank[y] ) 
	 		Rank[y]++; // 改变树的高度 
	 	return y; 	 
	} 
}
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int main()
{
	int low,dd1,dd2,fa,cs,kk,h,w,i,j,k,d1,d2,idx,mp[110][110],out[11000],bj[11000];
	freopen("watersheds.in","r",stdin);
	freopen("watersheds.out","w",stdout);
	scanf("%d",&cs);
	for (kk=1;kk<=cs;kk++)
	{
		scanf("%d%d",&h,&w);
		for (i=1;i<=h*w;i++)
			make_set(i);
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
				scanf("%d",&mp[i][j]);
		for (i=1;i<=h;i++)
			for (j=1;j<=w;j++)
			{
				low=1000000000;
				for (k=0;k<4;k++)
				{
					d1=i+dir[k][0];
					d2=j+dir[k][1];
					if ( d1>=1 && d1<=h && d2>=1 && d2<=w && mp[i][j]>mp[d1][d2] && mp[d1][d2]<low)
					{
						low=mp[d1][d2];
						dd1=d1;
						dd2=d2;
					}
				}
				if (low!=1000000000)
					Union((i-1)*w+j,(dd1-1)*w+dd2);
			}
		idx=0;
		memset(bj,-1,sizeof(bj));
		for (i=1;i<=h*w;i++)
		{
			fa=FindSet(i);
			if (bj[fa]==-1)
			{
				bj[fa]=idx;
				idx++;
			}
			out[i]=bj[fa];
		}
		printf("Case #%d:\n",kk);
		for (i=1;i<=h;i++)
		{
			for (j=1;j<=w;j++)
				if (j<w) printf("%c ",out[(i-1)*w+j]+'a');
				else printf("%c",out[(i-1)*w+j]+'a');
			printf("\n");
		}
	}
	return 0;
}
		

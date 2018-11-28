#include <cstdio>
#include <memory>
#define oo 105
#define M 10007
#define ok(x,y) ((x)>0&&(x)<=H&&(y)>0&&(y)<=W&&(!map[x][y]))
const int dx[]={-2,-1};
const int dy[]={-1,-2};
int Test,Case;
int H,W,r,c,R;
int f[oo][oo];
bool map[oo][oo];

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	
	for (scanf("%d",&Test);Test;Test--)
	{
		memset(map,0,sizeof map);
		memset(f,0,sizeof f);
		f[1][1]=1;
		scanf("%d%d%d",&H,&W,&R);
		while (R--)
		{
			scanf("%d%d",&r,&c);
			map[r][c]=true;
		}
		
		for (int i=1;i<=H;++i)
			for (int j=1;j<=W;++j)
				if (!map[i][j])
				{
					for (int k=0;k<2;++k)
						if (ok(i+dx[k],j+dy[k]))
							f[i][j]+=f[i+dx[k]][j+dy[k]];
					f[i][j]%=M;
				}
		
		printf("Case #%d: %d\n",++Case,f[H][W]);
	}
	
	return 0;
}

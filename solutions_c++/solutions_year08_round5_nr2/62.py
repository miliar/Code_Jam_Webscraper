#include <stdio.h>
#include <vector>
#include <string.h>
#include <utility>
#include <memory>
using namespace std;
int nT,T;
int R,C;
char data[16][16];
typedef signed char schar;
bool reach[15][15][15][16][4][15][16];
pair<schar,schar> shootdir[15][15][4];
int dir[4][2]={
	{1,0},
	{0,1},
	{-1,0},
	{0,-1}};
struct normal
{
	char x,y;
	char yx,yy,yf;
	schar bx,by;
	bool solget()
	{
		return data[x][y]=='X';
	}
	bool shooty(schar dir)
	{
		if (shootdir[x][y][dir].first!=-1)
		{
			if (reach[x][y][shootdir[x][y][dir].first][shootdir[x][y][dir].second][dir][bx][by])
				return false;
			yx=shootdir[x][y][dir].first;
			yy=shootdir[x][y][dir].second;
			yf=dir;
			reach[x][y][yx][yy][yf][bx][by]=true;
			return true;
		}
		return false;
	}
	bool shootb(schar dir)
	{
		if (shootdir[x][y][dir].first!=-1)
		{
			if (reach[x][y][yx][yy][yf][shootdir[x][y][dir].first][shootdir[x][y][dir].second])
				return false;
			bx=shootdir[x][y][dir].first;
			by=shootdir[x][y][dir].second;
			reach[x][y][yx][yy][yf][bx][by]=true;
			return true;
		}
		return false;
	}
	bool go(schar d)
	{
		if (x==yx&&y==yy&&yf==d&&by!=15)
		{
			if (reach[bx][by][yx][yy][yf][bx][by])
				return false;
			x=bx;
			y=by;
			reach[x][y][yx][yy][yf][bx][by]=true;
			return true;
		}

		schar _x=x+dir[d][0],_y=y+dir[d][1];
		if (_x<0||_x>=R||_y<0||_y>=C)
			return false;
		if (data[_x][_y]=='#')
			return false;
		if (reach[_x][_y][yx][yy][yf][bx][by])
			return false;
		reach[_x][_y][yx][yy][yf][bx][by]=true;
		x=_x;
		y=_y;
	}
};
vector<normal> nowp,lastp;
int main()
{
	freopen("c:\\test.in","r",stdin);
	FILE*s=fopen("c:\\test.out","w");
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		printf("%d\n",T);
		scanf("%d%d",&R,&C);
		schar i,j,k,l,m;
		for (i=0;i<R;i++)
			scanf("%s",data[i]);
		//Recalc walls
		for (i=0;i<R;i++)
			for (j=0;j<C;j++) if (data[i][j]!='#')
				for (k=0;k<4;k++)
				{
					l=i;
					m=j;
					while (l>=0&&l<R&&m>=0&&m<C&&data[l][m]!='#')
					{
						l+=dir[k][0];
						m+=dir[k][1];
					}
					shootdir[i][j][k]=make_pair(l-dir[k][0],m-dir[k][1]);
				}
		//Get player
		for (i=0;i<R;i++)
			for (j=0;j<C;j++)
				if (data[i][j]=='O')
					goto found;
found:
		memset(reach,0,sizeof(reach));
		//Make first
		normal f;
		f.x=i;
		f.y=j;
		f.yx=0;
		f.yy=15;
		f.yf=2;
		f.bx=0;
		f.by=15;
		nowp.clear();
		lastp.clear();
		nowp.push_back(f);
		int c=0;
		while (nowp.size())
		{
			c++;
			lastp.swap(nowp);
			nowp.clear();
			while (lastp.size())
			{
				normal t=*lastp.rbegin();
				lastp.pop_back();
				f=t;
				//Try shoot
				for (i=0;i<4;i++)
				{
					if (f.shootb(i))
					{
						lastp.push_back(f);
						f=t;
					}
					if (f.shooty(i))
					{
						lastp.push_back(f);
						f=t;
					}
				}
				//Try move
				for (i=0;i<4;i++)
					if (f.go(i))
					{
						if (f.solget())
							goto ansgot;
						nowp.push_back(f);
						f=t;
					}
			}
		}
		fprintf(s,"Case #%d: THE CAKE IS A LIE\n",nT-T);
		continue;
ansgot:
		fprintf(s,"Case #%d: %d\n",nT-T,c);
	}
	fclose(stdin);
	fclose(s);
}
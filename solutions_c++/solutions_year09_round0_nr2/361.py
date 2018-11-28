#include <cstdio>
#include <cstring>
using namespace std;
char lt[100][100];
int co[100][100][4];
int fill(int a,int b,char ch)
{
	lt[a][b]=ch;
	if (co[a][b][0] && !lt[a-1][b]) fill(a-1,b,ch);
	if (co[a][b][1] && !lt[a][b-1]) fill(a,b-1,ch);
	if (co[a][b][2] && !lt[a][b+1]) fill(a,b+1,ch);
	if (co[a][b][3] && !lt[a+1][b]) fill(a+1,b,ch);
	return 0;
}
int main()
{
	int ri,rp;
	int h,w,i,j;
	int al[100][100];
	char now;
	scanf("%d",&rp);
	for (ri=0;ri<rp;ri++)
	{
		memset(co,0,sizeof(co));
		memset(lt,0,sizeof(lt));
		scanf("%d%d",&h,&w);
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
				scanf("%d",&al[i][j]);
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
			{
				int min=al[i][j],dir=-1;
				if (i>0 && al[i-1][j]<min) {min=al[i-1][j]; dir=0;}
				if (j>0 && al[i][j-1]<min) {min=al[i][j-1]; dir=1;}
				if (j<w-1 && al[i][j+1]<min) {min=al[i][j+1]; dir=2;}
				if (i<h-1 && al[i+1][j]<min) {min=al[i+1][j]; dir=3;}
				switch (dir)
				{
				case 0:co[i][j][0]=co[i-1][j][3]=1;break;
				case 1:co[i][j][1]=co[i][j-1][2]=1;break;
				case 2:co[i][j][2]=co[i][j+1][1]=1;break;
				case 3:co[i][j][3]=co[i+1][j][0]=1;break;
				}
			}
		/*for (i=0;i<h;i++)
		{
			for (j=0;j<w;j++)
				printf("%d ",co[i][j][0]);
		}*/
		now='a';
		for (i=0;i<h;i++)
			for (j=0;j<w;j++)
			{
				if (lt[i][j]==0) {fill(i,j,now); now++;}
			}
		printf("Case #%d:\n",ri+1);
		for (i=0;i<h;i++)
		{
			for (j=0;j<w-1;j++)
			{
				putchar(lt[i][j]);
				putchar(' ');
			}
			putchar(lt[i][w-1]);
			putchar('\n');
		}
	}
	return 0;
}

#include <cstring>
#include <cstdio>
using namespace std;
bool b[2][110][110];
int c,r;

int main()
{
	FILE *input=fopen("c.in","r");
	FILE *output=fopen("c.out","w");
	fscanf(input,"%d",&c);
	for (int c0=1;c0<=c;c0++)
	{
		memset(b,false,sizeof(b));
		fscanf(input,"%d",&r);
		int x1,y1,x2,y3,k=0;
		for (int i=1;i<=r;i++)
		{
			fscanf(input,"%d%d%d%d",&x1,&y1,&x2,&y3);
			for (int x=x1;x<=x2;x++)
				for (int y=y1;y<=y3;y++)
					b[0][x][y]=true;
		}
		bool bb=true;
		while (bb)
		{
			bb=false;
			k++;
			for (int x=1;x<=100;x++)
				for (int y=1;y<=100;y++)
				{
					if (!b[1-k%2][x-1][y] && !b[1-k%2][x][y-1])
						b[k%2][x][y]=false;
					else if (b[1-k%2][x-1][y] && b[1-k%2][x][y-1])
						b[k%2][x][y]=true;
					else b[k%2][x][y]=b[1-k%2][x][y];
					if (b[k%2][x][y]) bb=true;
				}
		}
		fprintf(output,"Case #%d: %d\n",c0,k);
	}
	fclose(input);
	fclose(output);
	return 0;
}
#include <iostream>
#include <string.h>
using namespace std;
int low;
int alt[102][102];
int lc[102][102];
int fai[102][102],faj[102][102];
char map[102][102];
char label;
inline void test(int i,int j,int x,int y)
{
	if (alt[x][y]<=low)
	{
		fai[i][j]=x;
		faj[i][j]=y;
		low=alt[x][y];
	}
}
void expand(int x,int y)
{
	map[x][y]=label;
	if (fai[x-1][y]==x&&faj[x-1][y]==y)
		expand(x-1,y);
	if (fai[x][y-1]==x&&faj[x][y-1]==y)
		expand(x,y-1);
	if (fai[x+1][y]==x&&faj[x+1][y]==y)
		expand(x+1,y);
	if (fai[x][y+1]==x&&faj[x][y+1]==y)
		expand(x,y+1);
}
int main()
{
	int tot,t,i,j,h,w,size,temp;
	int sortlc[30],sorti[30],sortj[30];
	cin >> tot;
for (t=1;t<=tot;t++)
{
	memset(alt,127,sizeof(alt));
	cin >> h >> w;
	for (i=1;i<=h;i++)
		for (j=1;j<=w;j++)
			cin >> alt[i][j];
	for (i=0;i<=h+1;i++)
		for (j=0;j<=w+1;j++)
		{
			fai[i][j]=i;
			faj[i][j]=j;
			lc[i][j]=i*200+j;
		}
	for (i=1;i<=h;i++)
		for (j=1;j<=w;j++)
		{
			low=alt[i][j]-1;
			test(i,j,i+1,j);
			test(i,j,i,j+1);
			test(i,j,i,j-1);
			test(i,j,i-1,j);
			lc[fai[i][j]][faj[i][j]]=min(lc[i][j],lc[fai[i][j]][faj[i][j]]);
		}
	size=0;
	for (i=1;i<=h;i++)
		for (j=1;j<=w;j++)
			if (fai[i][j]==i&&faj[i][j]==j)
			{
				sortlc[size]=lc[i][j];
				sorti[size]=i;
				sortj[size]=j;
				size++;
			}
	for (i=0;i<size;i++)
		for (j=0;j<size-1;j++)
			if (sortlc[j]>sortlc[j+1])
			{
				temp=sortlc[j];
				sortlc[j]=sortlc[j+1];
				sortlc[j+1]=temp;
				temp=sorti[j];
				sorti[j]=sorti[j+1];
				sorti[j+1]=temp;
				temp=sortj[j];
				sortj[j]=sortj[j+1];
				sortj[j+1]=temp;
			}
	for (i=0;i<size;i++)
	{
		label=char(i+int('a'));
		expand(sorti[i],sortj[i]);
	}
	cout << "Case #" << t << ":\n";
	for (i=1;i<=h;i++)
	{
		cout << map[i][1];
		for (j=2;j<=w;j++)
			cout << " " << map[i][j];
		cout << endl;
	}
}}

#include <cstdio>
#include <cstring>
using namespace std;

const char answ[4][10]={"Neither","Red","Blue","Both"};
char c[55][55];
int n,k;

void read()
{
	for(int i=1;i<=n;++i)gets(&c[i][1]);
	for(int i=1;i<=n;++i)
	{
		int p=n;
		for(int j=n;j>=1;--j)
			if(c[i][j]!='.')c[i][p--]=c[i][j];
		for(;p>=1;--p)c[i][p]='.';
	}

}

const int xd[]={0,1,1,1};
const int yd[]={1,0,1,-1};

bool test(char col,int x,int y,int d)
{
	for(int j=0;j<k;++j)
	{
		if(c[x][y]!=col)return false;
		x+=xd[d];
		y+=yd[d];
	}
	return true;
}

bool have(char col)
{
	for(int i=1;i<=n;++i)
		for(int j=1;j<=n;++j)
			for(int d=0;d<4;++d)
				if(test(col,i,j,d))return true;
	return false;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i)
	{
		scanf("%d %d\n",&n,&k);
		memset(c,'.',sizeof(c));
		read();
		int m=0;
		if(have('R'))m+=1;
		if(have('B'))m+=2;
		printf("Case #%d: %s\n",i,answ[m]);
	}
	scanf("\n");
	return 0;
}




#include <fstream>
using namespace std;

int T,H,W,i,j,k,m,minNum,ch,currentch;
int a[102][102];
int b[10001];
char c[102][102];

int getPos(int i,int j)
{
	return (i-1)*W+j;
}
int getPosH(int num)
{
	if(num%W==0)
		return num/W;
	return num/W+1;
}
int getPosW(int num)
{
	if(num%W==0 && num/W!=0)
		return W;
	return num%W;
}
int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("B-small-attempt0.in");
	outf.open("B-small-attempt0.out");
	inf>>T;
	for(m=0;m<T;m++)
	{
		inf>>H>>W;
		for(i=1;i<=H*W;i++)
			b[i]=i;
		for(i=0;i<H+2;i++)
			a[i][0]=a[i][W+1]=10;
		for(i=0;i<W+2;i++)
			a[0][i]=a[H+1][i]=10;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
			{inf>>a[i][j];c[i][j]=0;}
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
			{
				minNum=a[i][j];
				if(a[i-1][j]<minNum)
				{minNum=a[i-1][j];k=getPos(i-1,j);}
				if(a[i][j-1]<minNum)
				{minNum=a[i][j-1];k=getPos(i,j-1);}
				if(a[i][j+1]<minNum)
				{minNum=a[i][j+1];k=getPos(i,j+1);}
				if(a[i+1][j]<minNum)
				{minNum=a[i+1][j];k=getPos(i+1,j);}
				if(a[i][j]!=minNum)
				{b[getPos(i,j)]=k;}	
			}
		currentch='a'-1;
		outf<<"Case #"<<m+1<<": "<<endl;	
		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++)
			{
				if(c[i][j]!=0) {outf<<c[i][j]<<' ' ;continue;}
				ch=0;
				for(k=getPos(i,j);k!=b[k];k=b[k])
				{
				if(c[getPosH(k)][getPosW(k)]!=0)
				{ch=c[getPosH(k)][getPosW(k)];break;}
				}
				if(k==b[k])
					if(c[getPosH(k)][getPosW(k)]!=0)
						{ch=c[getPosH(k)][getPosW(k)];}
				if(ch==0)
				{c[getPosH(k)][getPosW(k)]=c[i][j]=++currentch;}
				else c[i][j]=ch;
				outf<<c[i][j]<<' ';
			}
			outf<<endl;
		}
	}
	return 0;
}

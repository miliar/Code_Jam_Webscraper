

#include <iostream>
using namespace std;

char b[100][100];
int a[100][100];
char s;
int H,W;
bool ok(int x,int y)
{
	if(x<0)return false;
	if(x>H-1)return false;
	if(y<0)return false;
	if(y>W-1)return false;
	return true;
}
char fun(int i,int j)
{
	int t=a[i][j];
	int ti=i,tj=j;
	if(ok(i-1,j) && a[i-1][j]<t){
		ti=i-1;
		tj=j;
		t=a[i-1][j];
	}
	if(ok(i,j-1) && a[i][j-1]<t){
		ti=i;
		tj=j-1;
		t=a[i][j-1];
	}
	if(ok(i,j+1) && a[i][j+1]<t){
		ti=i;
		tj=j+1;
		t=a[i][j+1];
	}
	if(ok(i+1,j) && a[i+1][j]<t){
		ti=i+1;
		tj=j;
		t=a[i+1][j];
	}
	if(ti==i && tj==j)return b[i][j]=char(s++);
	if(b[ti][tj]!=' ')return b[i][j]=b[ti][tj];
	return b[i][j]=fun(ti,tj);
}
int main()
{
	freopen("E://B-large.in","r",stdin);
	freopen("E://yyy.txt","w",stdout);
	int T,t=1;
	cin>>T;
	while(t<=T)
	{
		cin>>H>>W;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				cin>>a[i][j];
				b[i][j]=' ';
			}
		}
		s='a';
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				if(b[i][j]==' ')
					fun(i,j);
			}
		}
		cout<<"Case #"<<t<<":"<<endl;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				cout<<b[i][j]<<" ";
			}
			cout<<endl;
		}
		t++;
	}
	return 0;
}
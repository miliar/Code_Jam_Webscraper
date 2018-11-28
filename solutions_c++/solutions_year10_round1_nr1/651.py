#include<fstream>
#include<iostream>

using namespace std;

//ifstream cin("date.in");
//ofstream cout("date.out");

int x,y,a[51][51],OKB,OKR,k,n,i;

void clear(int n);
void rotate(int n);
void verify(int n);
void solve(int n);

int main()
{
	cin>>n;
	for (i=1;i<=n;++i)
	{
		cin>>x>>k;
		cin.get();
		solve(x);
		cout<<"Case #"<<i<<": ";
		if (OKB==OKR&&!OKR) cout<<"Neither";
		else if (OKB==OKR&&OKB) cout<<"Both";
		else if (OKB&&!OKR) cout<<"Blue";
		else cout<<"Red";
		cout<<'\n';
	}
	//cin.close();
	//cout.close();
	return 0;
}

void solve(int n)
{
	int i,j;
	char c;
	for (i=1;i<=n;++i)
	{
		for (j=1;j<=n;++j)
		{
			cin.get(c);
			if (c=='B') a[i][j]=2;
			else if (c=='R') a[i][j]=1;
			else a[i][j]=0;
			//cin.coutet(c);
		}
		cin.get();
	}
	rotate(n);
	verify(n);
	clear(n);
}

void rotate(int n)
{
	int i,j,pos;
	for (i=n;i>=1;--i)
	{
		pos=n+1;
		for (j=n;j>=1;--j)
			if (a[i][j])
			{
				--pos;
				a[i][pos]=a[i][j];
				if (j!=pos)	a[i][j]=0;
			}
	}
}

void verify(int n)
{
	int i,j,nr,x,y;
	OKB=OKR=0;
	for (i=n;i>=1;--i)
		for (j=1;j<=n;++j)
			if (a[i][j])
			{
				
				x=i;
				y=j+1;
				nr=k-1;
				
				while (y<=n&&nr&&a[i][y]==a[i][j])
				{
					--nr;
					++y;
				}
				
				if (!nr)
				{
					if (a[i][j]==1) OKR=1;
					else OKB=1;
				}
				
				x=i-1;
				y=j;
				nr=k-1;
				
				while (x>=1&&nr&&a[x][j]==a[i][j])
				{
					--nr;
					--x;
				}
				
				if (!nr)
				{
					if (a[i][j]==1) OKR=1;
					else OKB=1;
				}
				
				x=i-1;
				y=j+1;
				nr=k-1;
				
				while (x>=1&&j<=n&&nr&&a[x][y]==a[i][j])
				{
					--nr;
					--x;
					++y;
				}
				
				if (!nr)
				{
					if (a[i][j]==1) OKR=1;
					else OKB=1;
				}
				
				x=i-1;
				y=j-1;
				nr=k-1;
				
				while (x>=1&&j>=1&&nr&&a[x][y]==a[i][j])
				{
					--nr;
					--x;
					--y;
				}
				
				if (!nr)
				{
					if (a[i][j]==1) OKR=1;
					else OKB=1;
				}
			}
}

void clear(int n)
{
	int i,j;
	for (i=1;i<=n;++i)
		for (j=1;j<=n;++j)
			a[i][j]=0;
} 

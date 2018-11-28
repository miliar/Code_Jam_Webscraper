#include <iostream>

using namespace std;


int t;
int board[34][34];
int m,n;

int cnt[33];
int sum;

void input()
{
	int i,j;
	char line[100];
	for (i=0; i<33; i++)
		cnt[i]=0;
	for (i=0; i<m; i++)
	{
		cin>>line;
		for (j=0; j<n/4; j++)
			switch (line[j])
			{
				case '0':
					board[i][j*4]=0;
					board[i][j*4+1]=0;
					board[i][j*4+2]=0;
					board[i][j*4+3]=0;
					break;
				case '1':
					board[i][j*4]=0;
					board[i][j*4+1]=0;
					board[i][j*4+2]=0;
					board[i][j*4+3]=1;
					break;
				case '2':
					board[i][j*4]=0;
					board[i][j*4+1]=0;
					board[i][j*4+2]=1;
					board[i][j*4+3]=0;
					break;
				case '3':
					board[i][j*4]=0;
					board[i][j*4+1]=0;
					board[i][j*4+2]=1;
					board[i][j*4+3]=1;
					break;
				case '4':
					board[i][j*4]=0;
					board[i][j*4+1]=1;
					board[i][j*4+2]=0;
					board[i][j*4+3]=0;
					break;
				case '5':
					board[i][j*4]=0;
					board[i][j*4+1]=1;
					board[i][j*4+2]=0;
					board[i][j*4+3]=1;
					break;
				case '6':
					board[i][j*4]=0;
					board[i][j*4+1]=1;
					board[i][j*4+2]=1;
					board[i][j*4+3]=0;
					break;
				case '7':
					board[i][j*4]=0;
					board[i][j*4+1]=1;
					board[i][j*4+2]=1;
					board[i][j*4+3]=1;
					break;
				case '8':
					board[i][j*4]=1;
					board[i][j*4+1]=0;
					board[i][j*4+2]=0;
					board[i][j*4+3]=0;
					break;
				case '9':
					board[i][j*4]=1;
					board[i][j*4+1]=0;
					board[i][j*4+2]=0;
					board[i][j*4+3]=1;
					break;
				case 'A':
					board[i][j*4]=1;
					board[i][j*4+1]=0;
					board[i][j*4+2]=1;
					board[i][j*4+3]=0;
					break;
				case 'B':
					board[i][j*4]=1;
					board[i][j*4+1]=0;
					board[i][j*4+2]=1;
					board[i][j*4+3]=1;
					break;
				case 'C':
					board[i][j*4]=1;
					board[i][j*4+1]=1;
					board[i][j*4+2]=0;
					board[i][j*4+3]=0;
					break;
				case 'D':
					board[i][j*4]=1;
					board[i][j*4+1]=1;
					board[i][j*4+2]=0;
					board[i][j*4+3]=1;
					break;
				case 'E':
					board[i][j*4]=1;
					board[i][j*4+1]=1;
					board[i][j*4+2]=1;
					board[i][j*4+3]=0;
					break;
				case 'F':
					board[i][j*4]=1;
					board[i][j*4+1]=1;
					board[i][j*4+2]=1;
					board[i][j*4+3]=1;
					break;
			}
	}
}

void find(int size)
{
	int i,j,x,y;
	bool flag;
	for (x=0; x<=m-size; x++)
		for (y=0; y<=n-size; y++)
		{
			if (board[x][y]==2) continue;
			flag=true;
			for (i=x; i<x+size; i++)
				for (j=y; j<y+size; j++)
				{
					if (i>x && board[i][j]==board[i-1][j])
					{
						flag=false;
						break;
					}
					if (i<x+size-1 && board[i][j]==board[i+1][j])
					{
						flag=false;
						break;
					}
					if (j>y && board[i][j]==board[i][j-1])
					{
						flag=false;
						break;
					}
					if (j<y+size-1 && board[i][j]==board[i][j+1])
					{
						flag=false;
						break;
					}
					if (board[i][j]==2)
					{
						flag=false;
						break;
					}
				}
			if (flag)
			{
				cnt[size]++;
				for (i=x; i<x+size; i++)
					for (j=y; j<y+size; j++)
						board[i][j]=2;
			}
		}
}

int main()
{
	int c,i,min;
	cin>>t;
	for (c=1; c<=t; c++)
	{
		//Do here
		cin>>m>>n;
		input();
		sum=0;
		if (m>n) min=n;
		else min=m;
		for (i=min; i>=1; i--)
			find(i);
		for (i=1; i<=min; i++)
			if (cnt[i]) sum++;
		cout<<"Case #"<<c<<": "<<sum<<endl;
		for (i=min; i>=1; i--)
			if (cnt[i]) cout<<i<<' '<<cnt[i]<<endl;
	}
	return 0;
}

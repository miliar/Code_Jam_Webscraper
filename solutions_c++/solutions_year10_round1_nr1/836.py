#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

ll t;
ll N, K;
string board[50];
int b[50][50];


int main()
{
	cin >> t;
	for(int a=1;a<=t;a++)
	{
		memset(b,0,sizeof(b));
		cin >> N >> K;
		for(int n=0;n<N;n++)
		{
			cin >> board[n];
		}
		for(int i=N-1;i>=0;i--)
		{
			int count=0;
			for(int j=N-1;j>=0;j--)
			{
				if(board[i][j] != '.')
				{
					board[i][j]=='R' ? b[count][N-i-1] = 1 : b[count][N-i-1] = 2;
					count++;
				}
			}
		}
		bool red=false,blue=false;
		for(int r=0;r<N;r++)
		{
			for(int c=0;c<=N-K;c++)
			{
				int tmp=b[r][c];
				if(tmp==0)
					break;
				for(int n=c+1;n<c+K;n++)
				{
					if(b[r][n]!=tmp) break;
					if(n==c+K-1)
					{
						tmp==1 ? red=true : blue=true;
					}
				}
			}
		}

		for(int c=0;c<N;c++)
		{
			for(int r=0;r<=N-K;r++)
			{
				int tmp=b[r][c];
				if(tmp==0)
					break;
				for(int n=r+1;n<r+K;n++)
				{
					if(b[n][c]!=tmp) break;
					if(n==r+K-1)
					{
						tmp==1 ? red=true : blue=true;
					}
				}
			}
		}

		for(int r=0;r<=N-K;r++)
		{
			for(int c=0;c<=N-K;c++)
			{
				int tmp=b[r][c];
				if(tmp==0)
					break;
				for(int n=c+1,m=r+1;n<c+K;n++,m++)
				{
					if(b[m][n]!=tmp) break;
					if(n==c+K-1)
					{
						tmp==1 ? red=true : blue=true;
					}
				}
			}
		}

		for(int r=0;r<=N-K;r++)
		{
			for(int c=K-1;c<N;c++)
			{
				int tmp=b[r][c];
				if(tmp==0)
					break;
				for(int n=r+1,m=c-1;n<r+K;n++,m--)
				{
					if(b[n][m]!=tmp) break;
					if(n==r+K-1)
					{
						tmp==1 ? red=true : blue=true;
					}
				}
			}
		}

		cout << "Case #" << a << ": ";
		if(red && blue) cout << "Both" << endl;
		else if(red) cout << "Red" << endl;
		else if(blue) cout << "Blue" << endl;
		else cout << "Neither" <<endl;
	}
}

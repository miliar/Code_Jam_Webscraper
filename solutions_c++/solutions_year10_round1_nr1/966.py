#include <fstream>

using namespace std;

ofstream os("o.txt");
ifstream is("in.txt");

int main()
{
	int ie2;
	is>>ie2;
	for(int ie=1;ie<=ie2;ie++)
	{
		int n,K;
		is>>n>>K;
		char board[51][51];
		for(int i=0;i<n;i++)
			is>>board[i];
		char rotated[51][51];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				rotated[i][j]='.';
		for(int i=n-1;i>=0;i--)
		{
			int cur=0;
			bool start=false;
			for(int j=n-1;j>=0;j--)
			{
				if(board[i][j]!='.')
					start=true;
				if(start)
				{
					if(board[i][j]=='.')
						start=false;
					else
					{
						rotated[n-cur-1][n-i-1]=board[i][j];
						cur++;
					}
				}
			}
		}
		int d[4][2]={{1,0},{0,1},{1,1},{1,-1}};
		bool winr=false,winb=false;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(rotated[i][j]=='.')continue;
				for(int k=0;k<4;k++)
				{
					bool found=false;
					for(int m=1;m<K;m++)
					{
						int x=i+d[k][0]*m;
						int y=j+d[k][1]*m;
						if(x<0||y<0||x>=n||y>=n)
							found=true;
						if(rotated[x][y]!=rotated[i][j])
							found=true;
						if(found)
							break;
					}
					if(found==false)
					{
						if(rotated[i][j]=='R')
							winr=true;
						else
							winb=true;
					}
				}
			}
		}
		os<<"Case #"<<ie<<": ";
		if(winr)
		{
			if(winb)
				os<<"Both\n";
			else
				os<<"Red\n";
		}
		else
		{
			if(winb)
				os<<"Blue\n";
			else
				os<<"Neither\n";
		}
	}
	return 0;
}
#include<iostream>
#include<fstream>
using namespace std;

int map[200][200];
int tmp[200][200];
int t,n=101;
void born()
{
	for(int i=1;i<=n+1;i++)
	{
		for(int j=1;j<=n+1;j++)
		{
			if(map[i][j]==0)
			{
				if(map[i-1][j]==1 && map[i][j-1]==1)
					tmp[i][j] = 1;
			}
			else
				tmp[i][j] = map[i][j];
		}
	}
	for(int i=0;i<=n+1;i++)
		for(int j=0;j<=n+1;j++)
			map[i][j] = tmp[i][j];
}

int dead()
{
	for(int i=1;i<=n+1;i++)
	{
		for(int j=1;j<=n+1;j++)
		{
			if(map[i][j]==1)
			{
				if(map[i-1][j]==0 && map[i][j-1]==0)
					tmp[i][j] = 0;
			}
			//tmp[i][j] = map[i][j];
		}
	}
	int b = 0;
	for(int i=0;i<=n+1;i++)
	{
		for(int j=0;j<=n+1;j++)
		{
			if(tmp[i][j] == 1)
			{
				b++;
			}
			//cout << tmp[i][j];
		}
	//	cout << endl;
	}
	return b;
}

int main()
{
	ofstream fout("ans");
	int x1,x2,y1,y2;
	cin >> t;
	int a;
	for(int m=1;m<=t;m++)
	{
		cin >> a;
		memset(map,0,sizeof(map));
		for(int i=0;i<a;i++)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			for(int j=x1+1;j<=x2+1;j++)
			{
				for(int k=y1+1;k<=y2+1;k++)
					map[j][k] = 1;
			}
		}
		int c = 0,r;
		while(true)
		{
			c++;
			born();
			r = dead();
		/*	for(int i=0;i<=n+1;i++)
			{
				for(int j=0;j<=n+1;j++)
				{
					//map[i][j] = tmp[i][j];
					//cout << tmp[i][j];
				}
				//cout << endl;
			}*/
			//cout << "r is " << r << endl;
			//system("pause");
			if(r==0)
				break;
			for(int i=0;i<=n+1;i++)
			{
				for(int j=0;j<=n+1;j++)
				{
					map[i][j] = tmp[i][j];
					//cout << tmp[i][j];
				}
				//cout << endl;
			}
			memset(tmp,0,sizeof(tmp));
		}
		fout << "Case #" << m << ": " << c << endl;
	}
}
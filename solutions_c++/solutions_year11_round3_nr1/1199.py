#include <iostream>
#include <vector>
#include <string>

using namespace std;
void doIt()
{
			int R,C;
		cin>>R>>C;
		string map[R];
		for (int i = 0; i<R;i++)
			cin>>map[i];
		for (int r = 0; r<R-1; r++)
		{
			for (int c = 0; c<C-1;c++)
			{
				if (map[r][c] == '#')
				{
					if ((map[r][c+1]!='#')or(map[r+1][c+1]!='#')or(map[r+1][c]!='#')) 
					{
						cout<<"Impossible"<<endl;
						return;
					}
					map[r][c] = '/';
					map[r][c+1] = '\\';
					map[r+1][c] = '\\';
					map[r+1][c+1] = '/';
				}
			}
		}
		
		for (int r = 0; r<R; r++)
		{
			if (map[r][C-1]=='#')
			{
				cout<<"Impossible"<<endl;
				return;
			}
		}
		
		for (int c = 0; c<C; c++)
		{
			if (map[R-1][c]=='#')
			{
				cout<<"Impossible"<<endl;
				return;
			}
		}
		for (int r = 0; r<R; r++)
			cout<<map[r]<<endl;
}

int main()
{
	int T;
	cin>>T;
	for (int t = 1;t<T+1;t++)
	{
		cout<<"Case #"<<t<<':'<<endl;
		doIt();
	}
	return 0;
}
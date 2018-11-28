#include <iostream>
#include <string>
#include <vector>
#include <string>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;

int main()
{
	int t,m,n,tmp;
	string a;
	cin >> t;

	for (int test=1;test<=t;test++)
	{
		cin >> m >> n;
		vector<string> tiles;
		string tmp;
		for (int i=0;i<m;i++)
		{
			cin >> tmp;
			tiles.push_back(tmp);
		}

		for (int i=0;i<m-1;i++)
		{
			for (int j=0;j<n-1;j++)
			{
				if (tiles[i][j]=='#' && tiles[i+1][j]=='#' && tiles[i][j+1]=='#' && tiles[i+1][j+1]=='#' )
				{
					
						tiles[i][j]='/';
						tiles[i+1][j]='\\';
						tiles[i][j+1]='\\';
						tiles[i+1][j+1]='/';
					
				}

			}
		}

		bool ok=true;
		for (int i=0;i<m;i++)
		{
			if (!ok) break;
			for (int j=0;j<n;j++)
			{
				if (tiles[i][j]=='#') 
					{
						ok=false;
						break;
				}
			}
		}

		cout << "Case #" << test << ":" << endl;
		if (!ok)
		{
				
				cout << "Impossible\n";
		}
		else
		{
			for (int i=0;i<m;i++)
				cout << tiles[i] << endl;

		}
				
	}
	//system("pause");
	return 0;
}
#include <iostream>

using namespace std;

int main()
{
	int t;
	int r, c;
    cin >> t;
    char a[100][100];
    
    for(int tt=1; tt<=t; tt++)
    {
		for(int i=0; i<100; i++) for(int j=0; j<100; j++) a[i][j] = '.';
		
		cin >> r >> c;
		
		for(int i=0; i<r; i++)
		{
			cin >> a[i];
			//cout << a[i] << endl;
		}
		
		bool ok = true;
		while(true)
		{
			bool found = false;			
			for(int i=0; i<r; i++)
			{
				//cout << a[i] << endl;;
				for(int j=0; j<c; j++)
				{
					if (a[i][j] == '#')
					{
						found = true;
						if (a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
						{
							a[i][j] = '/';
							a[i][j+1] = '\\';
							a[i+1][j] = '\\';
							a[i+1][j+1] = '/';
						}
						else
						{
							//cout << "here";
							ok = false;
							break;
						}
					}
				}
				if (!ok)
				{
					break;
				}
			}
			if (!ok) break;
			if (!found) break;
		}
		
		printf("Case #%d:\n", tt);
		if (!ok)
		{
			printf("Impossible\n");
		}
		else
		{
			for(int i=0; i<r; i++)
			{
				for(int j=0; j<c; j++)
				{
					cout << a[i][j];
				}
				cout << endl;
			}
		}
    }
    
    return 0;
}

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
 	freopen("A-large.in", "r", stdin);
 	freopen("A-large.out", "w", stdout);
    
    int T, R, C;
    
    cin >> T;
    
    for(int i = 0; i < T; i++)
    {
		cin >> R >> C;
		bool impossible = false;
		vector <string> s(R);
		int count = 0;
		for(int j = 0; j < R; j++)
		{
			cin >> s[j];
			for(int k = 0; k < C; k++)
				if(s[j][k] == '#')
					count++;
		}
		cout << "Case #" << i+1 << ':' << endl;
		if(count == 0)
		{
			for(int j = 0; j < R; j++)
				cout << s[j] << endl;
			continue;
		}
		else if(count % 4 == 0)
		{
			for(int j = 0; j < R; j++)
			{
				for(int k = 0; k < C; k++)
				{
					if(s[j][k] == '#')
					{
						if(k+1 >= C)
						{
							impossible = true;
							break;
						}
						if(s[j][k+1] == '#')
						{
							if(j+1 >= R)
							{
								impossible = true;
								break;
							}
							if(s[j+1][k] == '#' && s[j+1][k+1] == '#')
							{
								s[j][k] = '/'; s[j][k+1] = '\\';
								s[j+1][k] = '\\'; s[j+1][k+1] = '/';
								k++;
							}
							
						}
						else
						{
							impossible = true;
							break;
						}
					}
				}
				if(impossible)	break;

			}
			if(impossible)
				cout << "Impossible" << endl;
			else
			{
				for(int j = 0; j < R; j++)
					cout << s[j] << endl;
			}	
			
		}
		else
			cout << "Impossible" << endl;
    
	}	
    return 0;
}

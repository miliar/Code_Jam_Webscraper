#include<stdio.h>
#include<iostream>
#include<map>

using namespace std;

int main()
{
	int ncase,ccase;
	int n,l,h;
	int x,y,z,m;
	map<int,int> flag;
	
	cin >> ncase;
	for(ccase = 1;ccase <= ncase;ccase++)
	{
		cin >> n >> l >> h;
		
		flag.clear();
		for(x = 0;x < n;x++)
		{
			m = 0;
			cin >> z;
			for(y = l;y <= h;y++)
			{
				if(flag[y] == 0)
				{
					if(y % z == 0 || z % y == 0)
					{
						m = 1;
						flag[y] = 0;
					}
					else flag[y] = 1;
				}
			}
			//if(m == 0) break;
		}
		
		m = 1;
		cout << "Case #" << ccase << ": ";
		if(l == 1){cout << 1; m = 0;}
		else
		{
			for(x = l;x <= h;x++)
			{
				if(flag[x] == 0)
				{
					m = 0;
					cout << x;
					break;
				}
			}
		}
		if(m == 1) cout << "NO";
		cout << endl;
	}

    while(getchar()!=EOF);
    return 0;
}

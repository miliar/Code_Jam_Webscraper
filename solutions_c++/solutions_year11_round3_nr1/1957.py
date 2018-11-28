#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;


int d[51][51];

bool solve(int r, int c)
{
    for (int i = 1; i <= r - 1; i++)
    {
        for (int j = 1; j <= c - 1; j++)
            if (d[i][j] == 1)
			{
                if (d[i + 1][j] == 1 && d[i][j + 1] == 1 && d[i + 1][j + 1] == 1)
                {
                    d[i + 1][j] = 2;
                    d[i][j + 1] = 3;
                    d[i + 1][j + 1] = 4;
                }
            }
    }

	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			if (d[i][j] == 1 && (d[i][j + 1] != 3 || d[i + 1][j] != 2 || d[i + 1][j + 1] != 4))
			{
				return false;
			}
    return true;
}
int main()
{
    ifstream cin("A-large.in");
    ofstream cout("b.out");
    int r, c, count = 1;
    int tot;
    cin>>tot;

    while (tot--)
    {
        cin>>r>>c;
        char ch;

        memset(d, 0, sizeof(d));

        for (int i = 1; i <= r; i++)
		{
		  for (int j = 1; j <= c; j++)
		  {
			  cin>>ch;
			  if (ch == '#')d[i][j] = 1;
		  }
		}
        cout<<"Case #"<<count++<<":"<<endl;

        if (solve(r, c))
        {
            for (int i = 1; i <= r; i++)
            {
                for (int j = 1; j <= c; j++)
                    if (d[i][j] == 0)cout<<".";
                    else if (d[i][j] == 1)
                        cout<<"/";
                    else if (d[i][j] == 2)
                        cout<<"\\";
                    else if (d[i][j] == 3)
                        cout<<"\\";
                    else if (d[i][j] == 4)
                        cout<<"/";
                    cout<<endl;
            }
        }
        else cout<<"Impossible"<<endl;
    }
    return 0;
}

// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>	

using namespace std;

char b[50][50];

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int t=1;t<=T;t++)
	{
		cout << "Case #" << t <<":" << endl;
		int R,C;
		cin >> R >> C;
		for (int r=0;r<R;r++)
		{
			std::string s;
			cin >> s;
			for (int c=0;c<C;c++)
			{
				b[r][c] = s[c];
			}
		}

		for (int r=0;r<R-1;r++)
		{
			for (int c=0;c<C-1;c++)
			{
				if(b[r][c]=='#')
				{
					if(b[r][c+1]=='#'&&b[r+1][c]=='#'&&b[r+1][c+1]=='#')
					{
						b[r][c]='/';b[r][c+1]='\\';b[r+1][c]='\\';b[r+1][c+1]='/';
					}
					else
					{
						goto impossible;
					}
				}

			}
		}
		for (int r=0;r<R;r++)
			if(b[r][C-1] == '#')
				goto impossible;
		for (int c=0;c<C;c++)
			if(b[R-1][c] == '#')
				goto impossible;

		for (int r=0;r<R;r++) { for (int c=0;c<C;c++) cout << b[r][c]; cout << endl;};
		continue;

impossible:	cout << "Impossible" << endl;
		
	}
	return 0;
}



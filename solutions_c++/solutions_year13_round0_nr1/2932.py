#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;
string s[4];
int f(char c)
{
	string t(4,c);
	for(int i = 0; i < 4; ++i)
	    if(s[i] == t)
	        return 1;
	for(int i = 0; i < 4; ++i)
	{
		if(s[0][i] == c && s[1][i] == c && s[2][i] == c && s[3][i] == c)
		    return 1;
	}
	if(s[0][0] == c && s[1][1] == c && s[2][2] == c && s[3][3] == c)
	    return 1;
	if(s[0][3] == c && s[1][2] == c && s[2][1] == c && s[3][0] == c)
	    return 1;
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c = 1; c <= t;  ++c)
	{
		char re;
		for(int i = 0; i < 4; ++i)
		    cin>>s[i];
		bool over = 0;
		int ti = -1,tj;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			    if(s[i][j] == 'T')
			    {
					s[i][j] = 'X';
					ti = i;
					tj = j;
				}

		if(f('X'))
		{
			cout<<"Case #"<<c<<": X won"<<endl;
		}
		else
		{
			if(ti != -1)
				s[ti][tj] = 'O';
			if(f('O'))
			{
				cout<<"Case #"<<c<<": O won"<<endl;
			}
			else
			{
				bool draw = 1;
				for(int i = 0; i < 4 && draw; ++i)
				    for(int j = 0; j < 4; ++j)
				        if(s[i][j] == '.')
				        {
							draw = 0;
						    cout<<"Case #"<<c<<": Game has not completed"<<endl;
						    break;
						}
				if(draw)
				    cout<<"Case #"<<c<<": Draw"<<endl;
			}
		}
	}
	//system("pause");
	return 0;
}

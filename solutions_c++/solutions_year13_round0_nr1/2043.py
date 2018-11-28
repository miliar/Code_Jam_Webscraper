#include <iostream>
using namespace std;
char t[5][5];
int main()
{
	ios_base::sync_with_stdio(0);
	int tes;
	cin>>tes;
	for(int y=1; y<=tes; y++)
	{
		cout<<"Case #"<<y<<": ";
		int b=4;
		int sum=0;
		for(int i=1; i<=b; i++)
		{
			for(int j=1; j<=b; j++)
			{
				cin>>t[i][j];
				if(t[i][j]!='.')
				{
					sum++;
				}
			}
		}
		int git=0;
		for(int i=1; i<=b; i++)
		{
			git=0;
			for(int j=1; j<=4; j++)
			{
				if(t[i][j]=='T' || t[i][j]=='O')
				{
					git++;
				}
			}
			if(git==4)
			{
				cout<<"O won"<<endl;
				goto A;
			}
			git=0;
			for(int j=1; j<=4; j++)
			{
				if(t[i][j]=='T' || t[i][j]=='X')
				{
					git++;
				}
			}
			if(git==4)
			{
				cout<<"X won"<<endl;
				goto A;
			}
			git=0;
			for(int j=1; j<=4; j++)
			{
				if(t[j][i]=='T' || t[j][i]=='O')
				{
					git++;
				}
			}
			if(git==4)
			{
				cout<<"O won"<<endl;
				goto A;
			}
			git=0;
			for(int j=1; j<=4; j++)
			{
				if(t[j][i]=='T' || t[j][i]=='X')
				{
					git++;
				}
			}
			if(git==4)
			{
				cout<<"X won"<<endl;
				goto A;
			}
		}
		git=0;
		for(int i=1; i<=4; i++)
		{
			if(t[i][i]=='T' || t[i][i]=='O')
				{
					git++;
				}
		}
		if(git==4)
			{
				cout<<"O won"<<endl;
				goto A;
			}
		git=0;
			for(int i=1; i<=4; i++)
		{
			if(t[i][i]=='T' || t[i][i]=='X')
				{
					git++;
				}
		}
		if(git==4)
			{
				cout<<"X won"<<endl;
				goto A;
			}
			git=0;
		for(int i=1; i<=4; i++)
		{
			if(t[b-i+1][i]=='T' || t[b-i+1][i]=='O')
				{
					git++;
				}
		}
		if(git==4)
			{
				cout<<"O won"<<endl;
				goto A;
			}
		git=0;
			for(int i=1; i<=4; i++)
		{
			if(t[b-i+1][i]=='T' || t[b-i+1][i]=='X')
				{
					git++;
				}
		}
		if(git==4)
			{
				cout<<"X won"<<endl;
				goto A;
			}
		if(sum==16)
		{
			cout<<"Draw"<<endl;
		}
		else
		{
			cout<<"Game has not completed"<<endl;
		}
		A: ;
				
	}
	return 0;
}
/* 
10
OOTX
XXXX
XOXO
OXOO

.XTX
OXOX
.X.X
OOOO

.OTX
..O.
..X.
XXO.

....
....
....
....

XXOX
OXOO
XOOX
XOXO

..OO
....
XXXX
OOX.

XXTX
.X.O
OX.O
OXO.

O...
.O.X
..OX
XX.O

XXX.
XOOO
XOOO
XX..

XXOO
XOXO
OXTX
XOXO

*/



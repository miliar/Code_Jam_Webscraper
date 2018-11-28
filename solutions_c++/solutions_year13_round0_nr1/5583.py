#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;


int main()
{
	int t;
	int cont=1;
	char table[4][4];
	bool x,o,vazio;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		x=false;
		o=false;
		vazio=false;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>table[j][k];
				if(table[j][k]=='.')
					vazio=true;
			}
		}
		for(int j=0;j<4 && !x && !o;j++)
		{
			if(table[j][0]=='X')
			{
				x=true;
				for(int k=1;k<4 && x;k++)
				{
					if(table[j][k]!='X' && table[j][k]!='T')
						x=false;
				}
			}
			else if (table[j][0]=='O')
			{
				o=true;
				for(int k=1;k<4 && o;k++)
				{
					if(table[j][k]!='O' && table[j][k]!='T')
						o=false;
				}
			}
			else if (table[j][0]=='T')
			{
				if(table[j][1]=='X')
				{
					x=true;
					for(int k=2;k<4 && x;k++)
					{
						if(table[j][k]!='X' && table[j][k]!='T')
							x=false;
					}
				}
				else if (table[j][1]=='O')
				{
					o=true;
					for(int k=2;k<4 && o;k++)
					{
						if(table[j][k]!='O' && table[j][k]!='T')
							o=false;
					}
				}
			}
		}
		for(int j=0;j<4 && !x && !o;j++)
		{
			if(table[0][j]=='X')
			{
				x=true;
				for(int k=1;k<4 && x;k++)
				{
					if(table[k][j]!='X' && table[k][j]!='T')
						x=false;
				}
			}
			else if (table[0][j]=='O')
			{
				o=true;
				for(int k=1;k<4 && o;k++)
				{
					if(table[k][j]!='O' && table[k][j]!='T')
						o=false;
				}
			}
			else if(table[0][j]=='T')
			{
				if(table[1][j]=='X')
				{
					x=true;
					for(int k=2;k<4 && x;k++)
					{
						if(table[k][j]!='X' && table[k][j]!='T')
							x=false;
					}
				}
				else if (table[1][j]=='O')
				{
					o=true;
					for(int k=2;k<4 && o;k++)
					{
						if(table[k][j]!='O' && table[k][j]!='T')
							o=false;
					}
				}
			}
		}
		if(!x && !o)
		{
			if(table[0][0]=='X')
			{
				x=true;
				for(int k=1;k<4 && x;k++)
				{
					if(table[k][k]!='X' && table[k][k]!='T')
						x=false;
				}
			}
			else if (table[0][0]=='O')
			{
				o=true;
				for(int k=1;k<4 && o;k++)
				{
					if(table[k][k]!='O' && table[k][k]!='T')
						o=false;
				}
			}
			else if(table[0][0]=='T')
			{
				if(table[1][1]=='X')
				{
					x=true;
					for(int k=2;k<4 && x;k++)
					{
						if(table[k][k]!='X' && table[k][k]!='T')
							x=false;
					}
				}
				else if (table[1][1]=='O')
				{
					o=true;
					for(int k=2;k<4 && o;k++)
					{
						if(table[k][k]!='O' && table[k][k]!='T')
							o=false;
					}
				}
			}
		}
		if(!x && !o)
		{
			if(table[0][3]=='X')
			{
				x=true;
				for(int k=1;k<4 && x;k++)
				{
					if(table[k][3-k]!='X' && table[k][k]!='T')
						x=false;
				}
			}
			else if (table[0][3]=='O')
			{
				o=true;
				for(int k=1;k<4 && o;k++)
				{
					if(table[k][3-k]!='O' && table[k][3-k]!='T')
						o=false;
				}
			}
			else if(table[0][3]=='T')
			{
				if(table[1][2]=='X')
				{
					x=true;
					for(int k=2;k<4 && x;k++)
					{
						if(table[k][3-k]!='X' && table[k][3-k]!='T')
							x=false;
					}
				}
				else if (table[1][2]=='O')
				{
					o=true;
					for(int k=2;k<4 && o;k++)
					{
						if(table[k][3-k]!='O' && table[k][3-k]!='T')
							o=false;
					}
				}
			}
		}
		cout<<"Case #"<<cont<<": ";
		if(x)
			cout<<"X won\n";
		else if(o)
			cout<<"O won\n";
		else if(vazio)
			cout<<"Game has not completed\n";
		else
			cout<<"Draw\n";
		cont++;
	}
}
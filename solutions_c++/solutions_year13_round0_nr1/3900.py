#include <iostream>

using namespace std;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Problem A. Tic-Tac-Toe-Tomek

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int cases,counto,countx,countt;
	bool x,o,dot;
	char b[5][5];
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		x=false;
		o=false;
		dot=false;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>b[i][j];
				if(b[i][j]=='.')dot=true;
			}
		}
		for(int i=1;i<=4;i++)
		{
			counto=0;
			countx=0;
			countt=0;
			for(int j=1;j<=4;j++)
			{
				if(b[i][j]=='X')countx++;
				if(b[i][j]=='O')counto++;
				if(b[i][j]=='T')countt++;
				if(b[i][j]=='.')break;
			}
			if(countx+countt==4 && countt<=1)
			{
				x=true;
			}
			if(counto+countt==4 && countt<=1)
			{
				o=true;
			}
		}
		for(int i=1;i<=4;i++)
		{
			counto=0;
			countx=0;
			countt=0;
			for(int j=1;j<=4;j++)
			{
				if(b[j][i]=='X')countx++;
				if(b[j][i]=='O')counto++;
				if(b[j][i]=='T')countt++;
				if(b[j][i]=='.')break;
			}
			if(countx+countt==4 && countt<=1)
			{
				x=true;
			}
			if(counto+countt==4 && countt<=1)
			{
				o=true;
			}
		}
		counto=0;
		countx=0;
		countt=0;
		for(int j=1;j<=4;j++)
		{
			if(b[j][j]=='X')countx++;
			if(b[j][j]=='O')counto++;
			if(b[j][j]=='T')countt++;
			if(b[j][j]=='.')break;
		}
		if(countx+countt==4 && countt<=1)
		{
			x=true;
		}
		if(counto+countt==4 && countt<=1)
		{
			o=true;
		}
		counto=0;
		countx=0;
		countt=0;
		for(int j=1;j<=4;j++)
		{
			if(b[j][5-j]=='X')countx++;
			if(b[j][5-j]=='O')counto++;
			if(b[j][5-j]=='T')countt++;
			if(b[j][5-j]=='.')break;
		}
		if(countx+countt==4 && countt<=1)
		{
			x=true;
		}
		if(counto+countt==4 && countt<=1)
		{
			o=true;
		}
		cout<<"Case #"<<kase<<": ";
		if(x && !o)
		{
			cout<<"X won\n";
		}
		if(o && !x)
		{
			cout<<"O won\n";
		}
		if(x && o)
		{
			cout<<"Draw\n";
		}
		if(!x && !o)
		{
			if(dot)
				cout<<"Game has not completed\n";
			else
				cout<<"Draw\n";
		}
	}
	return 0;
}
#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
void main()
{
	int T;
	cin>>T;
	char g[4][4];
	for(int n=1;n<=T;n++)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>g[i][j];
			}
		}
		int x=0,o=0,t=0,b=0,flag=1;
		for(int i=0;i<4 && flag;i++)
		{
			switch(g[i][i])
			{
			case 'X':x++;break;
			case 'O':o++;break;
			case 'T':t++;break;
			case '.':b++;
			}
		}
		if(x==4)
		{
			cout<<"Case #"<<n<<": X won\n";
			flag=0;
		}
		else if(o==4)
		{
			cout<<"Case #"<<n<<": O won\n";
			flag=0;
		}
		else if(x==3 && t==1)
		{
			cout<<"Case #"<<n<<": X won\n";
			flag=0;
		}
		else if(o==3 && t==1)
		{
			cout<<"Case #"<<n<<": O won\n";
			flag=0;
		}
		x=0,t=0,o=0;
		for(int i=0;i<4 && flag;i++)
		{
			switch(g[i][3-i])
			{
			case 'X':x++;break;
			case 'O':o++;break;
			case 'T':t++;break;
			case '.':b++;
			}
		}
		if(x==4)
		{
			cout<<"Case #"<<n<<": X won\n";
			flag=0;
		}
		else if(o==4)
		{
			cout<<"Case #"<<n<<": O won\n";
			flag=0;
		}
		else if(x==3 && t==1)
		{
			cout<<"Case #"<<n<<": X won\n";
			flag=0;
		}
		else if(o==3 && t==1)
		{
			cout<<"Case #"<<n<<": O won\n";
			flag=0;
		}
		for(int i=0;i<4 && flag;i++)
		{
			x=0;
			o=0;
			t=0;
			for(int j=0;j<4;j++)
			{
				switch(g[i][j])
				{
				case 'X':x++;break;
				case 'O':o++;break;
				case 'T':t++;break;
				case '.':b++;
				}
			}
			if(x==4)
			{
				cout<<"Case #"<<n<<": X won\n";
				flag=0;
			}
			else if(o==4)
			{
				cout<<"Case #"<<n<<": O won\n";
				flag=0;
			}
			else if(x==3 && t==1)
			{
				cout<<"Case #"<<n<<": X won\n";
				flag=0;
			}
			else if(o==3 && t==1)
			{
				cout<<"Case #"<<n<<": O won\n";
				flag=0;
			}
		}
		for(int j=0;j<4 && flag;j++)
		{
			x=0;
			o=0;
			t=0;
			for(int i=0;i<4;i++)
			{
				switch(g[i][j])
				{
				case 'X':x++;break;
				case 'O':o++;break;
				case 'T':t++;break;
				case '.':b++;
				}
			}
			if(x==4)
			{
				cout<<"Case #"<<n<<": X won\n";
				flag=0;
			}
			else if(o==4)
			{
				cout<<"Case #"<<n<<": O won\n";
				flag=0;
			}
			else if(x==3 && t==1)
			{
				cout<<"Case #"<<n<<": X won\n";
				flag=0;
			}
			else if(o==3 && t==1)
			{
				cout<<"Case #"<<n<<": O won\n";
				flag=0;
			}
		}
		if(flag)
		{
			if(!b)
			{
				cout<<"Case #"<<n<<": Draw\n";
			}
			else
			{
				cout<<"Case #"<<n<<": Game has not completed\n";
			}
		}
	}
	getch();
}
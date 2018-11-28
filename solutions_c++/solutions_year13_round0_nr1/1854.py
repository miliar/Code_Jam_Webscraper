#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	int test;
	cin>>test;
	for(int i = 1; i<= test; i++)
	{
		//cout<<i;
		string st[4];
		cin>>st[0]>>st[1]>>st[2]>>st[3];
		int temp = 0;
		for(int j = 0; j< 4; j++)
		{
			string str ="";
			str =  st[j];
			//cout<<str<<endl;
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
				break;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";	
				temp = 1;
				break;
			}
		}
		string str = "";
		if(temp == 0)
		{
			str = str + st[0][0] + st[1][0] + st[2][0] + st[3][0];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";
				temp = 1;	
			}
		}
		if(temp == 0)
		{
			str = "";
			str = str + st[0][1] + st[1][1] + st[2][1] + st[3][1];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";	
				temp = 1;
			}
		}
		if(temp == 0)
		{
			str = "";
			str = str + st[0][2] + st[1][2] + st[2][2] + st[3][2];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";
				temp = 1;	
			}
		}
		if(temp == 0)
		{
			str = "";
			str = str +st[0][3] + st[1][3] + st[2][3] + st[3][3];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";
				temp = 1;	
			}
		}
		if(temp == 0)
		{
			str = "";
			str = str +st[0][0] + st[1][1] + st[2][2] + st[3][3];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";
				temp = 1;	
			}
		}
		if(temp == 0)
		{
			str = "";
			//cout<<st[2][1]<<"~"<<st[3][0]<<endl;
			str =str+ st[0][3] + st[1][2] + st[2][1] + st[3][0];
			if(str == "XXXX" ||str == "TXXX" || str == "XTXX"|| str == "XXTX" || str == "XXXT")
			{
				cout<<"Case #"<<i<<": X won\n";
				temp = 1;
			}
			else if(str == "OOOO" || str == "TOOO" || str == "OTOO"|| str == "OOTO" || str == "OOOT")
			{
				cout<<"Case #"<<i<<": O won\n";	
				temp = 1;
			}
		}
		if(temp == 0)
		{
			int flag = 0;
			for(int j = 0; j < 4 ;j++)
			{
				if(st[0][j] == '.' || st[1][j] == '.' || st[2][j] == '.' || st[3][j] == '.')
				{
					flag = 1;
					break;
				}
			}
			if(flag == 1)
			{
				cout<<"Case #"<<i<<": Game has not completed\n";
			}
			else 
			{
				cout<<"Case #"<<i<<": Draw\n";	
			}
		}
	}
	return 0;
}

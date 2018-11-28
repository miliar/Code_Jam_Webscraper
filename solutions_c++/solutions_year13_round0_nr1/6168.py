#include<iostream>
#include<math.h>
#include<string>
#include<vector>
#include<string.h>
using namespace std;
int t=0,c;
vector <string> ch;
void display(char chr,int r)
{
		c--;t++;
		for(int i=0;i<4;i++)
		{
			ch.pop_back();
		}
		if(chr==' ')
		{
			if(r>0)
			{
				cout<<"Case #"<<t<<": Game has not completed\n"; 
			}
			else
			{
				cout<<"Case #"<<t<<": Draw\n";
			}
		}
		else
		{
		cout<<"Case #"<<t<<": "<<chr<<" won\n";
		}
}
int main()
{
	int i,j,x=-1,z=0;
	
	string ch1;
	char cha;
	freopen("A-large.in","rt",stdin);
	freopen("A1.out","wt",stdout);
	cin>>c;
	while(c>0)
	{
		z=0;
		cha=' ';x=-1;
		for(i=0;i<4;i++)
		{
			cin>>ch1;
			ch.push_back(ch1);
		}
		
		
		for(i=0;i<4;i++)
		{
			ch1=ch[i];	
			x=ch1.find(".");
			if(x>=0)
			{
				z++;
				break;
			}
		
		}
		for(i=0;i<4;i++)
		{
			ch1=ch[i];	
			x=ch1.find("XXXX");
			if(x>=0)
			{
				cha='X';
				break;
			}
		
		}
		for(i=0;i<4;i++)
		{
			ch1=ch[i];	
			x=ch1.find("OOOO");
			if(x>=0)
			{
				cha='O';
				break;
			}
		}

		if(ch[0][0]=='X' && ch[1][1]=='X' && ch[2][2]=='X' && ch[3][3]=='X')
			cha='X';
		if(ch[0][0]=='O' && ch[1][1]=='O' && ch[2][2]=='O' && ch[3][3]=='O')
			cha='O';
		if(ch[0][0]=='X' && ch[1][0]=='X' && ch[2][0]=='X' && ch[3][0]=='X')
			cha='X';
		if(ch[0][0]=='O' && ch[1][0]=='O' && ch[2][0]=='O' && ch[3][0]=='O')
			cha='O';
		if(ch[0][1]=='X' && ch[1][1]=='X' && ch[2][1]=='X' && ch[3][1]=='X')
			cha='X';
		if(ch[0][1]=='O' && ch[1][1]=='O' && ch[2][1]=='O' && ch[3][1]=='O')
			cha='O';
		if(ch[0][2]=='X' && ch[1][2]=='X' && ch[2][2]=='X' && ch[3][2]=='X')
			cha='X';
		if(ch[0][2]=='O' && ch[1][2]=='O' && ch[2][2]=='O' && ch[3][2]=='O')
			cha='O';
		if(ch[0][3]=='X' && ch[1][3]=='X' && ch[2][3]=='X' && ch[3][3]=='X')
			cha='X';
		if(ch[0][3]=='O' && ch[1][3]=='O' && ch[2][3]=='O' && ch[3][3]=='O')
			cha='O';
		if(ch[3][0]=='X' && ch[2][1]=='X' && ch[1][2]=='X' && ch[0][3]=='X')
			cha='X';
		if(ch[3][0]=='O' && ch[2][1]=='O' && ch[1][2]=='O' && ch[0][3]=='O')
			cha='O';
		
			if(cha==' ')
			{
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("OOOT");
				if(x>=0)
				{
					cha='O';
					break;
				}
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("OOTO");
				if(x>=0)
				{
					cha='O';
					break;
				}
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("OTOO");
				if(x>=0)
				{
					cha='O';
					break;
				}
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("TOOO");
				if(x>=0)
				{
					cha='O';
					break;
				}
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("XXXT");
				if(x>=0)
				{
					cha='X';
					break;
				}
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("XXTX");
				if(x>=0)
				{
					cha='X';
					break;
				}
			
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("XTXX");
				if(x>=0)
				{
					cha='X';
					break;
				}
			
			}
			for(i=0;i<4;i++)
			{
				ch1=ch[i];	
				x=ch1.find("TXXX");
				if(x>=0)
				{
					cha='X';
					break;
				}
			
			}	
			if(ch[0][0]=='T' && ch[1][1]=='X' && ch[2][2]=='X' && ch[3][3]=='X')
			cha='X';
			if(ch[0][0]=='T' && ch[1][1]=='O' && ch[2][2]=='O' && ch[3][3]=='O')
			cha='O';
			if(ch[0][0]=='T' && ch[1][0]=='X' && ch[2][0]=='X' && ch[3][0]=='X')
			cha='X';
			if(ch[0][0]=='T' && ch[1][0]=='O' && ch[2][0]=='O' && ch[3][0]=='O')
			cha='O';
			if(ch[0][1]=='T' && ch[1][1]=='X' && ch[2][1]=='X' && ch[3][1]=='X')
			cha='X';	
			if(ch[0][1]=='T' && ch[1][1]=='O' && ch[2][1]=='O' && ch[3][1]=='O')
			cha='O';
			if(ch[0][2]=='T' && ch[1][2]=='X' && ch[2][2]=='X' && ch[3][2]=='X')
			cha='X';
			if(ch[0][2]=='T' && ch[1][2]=='O' && ch[2][2]=='O' && ch[3][2]=='O')
			cha='O';
			if(ch[0][3]=='T' && ch[1][3]=='X' && ch[2][3]=='X' && ch[3][3]=='X')
			cha='X';
			if(ch[0][3]=='T' && ch[1][3]=='O' && ch[2][3]=='O' && ch[3][3]=='O')
			cha='O';
			if(ch[3][0]=='T' && ch[2][1]=='X' && ch[1][2]=='X' && ch[0][3]=='X')
			cha='X';
			if(ch[3][0]=='T' && ch[2][1]=='O' && ch[1][2]=='O' && ch[0][3]=='O')
			cha='O';


			if(ch[0][0]=='X' && ch[1][1]=='T' && ch[2][2]=='X' && ch[3][3]=='X')
			cha='X';
			if(ch[0][0]=='O' && ch[1][1]=='T' && ch[2][2]=='O' && ch[3][3]=='O')
			cha='O';
			if(ch[0][0]=='X' && ch[1][0]=='T' && ch[2][0]=='X' && ch[3][0]=='X')
			cha='X';
			if(ch[0][0]=='O' && ch[1][0]=='T' && ch[2][0]=='O' && ch[3][0]=='O')
			cha='O';
			if(ch[0][1]=='X' && ch[1][1]=='T' && ch[2][1]=='X' && ch[3][1]=='X')
			cha='X';
			if(ch[0][1]=='O' && ch[1][1]=='T' && ch[2][1]=='O' && ch[3][1]=='O')
			cha='O';
			if(ch[0][2]=='X' && ch[1][2]=='T' && ch[2][2]=='X' && ch[3][2]=='X')
			cha='X';
			if(ch[0][2]=='O' && ch[1][2]=='T' && ch[2][2]=='O' && ch[3][2]=='O')
			cha='O';
			if(ch[0][3]=='X' && ch[1][3]=='T' && ch[2][3]=='X' && ch[3][3]=='X')
			cha='X';
			if(ch[0][3]=='O' && ch[1][3]=='T' && ch[2][3]=='O' && ch[3][3]=='O')
			cha='O';
			if(ch[3][0]=='X' && ch[2][1]=='T' && ch[1][2]=='X' && ch[0][3]=='X')
			cha='X';
			if(ch[3][0]=='O' && ch[2][1]=='T' && ch[1][2]=='O' && ch[0][3]=='O')
			cha='O';
		

			

			if(ch[0][0]=='X' && ch[1][1]=='X' && ch[2][2]=='T' && ch[3][3]=='X')
			cha='X';
			if(ch[0][0]=='O' && ch[1][1]=='O' && ch[2][2]=='T' && ch[3][3]=='O')
			cha='O';
			if(ch[0][0]=='X' && ch[1][0]=='X' && ch[2][0]=='T' && ch[3][0]=='X')
			cha='X';
			if(ch[0][0]=='O' && ch[1][0]=='O' && ch[2][0]=='T' && ch[3][0]=='O')
			cha='O';
			if(ch[0][1]=='X' && ch[1][1]=='X' && ch[2][1]=='T' && ch[3][1]=='X')
			cha='X';
			if(ch[0][1]=='O' && ch[1][1]=='O' && ch[2][1]=='T' && ch[3][1]=='O')
			cha='O';
			if(ch[0][2]=='X' && ch[1][2]=='X' && ch[2][2]=='T' && ch[3][2]=='X')
			cha='X';
			if(ch[0][2]=='O' && ch[1][2]=='O' && ch[2][2]=='T' && ch[3][2]=='O')
			cha='O';
			if(ch[0][3]=='X' && ch[1][3]=='X' && ch[2][3]=='T' && ch[3][3]=='X')
			cha='X';
			if(ch[0][3]=='O' && ch[1][3]=='O' && ch[2][3]=='T' && ch[3][3]=='O')
			cha='O';
			if(ch[3][0]=='X' && ch[2][1]=='X' && ch[1][2]=='T' && ch[0][3]=='X')
			cha='X';
			if(ch[3][0]=='O' && ch[2][1]=='O' && ch[1][2]=='T' && ch[0][3]=='O')
			cha='O';


			

			if(ch[0][0]=='X' && ch[1][1]=='X' && ch[2][2]=='X' && ch[3][3]=='T')
			cha='X';
			if(ch[0][0]=='O' && ch[1][1]=='O' && ch[2][2]=='O' && ch[3][3]=='T')
			cha='O';
			if(ch[0][0]=='X' && ch[1][0]=='X' && ch[2][0]=='X' && ch[3][0]=='T')
			cha='X';
			if(ch[0][0]=='O' && ch[1][0]=='O' && ch[2][0]=='O' && ch[3][0]=='T')
			cha='O';
			if(ch[0][1]=='X' && ch[1][1]=='X' && ch[2][1]=='X' && ch[3][1]=='T')
			cha='X';
			if(ch[0][1]=='O' && ch[1][1]=='O' && ch[2][1]=='O' && ch[3][1]=='T')
			cha='O';
			if(ch[0][2]=='X' && ch[1][2]=='X' && ch[2][2]=='X' && ch[3][2]=='T')
			cha='X';
			if(ch[0][2]=='O' && ch[1][2]=='O' && ch[2][2]=='O' && ch[3][2]=='T')
			cha='O';
			if(ch[0][3]=='X' && ch[1][3]=='X' && ch[2][3]=='X' && ch[3][3]=='T')
			cha='X';
			if(ch[0][3]=='O' && ch[1][3]=='O' && ch[2][3]=='O' && ch[3][3]=='T')
			cha='O';
			if(ch[3][0]=='X' && ch[2][1]=='X' && ch[1][2]=='X' && ch[0][3]=='T')
			cha='X';
			if(ch[3][0]=='O' && ch[2][1]=='O' && ch[1][2]=='O' && ch[0][3]=='T')
			cha='O';
				
		}
		display(cha,z);
		//cout<<"Game has not completed\n";
		
	}
	
						
	return 0;
}

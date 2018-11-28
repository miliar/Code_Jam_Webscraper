#include<fstream>
using namespace std;
int main()
{
	int a[4][4],win=0,p=0;
	char b[5];
	int s1=0,s2=0;
	int t=0;
	ifstream f("A-large.in");
	ofstream f1("output.txt");
	f>>t;
	for(int k=0;k<t;k++)
	{
		win=0;
		p=0;
		s1=0;
		s2=0;
		for(int i=0;i<4;i++)
		{
				f>>b;
				for(int j=0;j<4;j++)
				{
					if(b[j]=='X')
						a[i][j]=2;
					else if(b[j]=='O')
						a[i][j]=10;
					else if(b[j]=='T')
						a[i][j]=1;
					else 
					{
						a[i][j]=0;
						p=1;
					}
				}
		}
		for(int i=0;i<4;i++)
		{
			s1=a[i][0]+a[i][1]+a[i][2]+a[i][3];
			s2=a[0][i]+a[1][i]+a[2][i]+a[3][i];
			if(s1==8||s1==7||s2==8||s2==7)
			{	
				win=1;
				break;
			}
			else if(s1==40||s1==31||s2==40||s2==31)
			{
				win=2;
				break;
			}
		}
		if(win==0)
		{
			s1=a[0][0]+a[1][1]+a[2][2]+a[3][3];
			s2=a[0][3]+a[1][2]+a[2][1]+a[3][0];
			if(s1==7||s1==8||s2==8||s2==7)
			{	
				win=1;
			}
			else if(s1==40||s1==31||s2==40||s2==31)
			{
				win=2;
			}
		}
		f1<<"Case #"<<k+1<<": ";
		if(win==1)
			f1<<"X won";
		else if(win==2)
			f1<<"O won";
		else if(win==0&&p==0)
			f1<<"Draw";
		else f1<<"Game has not completed";
		f1<<endl;
	}
		/*
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				cout<<a[i][j]<< " ";
			cout<<endl;
		}*/
		return 0;
}
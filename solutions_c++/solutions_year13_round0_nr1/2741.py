#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int a[4][4],i,j,t,k,run,flag;
	char ch;

	ifstream fin("C:/a.txt");
	ofstream fout("C:/o.txt");

	fin>>t;
	for(k=0;k<t;k++)
	{
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fin>>ch;
				cout<<ch;
				if(ch=='.')
					a[i][j]=0;
				else if(ch=='X')
					a[i][j]=1;
				else if(ch=='O')
					a[i][j]=2;
				else if(ch=='T')
					a[i][j]=3;
			}
			cout<<endl;
		}
		//fin>>str;
		//check horizontal move
		flag=0;
		run=1;
		for(i=0;i<4;i++)
		{
			
			if((a[i][0]&a[i][1]&a[i][2]&a[i][3])>0)
			{
				flag=a[i][0];
				if(flag==3)
					flag=a[i][1];
				break;
			}

			else if((a[0][i]&a[1][i]&a[2][i]&a[3][i])>0)
			{
				flag=a[0][i];
				if(flag==3)
					flag=a[1][i];
				break;
			}

		}

		if(flag==0)
		{
		//check diagonal move
		if((a[0][0]&a[1][1]&a[2][2]&a[3][3])>0)
		{
			flag=a[0][0];
			if(flag==3)
				flag=a[1][1];
			
		}
		
		else if((a[0][3]&a[1][2]&a[2][1]&a[3][0])>0)
		{
			flag=a[0][3];
			if(flag==3)
				flag=a[1][2];
			
		}
		
		}
		//check if has empty cell
		if(flag==0)
		{
			for(i=0;i<4;i++)
			{
				for(j=0;j<4;j++)
				{
					if(a[i][j]==0)
					{
						flag=-1;
						break;
					}
				}
			if(flag==-1)
				break;
			}
		}

		if(flag==-1)
		 fout<<"Case #"<<(k+1)<<": Game has not completed"<<endl;
		else if(flag==1)
			fout<<"Case #"<<(k+1)<<": X won"<<endl;
		else if(flag==2)
			fout<<"Case #"<<(k+1)<<": O won"<<endl;
		else if(flag==0)
			fout<<"Case #"<<(k+1)<<": Draw"<<endl;
	}

	
	return 0;
}
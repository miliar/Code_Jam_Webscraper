#include<iostream>

using namespace std;

int check(char ch,char arr[4][4])
{
	//diagonal
	if((arr[0][0]==ch||arr[0][0]=='T')&&(arr[1][1]==ch||arr[1][1]=='T')&&(arr[2][2]==ch||arr[2][2]=='T')&&(arr[3][3]==ch||arr[3][3]=='T'))
		return 1;
	else if((arr[0][3]==ch||arr[0][3]=='T')&&(arr[1][2]==ch||arr[1][2]=='T')&&(arr[2][1]==ch||arr[2][1]=='T')&&(arr[3][0]==ch||arr[3][0]=='T'))
		return 1;
	else
	{
		int i,j;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(arr[i][j]!=ch&&arr[i][j]!='T')
					break;
			}
			if(j==4)
				return 1;
		}
		if(i==4)
		{
			int m,n;
			for(m=0;m<4;m++)
			{
				for(n=0;n<4;n++)
				{
					if(arr[n][m]!=ch&&arr[n][m]!='T')
						break;
				}
				if(n==4)
					return 1;
			}
			if(m==4)
				return 0;
		}
	}
	return 0;
}


int filled(char arr[4][4])
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(arr[i][j]=='.')
			{
				return 0;
			}
		}
	}
	return 1;
}

int main()
{
	int t;
	cin>>t;
	char arr[4][4];
	for(int k=0;k<t;k++)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>arr[i][j];
			}
		}
		cin.get();
		int a;
		a=check('X',arr);
		if(a==1)
			cout<<"Case #"<<k+1<<": X won";
		else if(a=check('O',arr))
			cout<<"Case #"<<k+1<<": O won";
		else if(filled(arr))
			cout<<"Case #"<<k+1<<": Draw";
		else
			cout<<"Case #"<<k+1<<": Game has not completed";
		cout<<endl;
	}
	return 0;
}
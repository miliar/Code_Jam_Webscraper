#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	int T=1,n;
	fflush(stdin);
	cin>>n;
	while(T<=n)
	{
		char A[4][4];
		for(int i =0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				fflush(stdin);
				cin>>A[i][j];
			}
		int flag =0, bl=0;		
		for(int i=0;i<4;i++)
		{
			flag = 0;			
			for(int j=0;j<4;j++)
			{
				if(A[i][j] == '.')
				{			
					flag = 0;				
					bl = 1;
					break;
				}
				if(A[i][j] == 'X')
				{
					if (flag == 2)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 1;					
						continue;
					}
				}
				if (A[i][j] == 'O')
				{
					if (flag == 1)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 2;
						continue;
					}
				}
			}
			if (flag==0)
				continue;
			else if (flag == 1)
			{
				cout<<"Case #"<<T<<": X won"<<"\n";
				break;
			}
			else if (flag == 2)
			{
				cout<<"Case #"<<T<<": O won"<<"\n";
				break;
			}
		}
		
		if (flag == 0)
		{
		for(int i=0;i<4;i++)
		{
			flag = 0;			
			for(int j=0;j<4;j++)
			{
				if(A[j][i] == '.')
				{			
					flag = 0;				
					bl = 1;
					break;
				}
				if(A[j][i] == 'X')
				{
					if (flag == 2)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 1;					
						continue;
					}
				}
				if (A[j][i] == 'O')
				{
					if (flag == 1)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 2;
						continue;
					}
				}
			}
			if (flag==0)
				continue;
			else if (flag == 1)
			{
				cout<<"Case #"<<T<<": X won"<<"\n";
				break;
			}
			else if (flag == 2)
			{
				cout<<"Case #"<<T<<": O won"<<"\n";
				break;
			}
		}
		}

		if (flag==0)
		{
			for(int i=0;i<4;i++)
			{
				if(A[i][i] == '.')
				{			
					flag = 0;				
					bl = 1;
					break;
				}
				if(A[i][i] == 'X')
				{
					if (flag == 2)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 1;					
						continue;
					}
				}
				if (A[i][i] == 'O')
				{
					if (flag == 1)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 2;
						continue;
					}
				}
			}			
			if (flag == 1)
			{
				cout<<"Case #"<<T<<": X won"<<"\n";
			}
			else if (flag == 2)
			{
				cout<<"Case #"<<T<<": O won"<<"\n";
			}

		}

		if (flag==0)
		{
			for(int i=0;i<4;i++)
			{
				if(A[i][3-i] == '.')
				{			
					flag = 0;				
					bl = 1;
					break;
				}
				if(A[i][3-i] == 'X')
				{
					if (flag == 2)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 1;					
						continue;
					}
				}
				if (A[i][3-i] == 'O')
				{
					if (flag == 1)
					{				
						flag = 0;					
						break;
					}
					if (flag == 0)
					{
						flag = 2;
						continue;
					}
				}
			}
			if (flag == 1)
			{
				cout<<"Case #"<<T<<": X won"<<"\n";
			}
			else if (flag == 2)
			{
				cout<<"Case #"<<T<<": O won"<<"\n";
			}
		}

		if (flag == 0 && bl == 0)
			cout<<"Case #"<<T<<": Draw"<<"\n";
		else if (flag ==0 && bl ==1)
			cout<<"Case #"<<T<<": Game has not completed"<<"\n";
		T++;
	}
}

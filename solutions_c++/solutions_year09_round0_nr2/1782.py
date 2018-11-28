#include<iostream>
using namespace std;
int H,W,altitude[201][201],con[201][201],array[201][201],flag[201],basin[201];
char res[201][201];
void search(int i,int j,int number)
{
	array[i][j]=number;
	if(con[i-1][j]==4)
	{
		search(i-1,j,number);
	}
	if(con[i+1][j]==1)
	{
		search(i+1,j,number);
	}
	if(con[i][j+1]==2)
	{
		search(i,j+1,number);
	}
	if(con[i][j-1]==3)
	{
		search(i,j-1,number);
	}
}

int main()
{
	int no;
	cin>>no;
	for(int kk=0;kk<no;kk++)
	{
	cin>>H>>W;
	for(int i=1;i<=H;i++)
	{
		for(int j=1;j<=W;j++)
		{
			cin>>altitude[i][j];
		}
	}

	for(int i=0;i<=H+1;i++)
	{
		altitude[i][0]=10000000;
		con[i][0]=0;
		altitude[i][W+1]=10000000;
		con[i][W+1]=0;
	}

	for(int i=0;i<=W+1;i++)
	{
		altitude[0][i]=10000000;
		con[0][i]=0;
		altitude[H+1][i]=10000000;
		con[H+1][i]=0;
	}

	int count=0,min=0;
	for(int i=1;i<=H;i++)
	{
		for(int j=1;j<=W;j++)
		{
			con[i][j]=0;
			min=altitude[i][j];
			if( altitude[i-1][j] < min )
			{
				min = altitude[i-1][j];
				con[i][j]=1;
			}
			if( altitude[i][j-1] < min )
			{
				min = altitude[i][j-1];
				con[i][j]=2;
			}
			
			if( altitude[i][j+1] < min )
			{
				min = altitude[i][j+1];
				con[i][j]=3;
			}
			if( altitude[i+1][j] < min )
			{
				min = altitude[i+1][j];
				con[i][j]=4;
			}
			if(con[i][j]==0)
			{
				basin[count]=(i-1)*W+j-1;
				count++;
			}
				
		}
	}
	/*cout<<"numbasin\n";
	cout<<count<<endl;
	cout<<"basins\n";*/
	for(int i=0;i<count;i++)
	{
//		cout<<(basin[i]/W)+1<<" "<<(basin[i]%W)+1<<endl;
		search( (basin[i]/W)+1 , (basin[i]%W)+1 , i+1);
		flag[i+1]=-1;
	}
/*	cout<<"array\n";
	for(int i=1;i<=H;i++)
	{
		for(int j=1;j<=W;j++)
		{
			cout<<array[i][j]<<" ";
		}
		cout<<endl;
	}*/

	int inc=0;
	for(int i=1;i<=H;i++)
	{
		for(int j=1;j<=W;j++)
		{
			int temp = array[i][j];
			if(flag[temp]==-1)
			{	
				flag[temp]=inc;
				res[i][j]='a'+flag[temp];
				inc++;
			}
			else
			{
				res[i][j]='a'+flag[temp];
			}
		}
		res[i][W+1]='\0';
	}
	
	cout<<"Case #"<<kk+1<<":\n";
	for(int i=1;i<=H;i++)
	{
		for(int j=1;j<=W;j++)
		{
			cout<<res[i][j]<<" ";
		}
		cout<<endl;
	}
	}
	return 0;
}

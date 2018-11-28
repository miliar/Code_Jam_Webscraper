#include<iostream>
using namespace std;
int height_map[100][100];
char label[100][100];
int sink=0;
int H,W;
char getsink(int i,int j)
{
	if(label[i][j]==' ')
	{
		int min_alt=height_map[i][j];
		char flag=0;
		if(i-1 >=0 && height_map[i-1][j]<min_alt )
		{
			flag=1;
			min_alt=height_map[i-1][j];
		}
		if( j-1 >=0 &&height_map[i][j-1]<min_alt )
		{
			flag=2;
			min_alt=height_map[i][j-1];
		}
		if( j+1 <W && height_map[i][j+1]<min_alt )
		{
			flag=3;
			min_alt=height_map[i][j+1];
		}
		if(i+1 <H && height_map[i+1][j]<min_alt )
		{
			flag=4;
			min_alt=height_map[i+1][j];
		}
		if(flag==0)
		{
			label[i][j]=97+sink;
			sink++;
		return label[i][j];
		}
		else if(flag==1)
		{
			label[i][j]=getsink(i-1,j);
		}
		else if(flag==2)
		{
			label[i][j]=getsink(i,j-1);
		}
		else if(flag==3)
		{
			label[i][j]=getsink(i,j+1);
		}
		else
			label[i][j]=getsink(i+1,j);
		return label[i][j];
	}
	else
		return label[i][j];
}










void get_label()
{
	sink=0;
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			cin>>height_map[i][j];
			label[i][j]=' ';
		}
	}
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			if(label[i][j]==' ')
			{
				label[i][j]=getsink(i,j);
			}
		}
	}
}

int main()
{
	int num_cases;
	cin>>num_cases;
	for(int n=0;n<num_cases;n++)
	{
		cin>>H>>W;
		get_label();
		cout<<"Case #"<<n+1<<":"<<'\n';
		for(int i=0;i<H;i++)
		{
			cout<<label[i][0];
			for(int j=1;j<W;j++)
			{
				cout<<' '<<label[i][j];
			}
			cout<<'\n';
		}
	}
	return(0);
}


#include <iostream>
#include <fstream>
using namespace std;

char a[60][60],b[60][60];
int n,k,ans[2];

int move[8][2]={{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{1,1},{-1,1},{1,-1}};

void rotate()
{
	int i,j;

	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			b[j][n-1-i]=a[i][j];

	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			a[i][j]=b[i][j];
}

void gravity()
{
	int i,j,u;
	
	for(j=0;j<n;j++)
	{
		i=n-1;
		u=n-1;

		while(i>=0)
		{
			while(u>=0&&a[u][j]!='.')
				u--;
			
			i=u-1;

			while(i>=0&&a[i][j]=='.')
				i--;
			
			if(i>=0)
			{
				a[u][j]=a[i][j];
				a[i][j]='.';
				--i;
				--u;
			}
		}
	}
}

bool inbound(int r,int c)
{
	return (r>=0&&r<n&&c>=0&&c<n);
}

bool checksub(int r,int c,int flag)
{
	int i,j,m,num;

	for(m=0;m<8;m+=2)
	{
		num=1;
		
		i=r+move[m][0];
		j=c+move[m][1];
		while(inbound(i,j))
			if((flag==0&&a[i][j]=='R')||(flag==1&&a[i][j]=='B'))
			{
				++num;
				i+=move[m][0];
				j+=move[m][1];
			}
			else
				break;

		i=r+move[m+1][0];
		j=c+move[m+1][1];
		while(inbound(i,j))
			if((flag==0&&a[i][j]=='R')||(flag==1&&a[i][j]=='B'))
			{
				++num;
				i+=move[m+1][0];
				j+=move[m+1][1];
			}
			else
				break;

		if(num>=k)
			return true;
	}

	return false;
}

void check()
{
	int i,j,flag;
	ans[0]=ans[1]=0;

	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			if(a[i][j]!='.')
			{
				if(a[i][j]=='R')
					flag=0;
				else
					flag=1;
				if(checksub(i,j,flag))
					ans[flag]=1;
			}
}


int main()
{
	int cases,t,i,j;
	ifstream fin("input1.txt");
	ofstream fout("output1.txt" );

	fin>>cases;
	for(t=1;t<=cases;t++)
	{
		fin>>n>>k;

		for(i=0;i<n;i++)
			fin>>a[i];
		
		/*
		cout<<"Matrix"<<endl;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				cout<<a[i][j]<<" ";
			cout<<endl;
		}
		*/

		rotate();
		
		/*
		cout<<"After rotate"<<endl;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				cout<<a[i][j]<<" ";
			cout<<endl;
		}
		*/
		
		gravity();
		
		/*
		cout<<"After gravity"<<endl;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				cout<<a[i][j]<<" ";
			cout<<endl;
		}
		*/

		check();
		
		fout<<"Case #"<<t<<": ";
		
		if(ans[0]==0&&ans[1]==0)
			fout<<"Neither"<<endl;
		else if(ans[0]==1&&ans[1]==0)
			fout<<"Red"<<endl;
		else if(ans[0]==0&&ans[1]==1)
			fout<<"Blue"<<endl;
		else
			fout<<"Both"<<endl;
	}

	fin.close();
	fout.close();


	return 0;
}
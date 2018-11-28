#include <iostream>
#include <fstream>
using namespace std;
int n,k;
int temp=1;
char a[50][50];
bool r=false,bl=false;
void find()
{
	r=false;
	bl=false;
	
	int temp1=n-1;
	for(int i=n-1;i>=0;i--)
	{
		temp1=n-1;
		for(int j=n-1;j>=0;j--)
			if(a[i][j]=='R'||a[i][j]=='B')
			{
				a[i][temp1--]=a[i][j];
				
			}
			for(int j=temp1;j>=0;j--)
				a[i][j]='.';
	}
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			if(a[i][j]=='R'&&r==false)
			{
				if(j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i][j+m]=='R')
						{
							if(m==k-1)
								r=true;
						}
						else
							break;
					}
				}
				if(i<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i+m][j]=='R')
						{
							if(m==k-1)
								r=true;
						}
						else
							break;
					}
				}
				if(i<=n-k&&j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i+m][j+m]=='R')
						{
							if(m==k-1)
								r=true;
						}
						else
							break;
					}
				}
			
				if(i>=k-1&&j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i-m][j+m]=='R')
						{
							if(m==k-1)
								r=true;
						}
						else
							break;
					}
				}

			}
			if(a[i][j]=='B'&&bl==false)
			{
				if(j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i][j+m]=='B')
						{
							if(m==k-1)
								bl=true;
						}
						else
							break;
					}
				}
				if(i<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i+m][j]=='B')
						{
							if(m==k-1)
								bl=true;
						}
						else
							break;
					}
				}
				if(i<=n-k&&j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i+m][j+m]=='B')
						{
							if(m==k-1)
								bl=true;
						}
						else
							break;
					}
				}
			
				if(i>=k-1&&j<=n-k)
				{
					for(int m=0;m<k;m++)
					{
						if(a[i-m][j+m]=='B')
						{
							if(m==k-1)
								bl=true;
						}
						else
							break;
					}
				}
			}
		}
}

int main()
{
	ofstream fout ("google.out");
    ifstream fin ("google.in");
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>n>>k;
		for(int p=0;p<n;p++)
			for(int q=0;q<n;q++)
				fin>>a[p][q];
		find();
		fout<<"Case #"<<i+1<<": ";
		
		if(r&&bl)
			fout<<"Both"<<endl;
		else if(r)
			fout<<"Red"<<endl;
		else if(bl)
			fout<<"Blue"<<endl;
		else
			fout<<"Neither"<<endl;
		
	}
	return 1;
}
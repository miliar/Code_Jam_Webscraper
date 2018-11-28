#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int cal(char * * a,int r,int c);


int main()
{
	
	ifstream fin("..\\A-large.in");
	ofstream fout("..\\testL.out");

	int testNum;
	fin>>testNum;
	for(int i=1;i<=testNum;i++)
	{
		int r,c;
		fin>>r>>c;
		char * * a=new char *[r];
		for(int j=0;j<r;j++)
		{
			a[j]=new char[c];
		}

		for(int m=0;m<r;m++)
		{
			for(int n=0;n<c;n++)
				fin>>a[m][n];
		}

		int rr=cal(a,r,c);
		cout<<"Case #"<<i<<":"<<endl;
		fout<<"Case #"<<i<<":"<<endl;

		if(rr==1)
		{
			for(int m=0;m<r;m++)
			{
				for(int n=0;n<c;n++)
				{
					cout<<a[m][n];
					fout<<a[m][n];
				}
				cout<<endl;fout<<endl;
			}
		}
		else
		{
			cout<<"Impossible"<<endl;
			fout<<"Impossible"<<endl;
		}

	}

	return 0;
}

int cal(char * * a,int r,int c)
{
	bool ok=true;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(a[i][j]=='#')
			{
				if(i<=r-2 && j<=c-2)
				{
					if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#')
					{
						a[i][j]='/';a[i][j+1]='\\'; a[i+1][j]='\\';a[i+1][j+1]='/';
					}
					else
					{
						ok=false;return -1;
					}
				}
				else
				{
					ok=false;return -1;
				}
			}
		}
	}

	if(ok==true)
		return 1;
	return -1;
}
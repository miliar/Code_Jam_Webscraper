#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<algorithm>

/////////////--------------stl library------------------///////////
#include<stack>

using namespace std;

typedef long long int int64;
typedef long double float64;
#define shift(x)  (1<<(x));
#define shift64(x) (((int64)(1))<<(x))
int max(int a,int b)
{
	if(a>=b)
		return a;
	else 
		return b;
}
int main()
{
	int ch;
	cin>>ch;
	for(int k=1;k<=ch;k++)
	{
		char arr[500][500];
		int row,col;
		cin>>row>>col;
		for(int i=1;i<=row;i++)
			scanf("%s",arr[i]);
		for(int i=1;i<row;i++)
		{
			for(int j=0;j<col-1;j++)
			{
				if(arr[i][j]=='#' && arr[i][j+1]=='#' && arr[i+1][j]=='#' && arr[i+1][j+1]=='#')
				{
					arr[i][j]='/';
					arr[i][j+1]='\\';
					arr[i+1][j]='\\';
					arr[i+1][j+1]='/';
				}
			}
		}
		int flag=0;
		for(int i=1;i<=row;i++)
		{
			for(int j=0;j<col;j++)
			{
					if(arr[i][j]=='#')
						flag=1;
				}
			}
		
		cout<<"Case #"<<k<<":\n";
		if(flag==1)
			cout<<"Impossible\n";
		else
		{
			for(int i=1;i<=row;i++)
				cout<<arr[i]<<endl;
			
		}
		
	}
	return 0;
}

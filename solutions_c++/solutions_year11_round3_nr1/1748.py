#include<iostream>
#include<vector>
#include<string>
using namespace std;

char mas[100][100];
char res[100][100];
bool dostep(int x,int y)
{
	if(mas[x+1][y]=='#' && mas[x+1][y]=='#' && mas[x][y+1]=='#')
	{
		mas[x][y]='/';
		mas[x+1][y]='\\';
		mas[x][y+1]='\\';
		mas[x+1][y+1]='/';
		return true;
	}
	return false;
}
	
int main()
{
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	int T;
	cin>>T;
	for(int k=0;k<T;k++)
	{
		printf("Case #%d:\n",k+1);
		string line;
		int m,n;
		int i,j;
		cin>>n>>m;
		for(i=0;i<100;i++)
			for(j=0;j<100;j++)
				mas[i][j]='.';
		for(i=0;i<n;i++)
		{
			cin>>line;
			for(j=0;j<m;j++)
			{
				mas[i][j]=line[j];
			}
		}
		bool pr=true;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(mas[i][j]=='#')
				{
					if(dostep(i,j)==false)
						pr=false;
				}
			}
		}
		if(pr==false)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for(i=0;i<n;i++)
			{
				if(i!=0)
					cout<<endl;
				for(j=0;j<m;j++)
					cout<<mas[i][j];
			}
			cout<<endl;
		}
		
	}

	
}
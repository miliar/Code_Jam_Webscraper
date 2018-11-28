#include<iostream>
int R,C;
char grid[100][100];
using namespace std;

void process()
{
	int counter = 0 ;
	for(int i = 0 ; i < R-1 ; i++)
	for(int j = 0 ; j < C-1 ; j++)
	if(grid[i][j]=='#'&&grid[i][j+1]=='#'&&grid[i+1][j]=='#'&&grid[i+1][j+1]=='#')
	{
		grid[i][j]='/';
		grid[i+1][j+1]='/';
		grid[i+1][j]=grid[i][j+1]='\\';
		counter++;
	};
	
	for(int i = 0 ; i < R ; i++)
	for(int j = 0 ; j < C ; j++)
	if(grid[i][j]=='#') {cout << "Impossible\n";
			     return ;
				};
	for(int i = 0 ; i < R ; i++)
	{	
		for(int j = 0 ; j < C ; j++)cout<<grid[i][j];
		cout << "\n";
	}	
}

int main()
{
	long long T;
	cin >> T ;
	for(int i=0; i < T ; i++)
	{
		cin >> R >> C ;
		for(int x = 0 ; x < R ; x++)for(int j = 0 ; j < C ; j++)cin >> grid[x][j];
		cout <<"Case #"<<(i+1)<<":\n";
		process();
	}
}

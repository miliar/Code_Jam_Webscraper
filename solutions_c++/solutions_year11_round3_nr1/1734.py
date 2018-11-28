#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
using namespace std;

ifstream fin("C:\\Users\\Edward\\A-large.in");
ofstream fout("C:\\Users\\Edward\\A-large.out");
#define cin fin
#define cout fout

int n , m;
int sum;
char map[100][100]; 
bool Lim( int x , int y )
{
	if( map[x][y] == '#' )
	{ return true; }
	return false;
}
bool DFS( int x , int y )
{
	int tx , ty;
	map[x][y] = '/';
	tx = x;
	ty = y + 1;
	if( Lim( tx , ty ) )
	{ 
		map[tx][ty]='\\'; 
	}
	else { return false; }
	tx = x + 1;
	ty = y;
	if( Lim( tx , ty ) )
	{ map[tx][ty] = '\\'; }
	else { return false; }
	tx = x + 1;
	ty = y + 1;
	if( Lim( tx , ty ) )
	{ map[tx][ty] = '/'; }
	else
	{ return false; }
	return true;
}

int main()
{
	int t , cas;
	cin>>t;
	int i , j;
	cas = 0;
	while( t-- )
	{
		++cas;
		cin>>n>>m;
		sum = 0;
		for( i = 0 ; i < n ; ++i )
		{
			for( j = 0 ; j < m ; ++j )
			{
				cin>>map[i][j];
			}
		}
		for( i = 0 ; i < n ; ++i )
		{
			for( j = 0 ; j < m ; ++j )
			{

				if( map[i][j] == '.' )
				{ map[i][j] = '.'; continue; }

				if( map[i][j] != '#' ){ continue; }

				if( !DFS( i , j ) )
				{ break; }
			}
			if( j < m ){ break; }
		}
		cout<<"Case #"<<cas<<":"<<endl;
		if( i < n )
		{ cout<<"Impossible"<<endl; }
		else
		{
			for( i = 0 ; i < n ; ++i )
			{
				for( j = 0 ; j < m ; ++j )
				{
					cout<<map[i][j];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}
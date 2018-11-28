#include<iostream>
using namespace std;
int H,W,value[101][101];
char map[101][101],dex;
char flood(int y,int x)
{
	if ( map[y][x] )
		return map[y][x];
	int mini = value[y][x],ty,tx;
	if ( y -1>= 0 )
	{
		if ( mini > value[y-1][x])
		{
			mini = value[y-1][x];
			ty = y-1;
			tx = x;
		}
	}
	if ( x -1 >=0 )
	{
		if (mini > value[y][x-1])
		{
			mini = value[y][x-1];
			ty = y;
			tx = x-1;
		}
	}
	if (  x + 1 < W )
	{
		if ( mini > value[y][x+1])
		{
			mini = value[y][x+1];
			ty = y;
			tx = x+1;
		}
	}
	if ( y +1 < H )
	{
		if ( mini > value[y+1][x])
		{
			mini = value[y+1][x];
			ty = y+1;
			tx = x;
		}
	}





	if ( mini == value[y][x] )
	{
		return map[y][x] = dex++;
	}
	return map[y][x] = flood(ty,tx);
}
int main()
{
	int T,i,j,k;
	cin >> T;
	for ( i=1; i<= T; i++)
	{
		memset(map,0,sizeof(map));
		cin >> H >> W;
		for ( j=0; j< H; j++ )
		{
			for ( k =0; k<W; k++ )
			{
				cin >> value[j][k];
			}
		}
		dex = 'a';
		cout<<"Case #"<<i <<":\n";
		for ( j =0; j< H; j++ )
		{
			cout<<flood(j,0);
			for ( k =1; k < W; k++ )
			{
				cout<<' '<<flood(j,k);
			}
			cout<<endl;
		}
	}

	return 0;
}
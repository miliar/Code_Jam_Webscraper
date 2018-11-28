#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;


int diffx[] = {0,-1,1,0};
int diffy[] = {-1,0,0,1};

int map[102][102];
int dirs[102][102];
int basins[102][102];
int h,w;
int currentbasin = 0;

		
bool oob(int i, int j)
{
	if(i < 0 || j < 0 || i >= h || j >= w)
			return true;
	
	return false;
}

void set_direction(int i, int j)
{
	int best = 999999999;
	for(int k = 1; k <= 4; k++)
	{
		int newi =i+diffy[k-1], newj =  j+diffx[k-1];
		if(!oob(newi,newj) && map[newi][newj]*100+k < best && map[newi][newj] < map[i][j])
		{
			best = map[newi][newj]*100+k;
		}
	}
	
	if(best != 999999999)
	{
		dirs[i][j] = best%100;
	}
	
}

int set_basin(int i, int j)
{
	
	if(basins[i][j])
		return basins[i][j];
	
	if(dirs[i][j] == 0)
	{
		basins[i][j] = currentbasin;
		currentbasin++;
		return currentbasin-1;
	}
	
	
	int k = dirs[i][j]-1;		
	int newi =i+diffy[k], newj =  j+diffx[k];
	
	return basins[i][j] = set_basin(newi,newj);
	
	
}


int main()
{
	int t;
	cin>>t;
	
	for(int testcase = 0; testcase < t; testcase++)
	{
		cin>>h>>w;
		
		memset(map,0,sizeof(map));
		
		for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++)
		{
			cin>>map[i][j];
		
		}
		
		memset(dirs,0,sizeof(dirs));
		
		for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++)
		{
			set_direction(i,j);
		}
		
		currentbasin = 1;
		memset(basins,0,sizeof(basins));
		
		for(int i = 0; i < h; i++)
		for(int j = 0; j < w; j++)
		{
				{set_basin(i,j);
			}
		}
		
		
		cout<<"Case #"<<testcase+1<<":\n";
		

		for(int i = 0; i < h; i++,cout<<endl)
		for(int j = 0; j < w; j++)
		{
			cout<<char('a'+basins[i][j]-1);
			if(i < h)
				cout<<" ";
		}
		
		
		
	}
}



#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;


typedef long long int64;


class index{
public: int i;
public: int j;
};


int altitudes[100][100];
char result[100][100];
int T, H, W;
char flag;
char lable(int h , int w);

void main(){
	freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Watersheds\\input.txt", "rt", stdin);
	freopen("D:\\Visual Studio 2008\\Projects\\googlejam2008\\Watersheds\\output.txt", "wt", stdout);



	vector<index> v;

	scanf("%d", &T);
	for(int k = 0; k < T; k ++)
	{
		scanf("%d %d", &H, &W);
		flag = 'a';
		for(int i = 0; i < H; i ++)
			for(int j = 0; j < W; j ++)
			{
				scanf("%d", &altitudes[i][j]);	
				result[i][j] = 0;
			}
		for(int i = 0; i < H; i ++)
			for(int j = 0; j < W; j ++)
			{
				if(result[i][j] == 0)
					lable(i, j);
			}
				
		printf("Case #%d:\n", k + 1);
		for(int i = 0; i < H; i ++)
		{	
			for(int j = 0; j < W; j ++)
				printf("%c ", result[i][j]);
			printf("\n");
		}

	}
}

void findLowest(int h, int w, int &i, int &j)
{
	i = j = -1;
	int low = altitudes[h][w];
	if(h - 1 >= 0)
	{//north
		if(altitudes[h-1][w] < low)
		{
			low = altitudes[h-1][w];
			i = h-1; j = w;
		}
	}
	if(w - 1 >= 0)
	{//west
		if(altitudes[h][w-1] < low)
		{
			low = altitudes[h][w-1];
			i = h; j = w-1;
		}
	}
	if(w+1 < W){
	//east
				if(altitudes[h][w+1] < low)
		{
			low = altitudes[h][w+1];
			i = h; j = w + 1;
		}
	}
	if(h+1<H)
	{
				if(altitudes[h+1][w] < low)
		{
			i = h+1; j = w;
		}
	}
}

char lable(int h , int w)
{
	int i , j;
	if(result[h][w] == 0)
	{
		findLowest(h, w, i, j);
		if(i != -1)
		{
			char l = lable(i, j);
			result[h][w] = l;
		}
		else
		{
			result[h][w] = flag;
			flag ++;
		}
	}
	return result[h][w];
}
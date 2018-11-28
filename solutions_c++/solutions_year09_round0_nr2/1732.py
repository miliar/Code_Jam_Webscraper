#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int T;
int H, W;
int fmap[100][100] = {};
char basin[100][100] = {};

int dH[4] = {-1, 0, 0, 1};
int dW[4] = {0, -1, 1, 0};
int flowToH[100][100] = {};
int flowToW[100][100] = {};
//int comeFromH[100][100] = {};
//int comeFromW[100][100] = {};

void dfs(int j, int k, char current)
{
	if(basin[j][k] != 0) return;
	basin[j][k] = current;
	if(flowToH[j][k] != j || flowToW[j][k] != k)
	{
		dfs(flowToH[j][k], flowToW[j][k], current);
	}
	//if(comeFromH[j][k] != j || comeFromW[j][k] != k)
	//{
	//	dfs(comeFromH[j][k], comeFromW[j][k], current);
	//}
	for(int m = 0; m < 4; m++)
	{
		int tempH = j + dH[m];
		int tempW = k + dW[m];
		if(tempH >= 0 && tempH < H && tempW >= 0 && tempW < W
		    && flowToH[tempH][tempW] == j && flowToW[tempH][tempW] == k)
		{
			dfs(tempH, tempW, current);
		}
	}
}

int main() 
{
    freopen("B-small.in", "r", stdin);
    ofstream fp("B-small.out");


	cin >> T;
	for(int i = 0; i < T; i++)
	{
		memset(basin, 0, sizeof(basin));
		cin >> H >> W;
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				cin >> fmap[j][k];
			}
		}
		//cout<<"Case"<<i<<endl;
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				int curH = j;
				int curW = k;
				for(int m = 0; m < 4; m++)
				{
					int tempH = j + dH[m];
					int tempW = k + dW[m];
					if(tempH >= 0 && tempH < H && tempW >= 0 && tempW < W 
					    && fmap[tempH][tempW] < fmap[curH][curW])
					{
						curH = tempH;
						curW = tempW;
					}
				}
				flowToH[j][k] = curH;
				flowToW[j][k] = curW;
				//comeFromH[curH][curW] = j;
				//comeFromW[curH][curW] = k;
				//cout << j << " " << k << " " << curH << " " << curW <<endl;
			}
		}
		char current = 'a';
		fp << "Case #" << i+1 << ": " << endl;
		for(int j = 0; j < H; j++)
		{
			for(int k = 0; k < W; k++)
			{
				//cout << basin[j][k] << " ";
				if(basin[j][k] == 0)
				{
					dfs(j, k, current);
					current ++;
				}
				fp << basin[j][k] << " ";
			}
			//cout << endl;
			fp << endl;
		}

	}

    fp.close();
    return 0;
}

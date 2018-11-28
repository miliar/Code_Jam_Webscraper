#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;



struct  node
{
	int x,  y;
	node(){x=-1;y=-1;}
} ;

node mapxy[100][100];
int H,  W;

int mapI[100][100];

char outp[100][100];


int direct[4][2] = {{0,-1},{-1,0},{1,0},{0,1}}; //x,y
int main()
{
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #"<<i<<":" << endl;
		cin >>H >> W;
		for (int j = 0; j <H; ++j)
			for(int k = 0; k < W; ++k)
			{
				cin >> mapI[j][k];
			}

			
			for (int j = 0; j <H; ++j)
				for(int k = 0; k < W; ++k)
				{
					int x = -1, y = -1;
					int curV = mapI[j][k];
					for (int kk = 0; kk < 4; ++kk)
					{
						if (
							j + direct[kk][1] < H &&
							j + direct[kk][1] >=0 &&
							k + direct[kk][0] >=0 &&
							k + direct[kk][0] < W &&
							curV > mapI[j + direct[kk][1]][ k + direct[kk][0]])
						{
							curV = mapI[j + direct[kk][1]][ k + direct[kk][0]];
							x = k + direct[kk][0];
							y = j + direct[kk][1];
						}
					}
					mapxy[j][k].x  = x;
					mapxy[j][k].y = y;
				}

				memset(outp, 0, sizeof outp);

				char nextC = 'a';
				for (int j = 0; j <H; ++j)
					for(int k = 0; k < W; ++k)
					if (outp[j][k] == 0)
					{
						if (mapxy[j][k].x==-1 && 
							mapxy[j][k].y==-1)
						{
							outp[j][k] = nextC++;
						}
						else
						{
							int x, y;
							x = mapxy[j][k].x;
							y = mapxy[j][k].y;

							while (mapxy[y][x].x != -1 && mapxy[y][x].y != -1)
							{

								int x1, y1;
								x1= mapxy[y][x].x;
								y1= mapxy[y][x].y;
								x= x1,y=y1;
							}
							outp[j][k] = outp[y][x];
							if (outp[j][k] == 0)
							{
								outp[j][k] = outp[y][x]=nextC++;
							}
						}
					}

					for (int j = 0; j <H; ++j){
						for(int k = 0; k < W; ++k)
						{
							cout << outp[j][k] << " ";
						}
						cout << endl;}
	}

	return 1;
}
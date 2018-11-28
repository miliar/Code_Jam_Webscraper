#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

const char basinName[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

const int maxAl = 10000000;

int main(void){
	int T;
	
	cin >> T;

	int elevMap[110][110];
	char elevMapCH[110][110];
	
	for (int i=0; i < T; i++) 
	{
		cout << "Case #" << (i+1) <<":\n";
		for (int kx=0; kx < 110; kx++)
			for(int ky=0; ky < 110; ky++) 
			{
				elevMap[ky][kx] = 0;
				elevMapCH[ky][kx] = '1';
			}

		int H;
		int W;
		cin >> H;
		cin >> W;

		for (int ky=0; ky < H; ky++) 
		{
			for (int kx = 0; kx < W; kx++)
			{
				cin >> elevMap[ky][kx];
			}
		}

		int actualName = 0;

		int numOfBasins = 0;
		for (int ky = 0; ky < H; ky++)
		{
			for (int kx = 0; kx < W; kx++)
			{
				int lowest = maxAl;

				int lowestNorth = (ky > 0)	    ? elevMap[ky-1][kx] : maxAl;
				int lowestWest  = (kx > 0)		? elevMap[ky][kx-1] : maxAl;
				int lowestEast  = (kx < (W-1))  ? elevMap[ky][kx+1] : maxAl;
				int lowestSouth = (ky < (H-1))  ? elevMap[ky+1][kx] : maxAl;

				if ((elevMap[ky][kx] <= lowestNorth) &&
					(elevMap[ky][kx] <= lowestWest)  &&
					(elevMap[ky][kx] <= lowestEast)  &&
					(elevMap[ky][kx] <= lowestSouth))
				{
					elevMapCH[ky][kx] = basinName[actualName++];
					numOfBasins++;					
				}
					
			}
		}

		
		if (numOfBasins == 0)
		{
			actualName = 0;
			for (int ky=0; ky < H; ky++) 
			{
				for (int kx = 0; kx < W; kx++)
				{
					elevMapCH[ky][kx] = basinName[actualName++];
				}				
			}			
		} else 
		{
			for (int ky = 0; ky < H; ky++)
			{
				for (int kx = 0; kx < W; kx++)
				{
					int ny = ky;
					int nx = kx;

					while (elevMapCH[ny][nx] == '1') 
					{		
						int lowestNorth = (ny > 0)	    ? elevMap[ny-1][nx] : maxAl;
						int lowestWest  = (nx > 0)		? elevMap[ny][nx-1] : maxAl;
						int lowestEast  = (nx < (W-1))  ? elevMap[ny][nx+1] : maxAl;
						int lowestSouth = (ny < (H-1))  ? elevMap[ny+1][nx] : maxAl;

						if ((lowestNorth != maxAl) && ((lowestNorth <= lowestWest) && (lowestNorth <= lowestEast) && (lowestNorth <= lowestSouth)))
						{
							nx = nx;
							ny = ny-1;
						} 
						else if ((lowestWest != maxAl) && ((lowestWest <= lowestEast) && (lowestWest <= lowestSouth)))
						{
							nx = nx-1;
							ny = ny;
						} 
						else if ((lowestEast != maxAl) && ((lowestEast <= lowestSouth)))
						{
							nx = nx+1;
							ny = ny;
						} else {
							nx = nx;
							ny = ny+1;
						}
					}
					elevMapCH[ky][kx] = elevMapCH[ny][nx];
				}
			}
		}

		int sortArray[26];
		char origin[26];
		for (int m=0; m < 26; m++)
		{
			sortArray[m] = -1;
			origin[m] = '1';
		}

		int actualPositionSort = 0;
		for (int ky=0; ky < H; ky++) 
		{
			for (int kx = 0; kx < W; kx++)
			{
				char kk = elevMapCH[ky][kx];

				bool existsInArray = false;
				for (int rr = 0; rr < 26; rr++)
				{
					if (origin[rr] == kk)
					{
						existsInArray = true;
						break;
					}
				}
				if (existsInArray == false)
				{
					origin[actualPositionSort++] = kk;
				}
			}
		}


		for (int ky=0; ky < H; ky++) 
		{
			for (int kx = 0; kx < W; kx++)
			{
				int newPosition = -1;
				char kk = elevMapCH[ky][kx];
				for (int rr = 0; rr < 26; rr++)
				{
					if (origin[rr] == kk)
					{
						newPosition = rr;
						break;
					}
				}		
				elevMapCH[ky][kx] = basinName[newPosition];
			}
		}





		for (int ky=0; ky < H; ky++) 
		{
			for (int kx = 0; kx < W; kx++)
			{
				cout << elevMapCH[ky][kx] << " ";
			}
			cout <<"\n";
		}
	}
}
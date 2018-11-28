#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;
int cost[120][280];
int arr[280];
int diff(int a, int b)
{
	if(a==256||b==256)
		return 0;
	else
		return abs(a-b);
}
int main()
{
	FILE *in=fopen("msmin.txt", "r");
	FILE *out=fopen("msmout.txt", "w");
	//I want the cost to pass through a certain distance on the array, with a specific ending
	//which may be gained by taking the previous length, looking at the costs for all endings there
	//If the new block I want to push is too different, I can change it normally, delete it completely, insert one or more between it and the old pixel
	int T;
	fscanf(in, "%d", &T);
	for(int t=0; t<T; t++)
	{
		for(int i=0; i<120; i++)
			for(int j=0; j<280; j++)
				cost[i][j]=1000000000;
		for(int i=0; i<280; i++)
			arr[i]=256;
		//Warning: There are cases where I want to do 2 or more of insert, delete, change
		//eg difference 6, insert costs 3, max diff 2
		//I would have to change the new number by 2, and insert one between them, to get optimal results
		//I think this can be safely dealt with by checking all insertions in place rather than on to the next row
		cost[0][256]=0;
		int D, I, M, N;
		fscanf(in, "%d%d%d%d", &D, &I, &M, &N);
		for(int i=0; i<N; i++)
		{
			fscanf(in, "%d", &arr[i+1]);
		}
		for(int i=0; i<N; i++)
		{
			cost[i+1][arr[i+1]]=cost[i][256];
			for(int j=0; j<=256; j++)	//old cost
			{
				for(int k=0; k<256; k++)	//new cost
				{
					if(k==j)
					{
						cost[i+1][k]=min(cost[i+1][k], cost[i][j]+D);	//deleting the new element
					}
					if(j==256)
					{
						cost[i+1][k]=min(cost[i+1][k], cost[i][j]+diff(arr[i+1], k));	//If this is the first element, we can change it to whatever we want
					}
					if(j!=256 && diff(k, j)<=M)	//If we can just change our new point
					{
						cost[i+1][k]=min(cost[i+1][k], cost[i][j]+diff(k, arr[i+1]));	//An alternative cost is the cost of changing to this number
					}
				}
				cost[i+1][256]=min(cost[i+1][256], cost[i][256]+D);	//Carrying deletion onward for a late start
			}
			for(int k=0; k<256; k++)	//Here I do all the insertion things
			{
				for(int j=0; j<256; j++)
				{
					//The number of things I need to insert to make j from k should be difference/M, rounded up
					//so the cost is ((diff-1)/M+1)*I
					if(M!=0)
						cost[i+1][j]=min(cost[i+1][j], cost[i+1][k]+((diff(j, k)-1)/M+1)*I);
				}
			}
		}
		//So, I should now have all the final costs stored at N
		int mn=1000000000;
		for(int i=0; i<=256; i++)
		{
			mn=min(mn, cost[N][i]);
		}
		fprintf(out, "Case #%d: %d\n", t+1, mn);
	}
	return 0;
}
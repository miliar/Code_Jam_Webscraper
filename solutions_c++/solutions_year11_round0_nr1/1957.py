//Author : Nitin Gangahar
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <cstring>
#include <set>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define isok(x,y) (x>=0 && x<R && y>=0 && y<C)
#define MAX 103
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;
char COL[MAX];
int BUT[MAX];
int ORANGE[MAX];
int BLUE[MAX];
int main()
{
	int T;
	int cases = 1;
	scanf("%d",&T);
	while(T--)
	{
		int currO = 1;
		int currB = 1;
		int nxtO = 0;
		int nxtB = 0;
		int ans = 0;
		int idx = 0;
		int totO = 0;
		int totB = 0;
		int steps;
		scanf("%d",&steps);
		for(int i=0;i<steps;i++)
		{
				char col;
				int but;
				scanf(" %c %d",&col,&but);
				//printf("%c %d\n",col,but);
				COL[i] = col;
				BUT[i] = but;
				if(col == 'O')
					ORANGE[totO++] = but;
				else
					BLUE[totB++] = but;
		}
		nxtO = 0;
		nxtB = 0;
		while(idx != steps)
		{
			if(COL[idx]=='O') //its Os turn to push a button
			{
				if(currO == ORANGE[nxtO])
				{
					idx++; //push the damn button and move on in the list
					nxtO++;
					ans++;
				}
				else if(currO < ORANGE[nxtO])
				{	
						currO++;
						ans++;
				}
				else if(currO > ORANGE[nxtO])
				{
						currO--;
						ans++;
				} 
				if(nxtB < totB) //theres something remaining for B to do
				{
					if(currB == BLUE[nxtB]); //wait here do nothing
					else if(currB < BLUE[nxtB])
						currB++;
					else if(currB > BLUE[nxtB])
						currB--;	
				}				
			}
			else
			{
				if(currB == BLUE[nxtB])
				{
					idx++; //push the damn button and move on in the list
					nxtB++;
					ans++;
				}
				else if(currB < BLUE[nxtB])
				{
						currB++;
						ans++;
				}
				else if(currB > BLUE[nxtB])
				{
						currB--;
						ans++;
				} 
				if(nxtO < totO)
				{
					if(currO == ORANGE[nxtO]); //wait here do nothing until it moves on to the next index
					else if(currO < ORANGE[nxtO])
						currO++;
					else if(currO > ORANGE[nxtO])
						currO--;	
				}
			}
		}
		printf("Case #%d: %d\n",cases++,ans);	
	}
	return 0;
}

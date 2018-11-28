#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


int px[5] = {0,-1,0,0,1};
int py[5] = {0,0,-1,1,0};

int mp[100][100];
int ans[100][100];
int dolis[100000][2];

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		int h,w;
		cin >> h >> w;
		for(i=0; i<h; i++)
		{
			for(j=0; j<w; j++)
			{
				cin >> mp[i][j];
				ans[i][j]=-1;
			}
		}
		int currans = 0;
		int curr = 0;
		for(i=0; i<h; i++)
		{
			for(j=0; j<w; j++)
			{
				if(ans[i][j]!=-1)
					continue;
				curr = 0;
				dolis[curr][0]=i;
				dolis[curr][1]=j;
				while(true)
				{
					
					int x,y;
					x=dolis[curr][0];
					y=dolis[curr][1];
					//cout << curr << " " << x << " " << y << endl;
					if(ans[x][y]>=0)
						break;
					int best = mp[x][y];
					int bestk = 0;
					for(k=1; k<5; k++)
					{
						if(x+px[k]>=0 && x+px[k]<h && y+py[k]>=0 && y+py[k]<w)
						{
							if(mp[x+px[k]][y+py[k]]<best)
							{
								best=mp[x+px[k]][y+py[k]];
								bestk=k;
							}
						}
					}
					if(bestk==0)
						break;
					curr++;
					dolis[curr][0]=x+px[bestk];
					dolis[curr][1]=y+py[bestk];
				}
				//cout << "BREAK" << endl;
				if(ans[dolis[curr][0]][dolis[curr][1]]==-1)
				{
					k=currans;
					currans++;
				}
				else
				{
					k=ans[dolis[curr][0]][dolis[curr][1]];
				}
				while(curr>=0)
				{
					ans[dolis[curr][0]][dolis[curr][1]]=k;
					curr--;
				}
				
			}
		}
		
		
		cout << "Case #" << ct << ":" << endl;
		fout << "Case #" << ct << ":" << endl;
		for(i=0; i<h; i++)
		{
			for(j=0; j<w; j++)
			{
				if(j>0)
				{
					fout << " ";
					cout << " ";
				}
				fout << ((char)(ans[i][j]+'a'));
				cout << ((char)(ans[i][j]+'a'));
			}
			cout << endl;
			fout << endl;
		}
				
		
	}

	
	return 0;
}


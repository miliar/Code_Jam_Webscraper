#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int readint()
{
  int n;
  cin >> n;
  return n;
}

string readstring()
{
  string s;
  cin >> s;
  return s;
}

string readline()
{
	char buff[1000];
	cin.getline(buff,1000);
	
	if (cin.gcount() < 2)
	{
		cin.getline(buff,1000);
	}
	
	return string(buff);
}

int main(int argc, char* argv[])
{
	int start = clock();
	
	int T = readint();
	
	for (int t=0; t<T; t++)
	{
		int H = readint();
		int W = readint();
		
		int alt[101][101];
		
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				alt[x][y] = readint();
			}
		}
		
		
		char ans[101][101];
		memset(ans, ' ', sizeof(ans));
		char flow[101][101];
		memset(flow, ' ', sizeof(flow));
		
		char label = 'a';
		
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				int lowest = alt[x][y];
				char dir='B';
				
				// North
				if (y>0 && alt[x][y-1] < lowest)
				{
					dir = 'N';
					lowest = alt[x][y-1];
				}
				
				// west
				if (x > 0 && alt[x-1][y] < lowest)
				{
					dir = 'W';
					lowest = alt[x-1][y];
				}
				
				// east
				if (x < W-1 && alt[x+1][y] < lowest)
				{
					dir = 'E';
					lowest = alt[x+1][y];
				}
				
				// south 
				if (y < H-1 && alt[x][y+1] < lowest)
				{
					dir = 'S';
					lowest = alt[x][y+1];
				}
				
				if (dir == 'B')
				{
					// if is a sink the use the next label
					flow[x][y] = 'B';
					ans[x][y] = label;
					label++;
				}
				else
				{
					// otherwise store the direction water flows from this sq
					flow[x][y] = dir;
				}
			}
		}
		
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				if (ans[x][y] == ' ')
				{
					int xx = x, yy = y;
					
					vector<pair<int, int> > trail;
					
					while (ans[xx][yy] == ' ')
					{
						trail.push_back(make_pair(xx,yy));
						
						switch(flow[xx][yy])
						{
							case 'N':
								yy--;
								break;
							case 'E':
								xx++;
								break;
							case 'S':
								yy++;
								break;
							case 'W':
								xx--;
								break;
							default:
								cout << "argggg" << endl;
						}
					}
					
					for (int i=0; i<trail.size(); i++)
					{
						ans[trail[i].first][trail[i].second] = ans[xx][yy];
					}
				}
			}
		}
		
		/*
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				cerr << flow[x][y];
				if (x != W-1)
				{
					cerr << " ";
				}	
			}
			cerr << endl;
		}*/
		
		char next = 'a';
		
		char ans2[101][101];
		memset(ans2, ' ', sizeof(ans2));
		
		char m[256];
		memset(m, 0, sizeof(m));
		
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				if (ans[x][y] == ' ')
				{
					cout << "arg2" << endl;
				}
				
				if (m[ans[x][y]] == 0)
				{
					m[ans[x][y]] = next;
					next++;
				}
				
				ans2[x][y] = m[ans[x][y]];
			}
		}
								
		cerr << "Case #" << t+1 << ":" << endl;
		
		for (int y=0; y<H; y++)
		{
			for (int x=0; x<W; x++)
			{
				cerr << ans2[x][y];
				if (x != W-1)
				{
					cerr << " ";
				}	
			}
			cerr << endl;
		}
	}
	
	cout << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}


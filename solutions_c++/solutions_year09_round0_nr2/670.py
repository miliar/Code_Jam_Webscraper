#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

int testCases;

using namespace std;

int main(void)
{
	ifstream in("B-small.in");
	ofstream out("B-output.out");
	string line;
	
	int dx[4] = {-1,0,0,1};
	int dy[4] = {0,-1,1,0};
	int nx, ny;
	
	int testCases; in >> testCases;
	
	for(int tst=0; tst<testCases; tst++)
	{
		int H, W; in >> H >> W;
		
		vector <int> bla(W,0);
		vector <vector<int> > map(H,bla);
		
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				int tem; in >> tem; map[i][j] = tem;
			}
		}
		
		string blank = ""; while(blank.size()<W) blank+=" ";
		vector<string> ret(H,blank);
		
		int basinCnt = 0;
		
		//check for basins
		
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				bool basin = true;
				for(int k=0; k<4; k++)
				{
					nx = i+dx[k]; ny = j + dy[k];
					if(nx >= 0 && nx < H && ny >= 0 && ny < W) 
					{
						if(map[nx][ny] < map[i][j]) basin = false;
					}
				}
				
				if(basin)
				{
					ret[i][j] = 'a'+basinCnt;
					basinCnt++;
					// cout << i << " " << j << " is a basin" << " " << ret[i][j] << endl;
				}
			}
		}
		
		basinCnt = 0;
		
		
		
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
			{
				if(ret[i][j] == 'a'+basinCnt)
				{
					// bfs
					queue<pair<int,int> > q;
					q.push(make_pair(i,j));
					pair<int,int> cur;
					
					while(!q.empty())
					{
						cur = q.front(); q.pop();
						int cx = cur.first; int cy = cur.second;
						char basinChar = ret[cx][cy];
						
						for(int k=0; k<4; k++)
						{
							int nx = cx+dx[k]; int ny = cy+dy[k];
							int nextX = nx; int nextY = ny;
							
							if(nx >= 0 && nx < H && ny >= 0 && ny < W)
							{
								int nnx, nny;
								
								
								for(int l=0; l<4; l++)
								{
									int nnx = nx + dx[l]; int nny = ny+dy[l];
									if(nnx >= 0 && nnx < H && nny >= 0 && nny < W)
									{
										if(map[nnx][nny] < map[nextX][nextY])
										{
											nextX = nnx; nextY = nny;
										}
									}
								}
							}
							
							if(nextX==cx && nextY==cy)
							{
								ret[nx][ny] = ret[cx][cy];
								q.push(make_pair(nx,ny));
							}
						}
					}
				
					basinCnt++;	
			
				}
			}
		}
					
	basinCnt = 0;			
	vector<string> res = ret;
					
	for(int i=0; i<H; i++)
	{
		for(int j=0; j<W; j++)
		{
			if(res[i][j]-'a'<=25&&res[i][j]-'a'>=0)
			{
				queue <pair<int,int> > q;
				q.push(make_pair(i,j));
				res[i][j] = 'A'+basinCnt;
				
				while(!q.empty())
				{
					pair<int,int> cur = q.front(); q.pop();
					int cx = cur.first; int cy = cur.second;
					
					for(int k=0; k<4; k++)
					{
						int nx = cx+dx[k]; int ny = cy+dy[k];
						if(nx>=0&&nx<H&&ny>=0&&ny<W)
						{
							if(ret[nx][ny]==ret[cx][cy]&&res[nx][ny]-'a'>=0&&res[nx][ny]-'a'<=25)
							{
							
								q.push(make_pair(nx,ny));
								res[nx][ny] = res[cx][cy];
							}
						}
					}
				}
			basinCnt++;
			}
		}
	}
	
				
			
		
	out << "Case #" << tst+1 << ":" << endl;
	for(int i=0; i<H; i++)
	{
		for(int j=0; j<ret[i].size()-1; j++)
		{
			out << (char)(res[i][j]-'A'+'a') << " ";
		}
		out << (char)(res[i][res[i].size()-1]-'A'+'a') << endl;
	}
	
	}


}
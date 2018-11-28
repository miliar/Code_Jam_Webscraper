#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>


int X,Y; 

const int MAX_ALT = 100001; 
const int UP = 1, LEFT =2, RIGHT = 3, DOWN = 4; 
const int SINK = 0; 

int getAltitude( std::vector < std::vector <int> > &map, int x, int y)
{
//	std::cout << x << ","<< y << " ?? " <<  X << " -- " <<  Y << std::endl;
	 if (x < 0 || x >= X || y < 0 || y >= Y)
	 {
//		std::cout << "OOB" << std::endl;
		return MAX_ALT;
	 }
	 else
	 {
//		std::cout << x << ","<< y << " = " << map[y][x] << std::endl; 
		return map[y][x]; 
	 }
}

int isSink( std::vector < std::vector <int> > &map, int x, int y)
{
		int myVal = map[y][x]; 
		int res = SINK; 
		int min = myVal;
		int a; 
		a = getAltitude(map, x, y + 1); if (a < myVal && a <= min) {min = a; res = DOWN; }
		a = getAltitude(map, x + 1, y); if (a < myVal && a <= min) {min = a; res = RIGHT; }
		a = getAltitude(map, x - 1, y); if (a < myVal && a <= min) {min = a; res = LEFT; }
		a = getAltitude(map, x, y - 1); if (a < myVal && a <= min) {min = a; res = UP; }

		return res; 

}
int fillSink(std::vector < std::vector <int> > &dir, std::vector < std::vector <int> > &res, int sinkID, int x, int y)
{
	res[y][x] = sinkID; 
	if (getAltitude( dir, x - 1 , y ) == RIGHT) fillSink(dir, res, sinkID, x -1, y); 
	if (getAltitude( dir, x + 1 , y ) == LEFT) fillSink(dir, res, sinkID, x +1, y); 
	if (getAltitude( dir, x  , y + 1 ) == UP) fillSink(dir, res, sinkID, x , y + 1); 
	if (getAltitude( dir, x  , y - 1) == DOWN) fillSink(dir, res, sinkID, x , y - 1); 
}
int main()
{
	int T; 
	std::cin >> T; 
	int c; 
	for (c = 1 ; c <= T; c++)
	{	
		std::cout << "Case #" << c << ":"<<std::endl; 
		std::vector < std::vector <int> > map,dir,res; 
		std::vector < std::pair<int, int> > sinks; 

		int t,t2,x,y;
		std::cin >> Y >> X; 
		map.resize(Y); 
		dir.resize(Y); 
		res.resize(Y); 
		for (t = 0; t < Y; t++)
		{
			map[t].resize(X,0); 
			dir[t].resize(X,0); 
			res[t].resize(X,-1); 
			for (t2 = 0; t2 < X; t2 ++)
			{
				std::cin >> map[t][t2]; 
			}
		}

		for(y = 0 ; y < Y; y++)
		{
			for (x = 0; x < X; x++)
			{	
				char DEBUG[5] = {'*', '^', '<', '>', '_'};  
				dir[y][x] = isSink(map, x,y);
				if (dir[y][x] == 0)
					sinks.push_back(std::make_pair(x,y)); 
//				std::cout << DEBUG[dir[y][x]] << "  "; 
			}
//			std::cout << std::endl; 
		}
		for (int sinkID = 0; sinkID < sinks.size(); sinkID++)
		{
		   fillSink(dir, res, sinkID, sinks[sinkID].first, sinks[sinkID].second); 
		}
		std::map<int, char> sinkCodes; 
		char lastSinkLetter = 'a'; 
		for (y = 0; y < Y; y++)
		{
			for (x = 0; x < X; x++)
			{
			    std::map<int, char>::iterator itr = sinkCodes.find(res[y][x]); 
			    char letter;
			    if (itr == sinkCodes.end())
			    {
				letter = sinkCodes[res[y][x]] = lastSinkLetter++; 	
			    }
			    else
			    {
				letter = itr->second; 
                            }
			    std::cout << letter;
			    if (x != (X - 1)) std::cout << " "; 
			}
			std::cout << std::endl; 
		}

	}

}

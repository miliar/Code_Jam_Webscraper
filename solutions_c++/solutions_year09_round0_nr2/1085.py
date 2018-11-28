#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int main(int argc, char ** argv)
{
	int T;
	ifstream f(argv[1]);
	f >> T ;
	for(int t=0; t<T; ++t)
	{
		int H,W;
		vector<vector<int> > map;
		vector<vector<int> > mapd;
		vector<vector<char> > mapr;

		f >> W >> H;
		map.resize(W);
		mapd.resize(W);
		mapr.resize(W);
		for(int w=0; w<W; ++w)
		{
			map[w].resize(H);
			mapd[w].resize(H);
			mapr[w].resize(H);
			for(int h=0; h<H; ++h){f >> map[w][h];mapr[w][h]='0';}
		}
	
		for(int w=0; w<W; ++w)
		{
			for(int h=0; h<H; ++h)
			{
				if((w==0 || map[w-1][h]>=map[w][h]) && 
				   (w==W-1 || map[w+1][h]>=map[w][h]) &&	
				   (h==0 || map[w][h-1]>=map[w][h]) &&	
				   (h==H-1 || map[w][h+1]>=map[w][h])) 
				{mapd[w][h]=0;}
				else
				{
					int min=map[w][h];
					if(w>0 && map[w-1][h]<min) 
					{
						min = map[w-1][h];
						mapd[w][h] = 2;
					}
					if(h>0 && map[w][h-1]<min) 
					{
						min = map[w][h-1];
						mapd[w][h] = 1;
					}
					if(h<H-1 && map[w][h+1]<min) 
					{
						min = map[w][h+1];
						mapd[w][h] = 4;
					}
					if(w<W-1 && map[w+1][h]<min) 
					{
						min = map[w+1][h];
						mapd[w][h] = 3;
					}

				}
			}
		}

		char c='a';
		for(int w=0; w<W; ++w)
		{
			for(int h=0; h<H; ++h)
			{
				if(mapr[w][h]=='0')
				{
					queue<pair<int,int> > Q;
					for(Q.push(make_pair(w,h)); !Q.empty();)
					{
						int w=Q.front().first, h=Q.front().second;
						Q.pop();
						if(mapr[w][h]=='0')
						{
							mapr[w][h]=c;
							if(h>0 && mapd[w][h-1]==4){Q.push(make_pair(w,h-1));}
							if(w>0 && mapd[w-1][h]==3) {Q.push(make_pair(w-1,h));}
							if(h<H-1 && mapd[w][h+1]==1) {Q.push(make_pair(w,h+1));}
  							if(w<W-1 && mapd[w+1][h]==2) {Q.push(make_pair(w+1,h));}
							if(mapd[w][h]==1) {Q.push(make_pair(w,h-1));}
							if(mapd[w][h]==2) {Q.push(make_pair(w-1,h));}
							if(mapd[w][h]==3) {Q.push(make_pair(w+1,h));}
							if(mapd[w][h]==4) {Q.push(make_pair(w,h+1));}
						}
					}
					++c;
				}
			}
		}

		cout << "Case #" << t+1 << ":" << endl;
		for(int w=0; w<W; ++w)
		{
			for(int h=0; h<H; ++h)
			{
				cout << mapr[w][h] << " ";
			}
			cout << endl;
		}



	}


	return 0;
}

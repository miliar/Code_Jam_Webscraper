#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <utility>

using namespace std;
// put the map outside;
int T;
int H, W;
int map[102][102];
int res[102][102];

void findpath( pair<int, int> st, int* label )
{
	pair<int, int> sink = st;
	vector<pair<int, int> > path;
	path.push_back( sink );
	bool flag;
	while(1)
	{
		flag = false;
		pair<int, int> min = sink;
		if( (sink.first - 1 >= 0) && 
			( map[sink.first - 1][sink.second] < map[min.first ][min.second]) ) //north
		{
			flag = true;
			min.first = sink.first - 1;
			min.second = sink.second ;
		}
		if( (sink.second -1 >= 0) &&
			( map[sink.first][sink.second - 1] < map[min.first][min.second]) )
		{
			flag = true;
			min.first = sink.first;
			min.second = sink.second - 1;
		}
		if( (sink.second + 1 < W ) &&
			( map[sink.first][sink.second + 1] < map[min.first][min.second]) )
		{
			flag = true;
			min.first = sink.first;
			min.second = sink.second + 1;
		}
		if( (sink.first + 1 < H ) &&
			( map[sink.first + 1][sink.second] < map[min.first][min.second]) )
		{
			flag = true;
			min.first = sink.first + 1;
			min.second = sink.second;
		}


		if( flag )
		{
			if( res[min.first][min.second] == -1)
			{
				path.push_back(make_pair(min.first, min.second));
		//		res[min.first][min.second] = label;
				sink = min;
			}
			else
			{
				int tmp = res[min.first][min.second];
				int len = path.size();
				for( int i = 0; i < len; i++)
				{
					res[path[i].first][path[i].second] = tmp;
				}
				return;		
			}
	//		sink = min;
		}
		else
			break;
	}
	int len1 = path.size();
	for( int j = 0; j < len1; j++ )
	{
		res[path[j].first][path[j].second] = *label;
	}
	(*label)++;
	
	return;
}
int main()
{
	int i, h, w;

	FILE* fin = fopen("B-large.in", "r");
//	FILE* fin = fopen("2f1.txt", "r");
	FILE* fout = fopen("tryL2.txt", "w");

	fscanf(fin, "%d", &T);

	for( i = 0; i < T; i++)
	{
		fscanf(fin, "%d %d",&H, &W);
		for( h = 0 ; h < H; h++ )
			for( w = 0; w < W; w++ )
			{
				fscanf(fin, "%d ", &map[h][w]);
				res[h][w] = -1;
			}

		int* label = new int;
		*label = 0;

//		pair<int, int> s0 = findsink( make_pair( 0, 0) );
		for( h = 0; h < H; h++ )
		{
			for( w = 0; w < W; w++)
			{
				if( res[h][w] == -1)
				{
					findpath( make_pair( h, w), label);
							
				}
		/*		pair<int, int> tmpr;
				if( findsink( make_pair( h, w )) == s0 ) 
				{
					res[h][w] = 0;
				}
				else
					res[h][w] = 1; */
			}
		}
		fprintf(fout, "Case #");
		fprintf(fout,"%d:\n", i+1 );
		for( h = 0 ; h < H; h++ )
		{
			for( w = 0; w < W; w++ )
			{
		//		out<<(char)(res[h][w] + 'a')<<" ";
				fprintf(fout, "%c ", (char)(res[h][w] + 'a') );
			}
		//	out<<endl;
			fprintf(fout, "\n");
		}
	}
}
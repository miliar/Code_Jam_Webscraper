// CodeJam.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//

#include <tchar.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
using namespace std;


typedef vector<int> Line;

int dirx[4] = { -1 ,  0 , 0 , 1 };
int diry[4] = { 0 , -1 , 1 ,  0 };

void f( int H , int W , ifstream& ifs , ofstream& ofs )
{
	vector<Line> mat( H );

	vector<Line> dst(H);
	vector<Line> mindir(H);

	for( int i = 0 ; i < H ; ++i )
	{
		dst[i].resize(W,0);

		mat[i].resize(W);
		mindir[i].resize(W);

		for( int j = 0 ; j < W ; ++j )
		{
			Line& l = mat[i];
			ifs >> l[j];
		}
	}

	dst[0][0] = 1;

	int sink_idx = 2;

	for( int i = 0 ; i < H ; ++i )
	{
		for( int j = 0 ; j < W ; ++j )
		{
			int min_flow = 0;
			mindir[i][j] = -1;
			for( int k = 0 ; k < 4 ; ++k )
			{
				int ni = i + dirx[k];
				int nj = j + diry[k];
				if( ni == -1 ) continue;
				if( nj == -1 ) continue;
				if( ni == H ) continue;
				if( nj == W ) continue;

				int a = mat[i][j];
				int na = mat[ni][nj];
				int df = na - a;
				if( df >= 0 ) continue;
				if( min_flow > df )
				{
					min_flow = df;
					mindir[i][j] = k;
				}
			}
		}
	}

	int laf = 2;

	for(;;)
	{
		bool bUpd = false;
		for( int i = 0 ; i < H ; ++i )
		{
			for( int j = 0 ; j < W ; ++j )
			{
				int d = mindir[i][j];
				if ( d == -1 ) continue;

				int ni = i + dirx[d];
				int nj = j + diry[d];

				if( ni == -1 ) continue;
				if( nj == -1 ) continue;
				if( ni == H ) continue;
				if( nj == W ) continue;

				if( dst[i][j] != dst[ni][nj] )
				{
					if( dst[i][j] != 0 )
						dst[ni][nj] = dst[i][j];
					else
						dst[i][j] = dst[ni][nj];
					bUpd = true;
				}
			}
		}
		if( !bUpd )
		{
			for( int i = 0 ; i < H ; ++i )
			{
				for( int j = 0 ; j < W ; ++j )
				{
					if( dst[i][j] != 0 ) continue;

					dst[i][j] = laf++;
					bUpd = true;
					break;
				}
			if( bUpd )break;
			}
		}
		if( !bUpd )break;
	}

	for( int i = 0 ; i < H ; ++i )
	{
		for( int j = 0 ; j < W ; ++j )
		{
			int o = (int)'a' + dst[i][j] -1;
			char c = (char)o;

			//int ii = mindir[i][j];
			if( j == 0 )
			{
				ofs << c;
				//cout << ii;
			}
			else
			{
				ofs << " " << c;
				//cout << " " << ii;
			}
		}
		ofs << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs("C:\\ws\\Codejam\\B-large.in");
	ofstream ofs("C:\\ws\\Codejam\\OUT.out");

	int T;
	ifs >> T;

	for( size_t i = 0 ; i < T ; ++i )
	{
		int h , w;
		ifs >> h >> w;
		ofs << "Case #" << (i+1) << ":" << endl;
		//cout << "Case #" << (i+1) << ":" << endl;
		f( h , w , ifs , ofs );
	}

	return 0;
}


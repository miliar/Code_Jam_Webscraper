#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <string>
#include <map>


//#define DEBUG
#define MAX_VALUE 99999

using namespace std;




typedef enum { NORTH, WEST, EAST, SOUTH, SINK, NUM_DIR} direction;

class coor
{
public:
	int h;
	int w;
};


int altMap[100][100];
direction dirMap[100][100];
int sinkMap[100][100];

set<pair<int,int>> sinks;

void printSinks()
{
	for(set<pair<int,int>>::iterator iter = sinks.begin(); iter != sinks.end(); ++iter){
		pair<int,int>& p = *iter;
		printf( "%d %d\n", p.first, p.second );
	}
}

void fillDirection( int H, int W )
{
	for( int iH = 0; iH < H; iH++){
		for( int iW = 0; iW < W; iW++){
			dirMap[iH][iW] = NUM_DIR;
			int min = altMap[iH][iW];
			direction dir = NUM_DIR;

			
			if( iH > 0 && min > altMap[iH-1][iW] ){
				dir = NORTH;
				min = altMap[iH-1][iW];
			}
			if( iW > 0 && min > altMap[iH][iW-1] ){
				dir = WEST;
				min = altMap[iH][iW-1];
			}
			if( iW < W - 1 && min > altMap[iH][iW+1] ){
				dir = EAST;
				min = altMap[iH][iW+1];
			}
			if( iH < H - 1 && min > altMap[iH+1][iW] ){
				dir = SOUTH;
				min = altMap[iH+1][iW];
			}


			if( dir == NUM_DIR ){
				//North
				if( iH > 0 && min == altMap[iH-1][iW] ){
					dir = NORTH;
					min = altMap[iH-1][iW];
				}else if( iW > 0 && min == altMap[iH][iW-1] ){
					dir = WEST;
					min = altMap[iH][iW-1];
				}else if( iW < W && min == altMap[iH][iW+1] ){
					dir = EAST;
					min = altMap[iH][iW+1];
				}else if( iH < H && min == altMap[iH+1][iW] ){
					dir = SOUTH;
					min = altMap[iH+1][iW];
				}else{
					dir = SINK;
				}

				if( min == altMap[iH][iW]){
					dir = SINK;
				}
			}
			
			dirMap[iH][iW] = dir;
			if( dir == SINK){
				pair<int,int> p(iH, iW);
				sinks.insert( p );
			}
		}
	}
}

void printMap(int m[100][100], int H, int W)
{
	for( int iH = 0; iH < H; iH++){
		for( int iW = 0; iW < W; iW++){
			printf("%d ", m[iH][iW] );
		}
		printf("\n");
	}
}


void printDirMap( int H, int W)
{
	for( int iH = 0; iH < H; iH++){
		for( int iW = 0; iW < W; iW++){
			char ch = ' ';
			switch( dirMap[iH][iW]){
				case NORTH:
					ch = 'N';
					break;
				case WEST:
					ch = 'W';
					break;
				case EAST:
					ch = 'E';
					break;
				case SOUTH:
					ch = 'S';
					break;
				case SINK:
					ch = 'X';
					break;
				default:
					ch = '_';
					break;
			}
				
			printf("%c ", ch);
		}
		printf("\n");
	}
}

direction diffDir( direction dir )
{
	direction ret;
	switch( dir ){
		case NORTH:
			ret = SOUTH;
			break;
		case SOUTH:
			ret = NORTH;
			break;
		case EAST:
			ret = WEST;
			break;
		case WEST:
			ret = EAST;
			break;
		default:
			ret = NORTH;
			break;
	}

	return ret;
}

void follow( int H, int W, int iH, int iW, int idxSink, direction dir )
{
	if( iH < 0 || H <= iH || iW < 0 || W <= iW ){
		return;
	}

	if( sinkMap[iH][iW] > -1 ){
		return;
	}
#ifdef DEBUG
	printf( "F: %d %d\n", iH, iW );
#endif //DEBUG

	if( diffDir( dirMap[iH][iW] ) == dir ){
		sinkMap[iH][iW] = idxSink;

#ifdef DEBUG
		printf( "M: h:%d w:%d d:%d %d %d %d \n", iH, iW, idxSink, dir, dirMap[iH][iW], diffDir( dirMap[iH][iW] ) );
#endif //DEBUG

		if( dir != NORTH )
			follow( H, W, iH+1, iW, idxSink, SOUTH);
		if( dir != WEST )
			follow( H, W, iH, iW+1, idxSink, EAST);
		if( dir != EAST )
			follow( H, W, iH, iW-1, idxSink, WEST);
		if( dir != SOUTH )
			follow( H, W, iH-1, iW, idxSink, NORTH);
	}


}

void followSink( int H, int W ){


	for( int iH = 0; iH < H; iH++){
		for( int iW = 0; iW < W; iW++){
			sinkMap[iH][iW] = -1;
		}
	}

	int idxSink = 0;
	for(set<pair<int,int>>::iterator iter = sinks.begin(); iter != sinks.end(); ++iter, idxSink++){
		pair<int,int>& p = *iter;
#ifdef DEBUG
		printf( "S: %d %d\n", p.first, p.second );
#endif //DEBUG

		sinkMap[p.first][p.second] = idxSink;
		follow( H, W, p.first+1, p.second, idxSink, SOUTH);
		follow( H, W, p.first, p.second+1, idxSink, EAST);
		follow( H, W, p.first, p.second-1, idxSink, WEST);
		follow( H, W, p.first-1, p.second, idxSink, NORTH);
	}
}

void printSinkMap( int H, int W ){

	map<int,char> chMap;
	map<int,char>::iterator it;


	char lastCh = 'a';
	for( int iH = 0; iH < H; iH++){
		for( int iW = 0; iW < W; iW++){
			int idx = sinkMap[iH][iW];
			char ch;
			
			it = chMap.find( idx );
			if( it == chMap.end() ){
				ch = lastCh;
				chMap[idx] = lastCh;
				lastCh++;
			}else{
				ch=it->second;
			}

			printf("%c ", ch );
		}
		printf("\n");
	}
}

int main(int argc, char** argv)
{
	//reopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	//freopen("B-small-attempt0.in", "r", stdin );
	//freopen("B-small-attempt0.out", "w", stdout );
	//freopen("A-large-practice.in", "r", stdin );
	//freopen("A-large-practice.out", "w", stdout );


	int T, H, W;
	

	cin >> T;
	for( int iT = 0; iT < T; iT++){
		cin >> H >> W;
		for( int iH = 0; iH < H; iH++){
			for( int iW = 0; iW < W; iW++){
				int tmp;
				cin >> tmp;
				altMap[iH][iW] = tmp;
			}
		}

		sinks.clear();
		fillDirection( H, W );

#ifdef DEBUG
		printMap(altMap, H,W);
		printDirMap(H,W);
		printSinks();
#endif//DEBUG

		followSink( H, W );

		printf("Case #%d:\n", iT +1 );

		printSinkMap( H, W );
	}

	return 0;
}
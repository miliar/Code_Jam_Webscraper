#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <deque>

using namespace std;

typedef struct{
	int altitude;
	char area;
	bool setted;
} cell;

typedef struct {
	int x;
	int y;
} POS;

vector<vector<cell>> map;
int W,H;

bool lowest_neighbor(POS& pos){
	int x = pos.x;
	int y = pos.y;
	int altitude = map[y][x].altitude;
	int lowest_x = x;
	int lowest_y = y;
	int lowest_altitude = altitude;
	bool bMove = false;

	// 4点チェック
	if( y - 1 >= 0 ){
		if( map[y-1][x].altitude < lowest_altitude ){
			lowest_altitude = map[y-1][x].altitude;
			lowest_x = x;
			lowest_y = y-1;
			bMove = true;
		}
	}
	if( x - 1 >= 0 ){
		if( map[y][x-1].altitude < lowest_altitude ){
			lowest_altitude = map[y][x-1].altitude;
			lowest_x = x-1;
			lowest_y = y;
			bMove = true;
		}
	}
	if( x + 1 < W ){
		if( map[y][x+1].altitude < lowest_altitude ){
			lowest_altitude = map[y][x+1].altitude;
			lowest_x = x+1;
			lowest_y = y;
			bMove = true;
		}
	}
	if( y + 1 < H ){
		if( map[y+1][x].altitude < lowest_altitude ){
			lowest_altitude = map[y+1][x].altitude;
			lowest_x = x;
			lowest_y = y+1;
			bMove = true;
		}
	}
	pos.x = lowest_x;
	pos.y = lowest_y;
	return bMove;
}


void main(int argc, char*argv[])
{
	if( argc < 3 ){
		printf("usage: solv.exe in out\n");
		return;
	}

	FILE* fin = fopen(argv[1],"r");
	FILE* fout = fopen(argv[2],"w");
	if( fin == NULL ){
		printf("cannot open in-file : %s\n", argv[1]);
		return;
	}
	if( fin == NULL ){
		printf("cannot open out-file : %s\n", argv[2]);
		return;
	}
	/////////////////////////////
	char line[1024];
	int CASE;
	int x,y;

	fgets(line,1024,fin);
	CASE = atoi(line);
	map.resize(10000);
	for( int i = 0; i < 10000; i++ ){
		map[i].resize(10000);
	}
	//for( int i = 0; i < 20; i++ ){
	//	map[i].resize(20);
	//}

	for( int cs = 0; cs < CASE; cs++ ){
		fgets(line,1024,fin);
		sscanf(line, "%d %d", &H,&W);
		for( y = 0; y < H; y++ ){
			fgets(line,1024,fin);
			char* p = line;
			int end = strlen(line);
			line[end] = ' ';
			line[end+1] = '\0';
			for( x = 0; x < W; x++ ){
				char* start = p;
				while(*p != ' ')
					p++;
				*p = '\0';
				map[y][x].altitude = atoi(start);
				map[y][x].setted = false;
				p++;
			}
		}
		//////////////////
		int count = 0;
		char current_area = 'a';
		bool bFirst = true;
		x = 0;
		y = 0;

		deque<POS> bfs;
		bfs.clear();
		POS pos;
		while( 1 ){
			if( bFirst == false ){
				for( y = 0; y < H; y++ ){
					for( x = 0; x < W; x++ ){
						if( map[y][x].setted == false ){
							goto out;
						}
					}
				}
out:
				if( y == H && x == W ){
					break;
				}
			}else{
				bFirst = false;
			}
			/////// not labeled
			map[y][x].area = current_area;
			map[y][x].setted = true;
			pos.y = y;
			pos.x = x;
			bfs.push_back(pos);

			while(1){
				if( bfs.empty() ){
					break;
				}
				pos = bfs.front();
				x = pos.x;
				y = pos.y;
				bfs.pop_front();

				// 高い方チェック
				if( y - 1 >= 0 ){
					if( map[y-1][x].altitude > map[y][x].altitude ){
						if( map[y-1][x].setted == false ){
							pos.x = x;
							pos.y = y-1;
							lowest_neighbor(pos);
							if( pos.x == x && pos.y == y ){
								map[y-1][x].area = current_area;
								map[y-1][x].setted = true;
								pos.x = x;
								pos.y = y-1;
								bfs.push_back(pos);
							}
						}
					}
				}
				if( x - 1 >= 0 ){
					if( map[y][x-1].altitude > map[y][x].altitude ){
						if( map[y][x-1].setted == false ){
							pos.x = x-1;
							pos.y = y;
							lowest_neighbor(pos);
							if( pos.x == x && pos.y == y ){
								map[y][x-1].area = current_area;
								map[y][x-1].setted = true;
								pos.x = x-1;
								pos.y = y;
								bfs.push_back(pos);
							}
						}
					}
				}
				if( x + 1 < W ){
					if( map[y][x+1].altitude > map[y][x].altitude ){
						if(map[y][x+1].setted == false){
							pos.x = x+1;
							pos.y = y;
							lowest_neighbor(pos);
							if( pos.x == x && pos.y == y ){
								map[y][x+1].area = current_area;
								map[y][x+1].setted = true;
								pos.x = x+1;
								pos.y = y;
								bfs.push_back(pos);
							}
						}
					}
				}
				if( y + 1 < H ){
					if( map[y+1][x].altitude > map[y][x].altitude ){
						if( map[y+1][x].setted == false ){
							pos.x = x;
							pos.y = y+1;
							lowest_neighbor(pos);
							if( pos.x == x && pos.y == y ){
								map[y+1][x].area = current_area;
								map[y+1][x].setted = true;
								pos.x = x;
								pos.y = y+1;
								bfs.push_back(pos);
							}
						}
					}
				}
				// 低い方チェック
				pos.x = x;
				pos.y = y;
				if( lowest_neighbor(pos) ){
					if( map[pos.y][pos.x].setted == false ){
						map[pos.y][pos.x].area = current_area;
						map[pos.y][pos.x].setted = true;
						bfs.push_back(pos);
					}
				}
			}
			current_area++;
		}
		////
		fprintf( fout,"Case #%d:\n", cs+1 );
		for( y = 0; y < H; y++ ){
			for( x = 0; x < W; x++ ){
				if( x == W-1 ){
					fprintf( fout, "%c\n", map[y][x].area );
				}else{
					fprintf( fout, "%c ", map[y][x].area );
				}
			}
		}
		}
		
}







#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fou("p2large.txt");


const int maxh = 101;
const int maxlat = 99999;
int H, W;
int map[maxh+1][maxh+1];
const int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

char ans[maxh+1][maxh+1];
char color;

void readdata()
{
	fin >> H >> W;
    int lat;
	for (int h=0; h<=maxh; h++)
    for (int w=0; w<=maxh; w++){
        map[h][w]= maxlat;
    }

    for (int h=1; h<=H; h++)
    for (int w=1; w<=W; w++){
    	fin >> lat;
        map[h][w]=lat;
    }
}


char floodfill( int h , int w )
{
	if (ans[h][w]!=0) return ans[h][w];

	//find lowest
    int lowlat = maxlat;
    int lowdir;
    for (int i=0; i<=3; i++){
        if (map[h+dir[i][0]][w+dir[i][1]]<lowlat ){
            lowlat = map[h+dir[i][0]][w+dir[i][1]];
            lowdir = i;
        }
    }

    if (lowlat < map[h][w]){
        char tmpc = floodfill( h+dir[lowdir][0] , w+dir[lowdir][1] );
 		ans[h][w] = tmpc;
    }
    else{
        ans[h][w]=color;
        color = color+1;
    }

    return ans[h][w];
}


void work()
{
    memset( ans , 0 , sizeof(ans) );
    color = 'a';
	for (int h=1; h<=H; h++)
    for (int w=1; w<=W; w++){
    	floodfill( h , w );
    }

    for (int h=1; h<=H; h++){
        for (int w=1; w<=W; w++){
            fou << ans[h][w] << " ";
        }
        fou << endl;
    }
}



int main()
{
	int T;
	fin >> T;
    for (int i=1; i<=T; i++){
        readdata();
        fou << "Case #" << i << ":" << endl;
        work();
    }
	system("pause");
    return 0;
}

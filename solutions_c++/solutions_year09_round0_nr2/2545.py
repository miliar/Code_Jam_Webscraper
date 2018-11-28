#include <fstream>
#include <vector>
using namespace std;

ofstream out("a.out");
ifstream in("a.in");

int grid[100][100] = {0};
char cgrid[100][100] = {0};

int main(){
	int N;
	in >> N;
	for (int n = 0; n < N; n++){
		int X, Y, letter=0;
		in >> Y >> X;
		memset(grid, 0, 40000);
		memset(cgrid, 0, 10000);
		for (int r = 0; r < Y; r++) for (int p = 0; p < X; p++) in >> grid[r][p];
		for (int x = 0; x < X; x++){
			for (int y = 0; y < Y; y++){
				bool up=true, down=true, left=true, right=true;
				int now = grid[y][x];
				if (x != 0) if (grid[y][x-1] < now) left = false;
				if (y != 0) if (grid[y-1][x] < now) up = false;
				if (x != X-1) if (grid[y][x+1] < now) right = false;
				if (y != Y-1) if (grid[y+1][x] < now) down = false;
				if (up && down && left && right) cgrid[y][x] = 'a'+letter, letter++;
			}
		}
		for (int y = 0; y < Y; y++){
			for (int x = 0; x < X; x++){
				vector<pair<int,int>> fp;
				fp.clear();
				int currx=x, curry=y;
				while (cgrid[curry][currx] == 0) {
					int alt = grid[curry][currx];
					int dir = 0;
					fp.push_back(pair<int,int>(curry, currx));
					if (curry != 0) if (grid[curry-1][currx] < alt) alt = grid[curry-1][currx], dir=1;
					if (currx != 0) if (grid[curry][currx-1] < alt) alt = grid[curry][currx-1], dir=2;
					if (currx != X-1) if (grid[curry][currx+1] < alt) alt = grid[curry][currx+1], dir=3;
					if (curry != Y-1) if (grid[curry+1][currx] < alt) alt = grid[curry+1][currx], dir=4;
					if (dir == 1) curry--;
					if (dir == 2) currx--;
					if (dir == 3) currx++;
					if (dir == 4) curry++;
				}
				for (int r = 0; r < fp.size(); r++) cgrid[fp[r].first][fp[r].second] = cgrid[curry][currx];
			}
		}
		bool b[26] = {false};
		int i[26] = {0};
		int c = 0;
		for (int y = 0; y < Y; y++){
			for (int x = 0; x < X; x++){
				if (!b[cgrid[y][x]-'a']){
					b[cgrid[y][x]-'a'] = true;
					c++;
					i[cgrid[y][x]-'a'] = cgrid[y][x]-'a' - (c-1);
					if (c==26) goto finish;
				}
			}
		}
finish:
		for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) cgrid[y][x] -= i[cgrid[y][x]-'a'];
		out << "Case #" << n+1 << ':' << endl;
		for (int y = 0; y < Y; y++){
			for (int x = 0; x < X; x++){
				out << cgrid[y][x];
				if (x != X-1) out << ' ';
			}
			out << endl;
		}
	}
}
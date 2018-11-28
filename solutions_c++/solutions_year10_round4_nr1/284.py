#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

char B[500][500];

bool is_elegant(int x, int y, int k)
{
	//printf("is_elegant(%d, %d, %d) - [%c]\n", x, y, k, B[x][y]);
	for (int xx = x - k; xx <= x; ++xx) {
		for (int yy = y - k; yy <= y; ++yy) {
			//if (x == 250 && y == 251) printf("compare %d,%d[%c][%c][%c]\n", xx - 250, yy - 250, B[xx][yy], B[x + x - xx][yy], B[xx][y + y - yy]);
			if (B[xx][yy] == ' ') continue;
			if (B[xx][yy] != B[x + x - xx][yy] && B[x + x - xx][yy] != ' ') return false;
			if (B[xx][yy] != B[xx][y + y - yy] && B[xx][y + y - yy] != ' ') return false;
		}
	}
	for (int xx = x; xx <= x + k; ++xx) {
		for (int yy = y; yy <= y + k; ++yy) {
			//if (x == 250 && y == 251) printf("compare %d,%d[%c][%c][%c]\n", xx - 250, yy - 250, B[xx][yy], B[x + x - xx][yy], B[xx][y + y - yy]);
			if (B[xx][yy] == ' ') continue;
			if (B[xx][yy] != B[x + x - xx][yy] && B[x + x - xx][yy] != ' ') return false;
			if (B[xx][yy] != B[xx][y + y - yy] && B[xx][y + y - yy] != ' ') return false;
		}
	}
	
	return true;
}

int solve()
{
	int k;
	int ret;
	char line[1024];
	
	cin >> k;
	memset(B, ' ', sizeof(B) );
	string x;
	cin.getline(line, 1024);
	
	for (int i = 0; i < 2 * k - 1; ++i) {
		cin.getline(line, 1024);
		x = line;
		//printf("[%s]\n", x.c_str() );
		for (int j = 0; j < x.size(); ++j) {
			B[251 - k + i][251 - k + j] = x[j];
		}
	}
	
	if (is_elegant(250, 250, k) ) return 0;
	for (int i = 1; i <= 2 *k + 2; ++i) {
		for (int j = 0; j < i; ++j) {
			if (is_elegant(250 - j, 250 + (i - j), k + i) ) {
				ret = (k + i) * (k + i) - k * k;
				return ret;
			}
			if (is_elegant(250 - (i - j), 250 - j, k + i) ) {
				ret = (k + i) * (k + i) - k * k;
				return ret;
			}
			if (is_elegant(250 + j, 250 - (i - j), k + i) ) {
				ret = (k + i) * (k + i) - k * k;
				return ret;
			}
			if (is_elegant(250 + (i -j), 250 + j, k + i) ) {
				ret = (k + i) * (k + i) - k * k;
				return ret;
			}
		}
	}
	
	fprintf(stderr, "ERROR>>>\n");
	return -1;
}

int main(int argc, char *argv[])
{
    int T;
    
    cin >> T;
    
    for (int i = 1; i <= T; ++i) {
		printf("Case #%d: %d\n", i, solve() );
	}
	
    return EXIT_SUCCESS;
}

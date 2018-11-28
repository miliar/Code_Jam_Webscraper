#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <time.h>
using namespace std;

int main()
{
	int n;
	cin >> n;
	
	for (int c = 1; c <= n; ++c) {
		vector<string> b(4);
		for (int j = 0; j < 4; ++j) {
			cin >> b[j];
		}
		
		bool wx = false, wo = false, over = true;
		
		for (int i = 0; i < 4; ++i) {
			int cx = 0, ct = 0, co = 0;
			for (int j = 0; j < 4; ++j) {
				if (b[i][j] == 'X') ++cx;
				else if (b[i][j] == 'T') ++ct;
				else if (b[i][j] == 'O') ++co;
				else if (b[i][j] == '.') over = false;
			}
			
			if (cx == 4 || cx == 3 && ct == 1) wx = true;
			if (co == 4 || co == 3 && ct == 1) wo = true;
			
			cx = 0, ct = 0, co = 0;
			for (int j = 0; j < 4; ++j) {
				if (b[j][i] == 'X') ++cx;
				else if (b[j][i] == 'T') ++ct;
				else if (b[j][i] == 'O') ++co;
			}
			if (cx == 4 || cx == 3 && ct == 1) wx = true;
			if (co == 4 || co == 3 && ct == 1) wo = true;
			
		}
			int cx = 0, ct = 0, co = 0;
			for (int j = 0; j < 4; ++j) {
				if (b[j][j] == 'X') ++cx;
				else if (b[j][j] == 'T') ++ct;
				else if (b[j][j] == 'O') ++co;
			}
			if (cx == 4 || cx == 3 && ct == 1) wx = true;
			if (co == 4 || co == 3 && ct == 1) wo = true;
			
			cx = 0, ct = 0, co = 0;
			for (int j = 0; j < 4; ++j) {
				if (b[j][3 - j] == 'X') ++cx;
				else if (b[j][3 - j] == 'T') ++ct;
				else if (b[j][3 - j] == 'O') ++co;
			}
			if (cx == 4 || cx == 3 && ct == 1) wx = true;
			if (co == 4 || co == 3 && ct == 1) wo = true;
		
		if (wx) printf("Case #%d: X won\n", c);
		else if (wo) printf("Case #%d: O won\n", c);
		else if (over) printf("Case #%d: Draw\n", c);
		else printf("Case #%d: Game has not completed\n", c);
	}
	
	return 0;
}

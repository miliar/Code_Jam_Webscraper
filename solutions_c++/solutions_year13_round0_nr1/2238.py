#include <cstdio>

int main() {
	char input[4][6];
	int T;
	
	scanf("%d", &T);
	for(int testCase = 1; testCase <= T; ++testCase) {
		scanf("%s", input[0]);
		scanf("%s", input[1]);
		scanf("%s", input[2]);
		scanf("%s", input[3]);
		
		bool wonO, wonX, draw;
		for(int x = 0; x < 4; ++x) {
			// Each row check
			
			wonO = true;
			wonX = true;
			for(int y = 0; y < 4; ++y) {
				if(input[x][y] != 'O' && input[x][y] != 'T') {
					wonO = false;
				}
				if(input[x][y] != 'X' && input[x][y] != 'T') {
					wonX = false;
				}
			}
			
			if(wonO) {
				printf("Case #%d: O won\n", testCase);
				break;
			}
			if(wonX) {
				printf("Case #%d: X won\n", testCase);
				break;
			}
			
			// Each column check
			
			wonO = true;
			wonX = true;
			for(int y = 0; y < 4; ++y) {
				if(input[y][x] != 'O' && input[y][x] != 'T') {
					wonO = false;
				}
				if(input[y][x] != 'X' && input[y][x] != 'T') {
					wonX = false;
				}
			}
			
			if(wonO) {
				printf("Case #%d: O won\n", testCase);
				break;
			}
			if(wonX) {
				printf("Case #%d: X won\n", testCase);
				break;
			}
		}
		
		if(wonO || wonX)
			continue;
		
		// Daiagonal check
		wonO = true;
		wonX = true;
		for(int y = 0; y < 4; ++y) {
			if(input[y][y] != 'O' && input[y][y] != 'T') {
				wonO = false;
			}
			if(input[y][y] != 'X' && input[y][y] != 'T') {
				wonX = false;
			}
		}
		
		if(wonO) {
			printf("Case #%d: O won\n", testCase);
			continue;
		}
		if(wonX) {
			printf("Case #%d: X won\n", testCase);
			continue;
		}
		
		wonO = true;
		wonX = true;
		for(int y = 0; y < 4; ++y) {
			if(input[y][3-y] != 'O' && input[y][3-y] != 'T') {
				wonO = false;
			}
			if(input[y][3-y] != 'X' && input[y][3-y] != 'T') {
				wonX = false;
			}
		}
		
		if(wonO) {
			printf("Case #%d: O won\n", testCase);
			continue;
		}
		if(wonX) {
			printf("Case #%d: X won\n", testCase);
			continue;
		}
		
		// Noone won
		
		for(int x = 0; x < 4; ++x) {
			draw = true;
			for(int y = 0; y < 4; ++y) {
				if(input[x][y] == '.') {
					draw = false;
					break;
				}
			}
			if(!draw) 
				break;
		}
		
		if(draw) {
			printf("Case #%d: Draw\n", testCase);
			continue;
		}
		
		printf("Case #%d: Game has not completed\n", testCase);
	}
}

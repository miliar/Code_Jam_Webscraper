#include <cstdio>
#include <algorithm>
#include <vector>

int main(){
	int T = 0;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int w = 0, h = 0;
		scanf("%d %d", &h, &w);
		std::vector<std::vector<int> > input(h + 2, std::vector<int>(w + 2, 10000));
		std::vector<std::vector<char> > output(h, std::vector<char>(w));
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				int x;
				scanf("%d", &x);
				input[i + 1][j + 1] = x;
			}
		}
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				int round[5] = {
					input[i + 1][j + 1],
					input[i    ][j + 1],
					input[i + 1][j    ],
					input[i + 1][j + 2],
					input[i + 2][j + 1]
				};
				output[i][j] = std::min_element(round, round + 5) - round;
			}
		}
		char c = 'a';
		printf("Case #%d:\n", t);
		for(int i = 0; i < h; i++){
			for(int j = 0; j < w; j++){
				int y = i, x = j;
				while(x >= 0){
					switch(output[y][x]){
					case 1:	y--;	break;
					case 2:	x--;	break;
					case 3:	x++;	break;
					case 4:	y++;	break;
					case 0:	output[y][x] = c++;
					default:
						printf("%c", output[y][x]);
						x = -1;
					}
				}
				printf(j == w - 1 ? "\n" : " ");
			}
		}
	}
	return 0;
}

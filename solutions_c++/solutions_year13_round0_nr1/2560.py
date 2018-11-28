#include <iostream>

int T;
char map[4][4];

int roff[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int coff[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

bool valid(int i, int j){
	return (0 <= i && i < 4 && 0 <= j && j < 4);
}

int main(){
	std::cin >> T;
	for(int p=0; p<T; ++p){
		int total = 0;
		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				std::cin >> map[i][j];
				if(map[i][j] == '.') ++total;
			}
		}
		bool brk = false;
		for(int i=0; i<4; ++i){
			char cur = map[0][i];
			if(cur == '.') continue;
			for(int j=0; j<8; ++j){
				int di = roff[j];
				int dj = coff[j];
				int pi = di;
				int pj = i+dj;
				int k;
				//std::cout << di << " " << dj << std::endl;
				for(k=0; k<3; ++k){
					if(!valid(pi, pj) || (map[pi][pj] != cur && map[pi][pj] != 'T')) break;
					pi+=di;
					pj+=dj;
				}
				if(k == 3) {
					//std::cout << 0 << " " << i << std::endl;
					if(cur == 'X') std::cout << "Case #" << (p+1) << ": " << "X won" << std::endl;
					else std::cout << "Case #" << (p+1) << ": " << "O won" << std::endl;
					brk = true;
					break;
				}
			}
			if(brk) break;
		}
		if(brk) continue;
		for(int i=0; i<4; ++i){
			char cur = map[i][0];
			if(cur == '.') continue;
			for(int j=0; j<8; ++j){
				int di = roff[j];
				int dj = coff[j];
				int pi = i+di;
				int pj = dj;
				int k;
				for(k=0; k<3; ++k){
					if(!valid(pi, pj) || (map[pi][pj] != cur && map[pi][pj] != 'T')) break;
					pi+=di;
					pj+=dj;
				}
				if(k == 3) {
					if(cur == 'X') std::cout << "Case #" << (p+1) << ": " << "X won" << std::endl;
					else std::cout << "Case #" << (p+1) << ": " << "O won" << std::endl;
					brk = true;
					break;
				}
			}
			if(brk) break;
		}
		if(brk) continue;
		if(total == 0) std::cout << "Case #" << (p+1) << ": " << "Draw" << std::endl;
		else std::cout << "Case #" << (p+1) << ": " << "Game has not completed" << std::endl;
	}
}
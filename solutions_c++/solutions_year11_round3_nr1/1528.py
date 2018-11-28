#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	std::fstream fin(argv[1]);
	if (!fin.is_open()) return 1;

	char pic[64][64];

	int T;
	fin >> T;

	for (int t=0; t<T; t++) {
		int R, C;
		fin >> R >> C;
		for (int r=0; r<R; r++) {
			fin >> pic[r];
		}
		memset(pic[R], 0, C);

		for (int r=0; r<R; r++) {
			for (int c=0; c<C; c++) {
				if (pic[r][c]=='#' && pic[r][c+1]=='#' && pic[r+1][c]=='#' && pic[r+1][c+1]=='#'){
					pic[r][c]='/';
					pic[r][c+1]='\\';
					pic[r+1][c]='\\';
					pic[r+1][c+1]='/';
				}
			}
		}
		bool possible=true;
		for (int r=0; r<R && possible; r++) {
			for (int c=0; c<C && possible; c++) {
				possible = pic[r][c]!='#';
			}
		}

		std::cout << "Case #" << (t + 1) << ":" << "\n";
		if (possible) {
			for (int r=0; r<R && possible; r++) {
				std::cout << pic[r] << "\n";
			}
		} else {
			std::cout << "Impossible\n";
		}
	}
}

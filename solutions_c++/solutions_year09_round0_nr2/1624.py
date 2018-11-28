/* 
 * File:   main.cpp
 * Author: maul
 *
 * Created on 2009. szeptember 3., 0:11
 *
 * //B
 */

#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <stack>

/*
 * 
 */


int main(int argc, char** argv)
{

	unsigned int T;
	std::cin >> T;


	for (unsigned int i = 0; i < T; i++) {

		unsigned int H, W;
		std::cin >> H;
		std::cin >> W;

		std::vector< std::vector<long int> > pool(H, std::vector<long int>(W, 0));
		std::vector< std::vector<long int> > target(H, std::vector<long int>(W, 0));

		for (unsigned int h = 0; h < H; h++) {
			for (unsigned int w = 0; w < W; w++) {
				long int t;
				std::cin >> t;
				pool[h][w] = t;
			}
		}

		for (unsigned int y = 0; y < H; y++) {
			for (unsigned int x = 0; x < W; x++) {

				std::vector<long int> tvect(4);
				if (y == 0) tvect[0] = 999999;
				else tvect[0] = pool[y - 1][x];
				if (x == 0) tvect[1] = 999999;
				else tvect[1] = pool[y][ x - 1];
				if (x == W - 1) tvect[2] = 999999;
				else tvect[2] = pool[y][ x + 1];
				if (y == H - 1) tvect[3] = 999999;
				else tvect[3] = pool[y + 1][ x];

				unsigned int t = pool[y][ x];

				if (t <= tvect[0] && t <= tvect[1] && t <= tvect[2] && t <= tvect[3]) {
					target[y][ x] = -1;

				} else {
					unsigned int minp = 0;
					for (unsigned int j = 1; j < 4; j++) {
						if (tvect[minp] > tvect[j]) minp = j;
					}
					if (minp == 0)
						target[y][ x] = (y - 1) * W + x;
					else if (minp == 1) target[y][ x] = y * W + x - 1;
					else if (minp == 2) target[y][ x] = y * W + x + 1;
					else if (minp == 3) target[y][ x] = (y + 1) * W + x;
				}
			}
		}

		std::vector< std::vector<unsigned int> > basins(H, std::vector<unsigned int>(W, 99));
		unsigned int curbas = 0;

		for (unsigned int h = 0; h < H; h++) {
			for (unsigned int w = 0; w < W; w++) {
				if (basins[h][w] == 99) {
					long int start = h * W + w;
					while (target[start/W][start%W] != -1) start = target[start / W][start % W];
					
					basins[start / W][start % W] = curbas;
					std::stack<unsigned int> ts;
					ts.push(start);
					while (!ts.empty()) {
						long int cur = ts.top();
						ts.pop();
						if (cur / W != 0) if (target[cur / W - 1][cur % W] == cur) ts.push(cur - W);
						if (cur / W != H - 1) if (target[cur / W + 1][cur % W] == cur) ts.push(cur + W);
						if (cur % W != 0) if (target[cur / W][cur % W - 1] == cur) ts.push(cur - 1);
						if (cur % W != W - 1) if (target[cur / W][cur % W + 1] == cur) ts.push(cur + 1);
						//if ((cur / W != h) && (cur % W != w)) target[cur / W][cur % W] = h * W + w;
						basins[cur / W][cur % W] = curbas;
					}
					curbas++;
				}
			}
		}

		std::cout << "Case #" << i + 1 << ": " << "\n";
		for (unsigned int h = 0; h < H; h++) {
			for (unsigned int w = 0; w < W; w++) {
				std::cout.put(97 + basins[h][w]);
				std::cout << " ";
				//if (target[h][w] == -1) std::cout << " s  ";
				//else
				//std::cout << target[h][w] / W  << ":" <<target[h][w] % W << " ";
			}
			std::cout << "\n";
		}

	}


	return(EXIT_SUCCESS);
}


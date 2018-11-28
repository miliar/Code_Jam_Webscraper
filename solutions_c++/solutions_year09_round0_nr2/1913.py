#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		int H, W;
		cin >> H >> W;
		
		int attitude[H+2][W+2];
		char basin[H+2][W+2];
		
		for (int h = 0; h < H+2; ++h) {
			attitude[h][0] = attitude[h][W+1] = 99999;
		}
		for (int w = 0; w < W+2; ++w) {
			attitude[0][w] = attitude[H+1][w] = 99999;
		}
		
		for (int h = 1; h <= H; ++h) {
			for (int w = 1; w <= W; ++w) {
				cin >> attitude[h][w];
				basin[h][w] = 0;
			}
		}
		
		char basin_char = 'a';
		
		for (int h = 1; h <= H; ++h) {
			for (int w = 1; w <= W; ++w) {
				if (basin[h][w]) continue;
				
				int h0 = h, w0 = w;
				for (;;) {
					if (basin[h0][w0]) break;
					int h1 = h0    , w1 = w0    ;
					int hN = h0 - 1, wN = w0    ;
					int hW = h0    , wW = w0 - 1;
					int hE = h0    , wE = w0 + 1;
					int hS = h0 + 1, wS = w0    ;
					if (attitude[h1][w1] > attitude[hN][wN]) { h1 = hN; w1 = wN; }
					if (attitude[h1][w1] > attitude[hW][wW]) { h1 = hW; w1 = wW; }
					if (attitude[h1][w1] > attitude[hE][wE]) { h1 = hE; w1 = wE; }
					if (attitude[h1][w1] > attitude[hS][wS]) { h1 = hS; w1 = wS; }
					if (h0 == h1 && w0 == w1) break;
					h0 = h1; w0 = w1;
				}
				
				if (basin[h0][w0] == 0) {
					basin[h0][w0] = basin_char++;
				}
				basin[h][w] = basin[h0][w0];
			}
		}

		cout << "Case #" << t << ":" << endl;
		for (int h = 1; h <= H; ++h) {
			for (int w = 1; w <= W; ++w) {
				cout << basin[h][w] << " ";
			}
			cout << endl;
		}
	}
}

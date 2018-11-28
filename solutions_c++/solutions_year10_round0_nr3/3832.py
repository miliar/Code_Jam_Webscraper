// Shawn Hoffman <godisgovernment@gmail.com>
#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdint.h>

int main() {
	std::ifstream in("C-small-attempt0.in");
	std::ofstream out("C-small-attempt0.out", std::ifstream::out | std::ifstream::trunc);
	
	uint32_t T;
	in >> T;
	for (uint32_t x = 0; x < T; x++) {
		uint32_t R, k, N;
		uint32_t y = 0;
		
		in >> R >> k >> N;
		uint32_t *g = new uint32_t[N];
		
		for (uint32_t n = 0; n < N; n++) {
			in >> g[n];
		}
		
		uint32_t pos = 0;
		for (uint32_t i = 0; i < R; i++) {
			uint32_t groups = 0, num_now = 0;

			while ((num_now + g[pos] <= k) && (groups < N)) {
				num_now += g[pos];
				pos = (pos + 1) % N;
				groups++;
			}
			y += num_now;
		}
		
		out << "Case #" << x + 1 << ": " << y << std::endl;
		
		delete[] g;
	}
	
	in.close();
	out.close();
	return 0;
}




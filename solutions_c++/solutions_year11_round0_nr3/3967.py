// -*- Mode: c++; Coding: utf-8; tab-width: 4; -*-
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

std::pair<int, std::vector<int> > parseProblem(std::iostream& stream) {
	int count = 0;
	std::vector<int> result;
	stream >> count;
	for (int i = 0; i < count; ++i) {
		int v = 0;
		stream >> v;
		result.push_back(v);
	}
	return std::make_pair(count, result);
}

int calcValues(int pat, const std::vector<int>& candies) {
	int sean = 0;
	int patrickHas = 0;
	int patrickGive = 0;

	for (int i = 0; i < candies.size(); ++i) {
		if (pat & (1 << i)) {
			sean += candies[i];
			patrickGive ^= candies[i];
		} else {
			patrickHas ^= candies[i];
		}
	}
	if (patrickHas == patrickGive) {
		return sean;
	}
	return -1;
}

int solv(int count, const std::vector<int>& candies) {
	int maxCount = 1 << count;
	int max = -1;
	for (int i = 1; i < maxCount-1; ++i) {
		int v = calcValues(i, candies);
		if (v >= 0) {
			if (max < v) {
				max = v;
			}
		}
	}
	return max;
}

int main(int argc, char *argv[]) {
	if (argc < 2) {
		std::cout << "usage: " << std::endl;
		return 0;
	}
	std::fstream file(argv[1], std::fstream::in);
	while (!file.eof()) {
		int dataCount = 0;
		file >> dataCount;
		for (int i = 0; i < dataCount; ++i) {
			std::pair<int, std::vector<int> > probs = parseProblem(file);
			int v = solv(probs.first, probs.second);
			std::cout << "Case #" << (i+1) << ": ";
			if (v < 0) {
				std::cout << "NO" << std::endl;
			} else {
				std::cout << v << std::endl;
			}
		}
	}
	file.close();

	return 0;
}

#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>

std::ifstream infile("input.txt");
std::ofstream outfile("output.txt");

typedef struct {
	uint16_t totalPoints;
	uint16_t estimatedTriple[3];
} Googler;

typedef std::vector<Googler> Googlers;

#define DEBUG false

int main(int argc, char *argv[]) {
	uint64_t testcases, iteration;
	infile >> testcases;
	for(iteration = 0; iteration < testcases; iteration++) {
		unsigned int googlers, surprising, threshold, successors = 0;
		infile >> googlers;
		infile >> surprising;
		infile >> threshold;


		if(DEBUG) std::cout << "Googlers: " << googlers << " (" << surprising << " surprising, " << threshold << " threshold)" << std::endl;

		unsigned char index;
		for(index = 0; index < googlers; index++) {
			Googler googler;
			infile >> googler.totalPoints;

			if(DEBUG) std::cout << "\tGoogler " << (int)index << " has " << googler.totalPoints << " points" << std::endl;

			googler.estimatedTriple[0] = googler.totalPoints / 3;
			googler.estimatedTriple[1] = (googler.totalPoints - googler.estimatedTriple[0]) / 2;
			googler.estimatedTriple[2] = googler.totalPoints - googler.estimatedTriple[1] - googler.estimatedTriple[0];

			if(DEBUG) std::cout << "\t\tEstimated triple: " << googler.estimatedTriple[0] << ", " << googler.estimatedTriple[1] << ", " << googler.estimatedTriple[2] << std::endl;
			if(DEBUG) std::cout << "\t\tBest: " << googler.estimatedTriple[2]  << std::endl;

			if(googler.estimatedTriple[2] >= threshold) {
				if(DEBUG) std::cout << "\t\tSuccessor!" << std::endl;
				++successors;
			} else if(surprising > 0 && googler.totalPoints > 0 && googler.estimatedTriple[2] + 1 >= threshold) {
				if((googler.estimatedTriple[2] + 1) - (googler.estimatedTriple[1] - 1) <= 2) {
					if(DEBUG) std::cout << "\t\tSuccessor (surprising)!" << std::endl;

					++successors;
					--surprising;
				}
			}
		}

		outfile << "Case #" << (iteration + 1) << ": " << successors << std::endl;
	}
	
	infile.close();
	outfile.close();
	return 0;
}

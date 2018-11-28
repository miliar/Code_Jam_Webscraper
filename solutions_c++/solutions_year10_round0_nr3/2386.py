
#include <iostream>
#include <fstream>
#include <vector>
#include <boost/filesystem/path.hpp>
#include <assert.h>


int trial_revenue(std::ifstream& infile) {
	int R, k, N, g_tot;
	std::vector<int> g;
	std::vector<bool> mark;

	infile >> R >> k >> N;
	g.resize(N);
	mark.resize(N,false);

	g_tot=0;
	for (int i=0; i<N; i++) {
		infile >> g[i];
		g_tot+=g[i];
	}
	// quick exit for easy case
	if (g_tot<=k) {
		return R*g_tot;
	}


	// start counting
	int index = 0;
	int revenue = 0;
	while (!mark[index] && R>0) {
		// this is a new sequence, so see where it takes us...
		mark[index]=true;
		int subtot=g[index];
		while (subtot<=k) {
			revenue += g[index];
			if (++index>=N)
				index =0;
			subtot+=g[index];
		}
		// subtot is now overflow - so index points to next sequence starter.
		R--; // count the ride against the max
	}
	if (R<=0)
		return revenue;

	// at this point we're looking at a repeating sequence
	int repeat=index;
	int seq_dR=0;
	int seq_drev=0;
	while (mark[repeat] && R>0) {
		int subtot=g[index];
		while (subtot<=k) {
			revenue += g[index];
			seq_drev += g[index];
			if (++index>=N)
				index =0;
			subtot+=g[index];
		}
		// subtot is now overflow - so index points to next sequence starter.
		R--; // count the ride against the max
		seq_dR++; // also count it towards sequence # of rides
		mark[index]=false;
	}
	assert(index == repeat);
	if (R<=0)
		return revenue;

	// now take out as much as possible via division
	revenue += seq_drev*(R/seq_dR);
	R-=(R/seq_dR)*seq_dR;
	assert(R>=0 && R<N && R<seq_dR);
	if (R<=0)
		return revenue;

	// now mop up
	while (R>0) {
		int subtot=g[index];
		while (subtot<=k) {
			revenue += g[index];
			if (++index>=N)
				index =0;
			subtot+=g[index];
		}
		// subtot is now overflow - so index points to next sequence starter.
		R--; // count the ride against the max
	}

	return revenue;
}

int codejam_solve(std::ifstream& infile, std::ofstream& outfile) {
	//Problem 3 - Theme Park
	int T, revenue;

	infile >> T;

	for (int trial=0; trial<T; trial++) {
		revenue = trial_revenue(infile);
		std::cout << "Case #" << trial+1 << ": " << revenue << std::endl;
		outfile << "Case #" << trial+1 << ": " << revenue << std::endl;
	}

	return 0;
}

int main(int argc, char* argv[])
{
	std::ifstream infile;
	std::ofstream outfile;

	boost::filesystem::path relpath(boost::filesystem::path(argv[0]).parent_path());
	boost::filesystem::path input_file_path;
	if (argc<=1) {
		std::cout << "input file?" << std::endl;
		std::cin >> input_file_path;
	}
	else
		input_file_path=argv[1];

	if (!input_file_path.has_root_path())
		input_file_path=relpath/input_file_path;

	infile.open(input_file_path.file_string().c_str());
	if (!infile) {
		std::cout << "couldn't find input" << std::endl;
		return -1;
	}
	outfile.open((relpath/"results.txt").file_string().c_str());
	if (!outfile) {
		std::cout << "couldn't open output" << std::endl;
		return -2;
	}

	return codejam_solve(infile, outfile);
}



#include <iostream>
#include <fstream>
#include <boost/filesystem/path.hpp>


int codejam_solve(std::ifstream& infile, std::ofstream& outfile) {
	//Problem 1 - Snapper

	unsigned int i, t, n, k, test;

	infile >> t;

	for (i=0;i<t;i++) {
		std::cout << "Case #" << (i+1) << ": ";
		outfile << "Case #" << (i+1) << ": ";
		infile >> n >> k;
		test = (1UL<<n)-1;
		std::string state = (((k+1)&test)==0) ? "ON" : "OFF";
		std::cout << state << std::endl;
		outfile << state << std::endl;
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


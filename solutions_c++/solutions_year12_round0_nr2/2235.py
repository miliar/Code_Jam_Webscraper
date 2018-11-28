//============================================================================
// Author      : Dominik Schnitzer, <dominik@schnitzer.at>
// Copyright   : Public Domain
// Description : Google Code Jam 2010 A
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>


template <class T>
std::vector<T> str2vector(std::string s)
{
    std::istringstream is(s);
    std::vector<T> res;
    while (!is.eof()) {
        T item;
        is >> item;
        res.push_back(item);
    }
    return res;
}


std::string process_case(int testcase, std::vector<std::string> input)
{
    // output string
    std::ostringstream o;

    // read input
    std::vector<std::string> W = str2vector<std::string>(input[0]);

    // compute solution
    for (size_t i = 0; i < W.size(); i++) {

        o << W[W.size() - i - 1];
        if (i != (W.size()-1)) {
            o << " ";
        }
    }

    // format solution
    std::ostringstream solution;
    solution << "Case #" << testcase << ": " << o.str() << std::endl;

    return solution.str();
}


void write_file(const char* ofile_path, std::vector<std::string>& ovec)
{
    std::cout << "Writing to file: " << ofile_path << std::endl;
    std::ofstream ofile(ofile_path, std::ofstream::out | std::ofstream::trunc);
    if (!ofile.good()) {
        ofile.close();
        std::cerr << "Error writing to file." << std::endl;
        return;
    }

    for (size_t i = 0; i < ovec.size(); i++) {
        ofile << ovec[i];
    }

    ofile.close();

}


std::vector<std::vector<std::string> > read_file(const char* ifile_path)
{
    std::vector<std::vector<std::string> > ivec;
    std::cout << "Reading from file: " << ifile_path << std::endl;
    std::ifstream ifile(ifile_path, std::ifstream::in);

    if (!ifile.good()) {
        ifile.close();
        std::cerr << "Error reading from file." << std::endl;
        return ivec;
    }

    // read header
    size_t testcases;
    std::string header;
    std::getline(ifile, header);
    std::vector<size_t> v_testcases = str2vector<size_t>(header);
    testcases = v_testcases[0];
    std::cout << "Found testcases: " << testcases << std::endl;


    for (size_t i = 0; i < testcases; i++) {
        // current testcase number
        size_t cur = i+1;

        // read testcase
        std::vector<std::string> testcase;
        std::string line;
        std::getline(ifile, line);
        testcase.push_back(line);

        // debug output
        std::cout << "-- Begin testcase #" << cur << " --" << std::endl;
        for (size_t j = 0; j < testcase.size(); j++) {
            std::cout << testcase[j] << std::endl;
        }
        std::cout << "-- End testcase #" << cur << " --" << std::endl;

        ivec.push_back(testcase);
    }

    ifile.close();

    return ivec;
}


int main(int argc, char *argv[])
{
    std::cout << "Google Code Jam" << std::endl;
    std::cout << "Dominik Schnitzer" << std::endl;

    if (argc != 3) {
        std::cerr << "No input and output files given!" << std::endl;
        std::cerr << "Synopsis: " << argv[0] << " input-file output-file"
                << std::endl;
        return 1;
    }

    const char* ifile_path = argv[1];
    const char* ofile_path = argv[2];

    // read input
    std::vector<std::vector<std::string> > ivec = read_file(ifile_path);
    size_t testcases = ivec.size();

    // multithreaded processing
    std::vector<std::string> ovec(testcases);
#ifdef _OPENMP
    #pragma omp parallel default(shared)
    #pragma omp for
#endif
    for (size_t i = 0; i < testcases; i++) {
        // current testcase number
        size_t cur = i+1;
        ovec[i] = process_case(cur, ivec[i]);
    }


    // write output
    write_file(ofile_path, ovec);


    return 0;
}

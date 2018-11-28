//============================================================================
// Author      : Dominik Schnitzer, <dominik@schnitzer.at>
// Copyright   : Public Domain
// Description : Google Code Jam 2010 A
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <stdlib.h>
#include <utility>
#include <boost/unordered_set.hpp>

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
    std::vector<int> in = str2vector<int>(input[0]);

    int A = in[0];
    int B = in[1];

//    std::stringstream o;
    boost::unordered_set<std::pair<int, int> > imap;
    int c = 0;

    // upper limit check
    for (int n = A; n <= B; n++) {

        std::stringstream out;
        out << n;
        std::string s = out.str();

        // skip single digits
        if (s.length() == 1) {
            break;
        }

        // generate numbers and check if they are in the ranges
        std::string snew = s;
        int slen = s.length();
        for (int j = 1; j < slen; j++) {

            //generate integer
            snew = snew.substr(1, slen-1) + snew.substr(0, 1);

            // invalid as leading 0
            if (snew[0] == '0') {
                continue;
            }

            int m = atoi(snew.c_str());
            if ((m >= A) && (m <= B) && (n < m)) {
//                o << "n=" << n << ", m=" << m << std::endl;
                std::pair<int, int> p(n, m);
                imap.insert(p);
                c++;
            }
        }
    }

    // format solution
    std::ostringstream solution;
//    solution << "Debug: " << o.str();
    solution << "Case #" << testcase << ": " << imap.size() << std::endl;

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

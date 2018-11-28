#include <algorithm>
#include <deque>
#include <iostream>

// Using boost version 1.45.0 from
// http://www.boost.org/users/history/
#include <boost/lexical_cast.hpp>

// Using google-gflags version 1.5 from
// http://code.google.com/p/google-gflags/
#include <gflags/gflags.h>

// Using google-glog version 0.3.1-1 from
// http://code.google.com/p/google-glog/
#include <glog/logging.h>

#include "input.hpp"

int code_jam_main(int argc, char ** argv, int test_case)
{
    LOG(INFO) << "Starting test case #" << test_case;
    int pieces = input::read<int>();
    std::deque<int> values;
    input::read<std::deque<int>, int>(&values);
    std::sort(values.begin(), values.end());
    int total_patrick_value = 0;
    for (int i = 0; i < pieces; ++i) {
        total_patrick_value ^= values[i];
    }
    if (total_patrick_value != 0) {
        LOG(INFO) << "NO Solution";
        std::cout << "Case #" << test_case << ": NO" << std::endl;
    } else {
        LOG(INFO) << "Patrick will be happy with just the least valuable piece";
        int total_sean_value = 0;
        for (int i = 1; i < pieces; ++i) {
            total_sean_value += values[i];
        }
        std::cout << "Case #" << test_case << ": " << total_sean_value << std::endl;
    }
    return 0;
}

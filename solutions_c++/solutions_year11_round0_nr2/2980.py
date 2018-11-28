#include <algorithm>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <string>

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
    std::deque<std::string> input;
    input::read<std::deque<std::string>, std::string>(&input);
    int number_of_combos = boost::lexical_cast<int>(input.front());
    input.pop_front();
    std::map<std::string, std::string> combos;
    for (int i = 1; i <= number_of_combos; ++i) {
        std::string combo = input.front();
        LOG(INFO) << "Combo #" << i << " = " << combo;;
        input.pop_front();
        std::string key1 = combo.substr(0,2);
        std::string key2 = std::string(1, key1[1]) + key1[0];
        std::string value = combo.substr(2, 1);
        LOG(INFO) << "Adding " << key1 << " maps to " << value;
        combos[key1] = value;
        LOG(INFO) << "Adding " << key2 << " maps to " << value;
        combos[key2] = value;
    }
    int number_of_oppositions = boost::lexical_cast<int>(input.front());
    input.pop_front();
    std::map<std::string, std::string> oppositions;
    for(int i = 1; i <= number_of_oppositions; ++i) {
        std::string opposition = input.front();
        LOG(INFO) << "Opposition # " << i << " = " << opposition;
        input.pop_front();
        std::string e1 = std::string(1, opposition[0]);
        std::string e2 = std::string(1, opposition[1]);
        LOG(INFO) << e1 << " -> " << e2;
        LOG(INFO) << e2 << " -> " << e1;
        oppositions[e1] = e2;
        oppositions[e2] = e1;
    }
    int number_of_elements = boost::lexical_cast<int>(input.front());
    input.pop_front();
    std::string elements = input.front();
    LOG(INFO) << "Elements: " << elements;
    std::deque<char> output;
    for (int i = 0; i < number_of_elements; ++i) {
        std::string element = std::string(1, elements[i]);
        LOG(INFO) << "Processing element " << element;
        if (output.size() == 0) {
            output.push_back(element[0]);
        } else {
            std::string last_two = std::string(1, output.back()) + element;
            LOG(INFO) << "Checking if " << last_two << " is a combo";
            if (combos.find(last_two) != combos.end()) {
                LOG(INFO) << "It is a combo";
                char new_last_char = combos[last_two][0];
                LOG(INFO) << "Replacing the last char with " << new_last_char;
                output.pop_back();
                output.push_back(new_last_char);
            } else {
                LOG(INFO) << "Checking if " << element << " causes an opposition";
                if (oppositions.find(element) != oppositions.end()) {
                    LOG(INFO) << element << " is part of an opposition";
                    
                    if (std::find(output.begin(), output.end(), oppositions[element][0]) != output.end()) {
                        LOG(INFO) << "And its pair is in the output. Clearing";
                        output.clear();
                    } else {
                        output.push_back(elements[i]);
                    }
                } else {
                    output.push_back(elements[i]);
                }
            }
        }
    }

    std::cout << "Case #" << test_case << ": [";
    for (size_t i = 1; i <= output.size(); ++i) {
        std::cout << std::string(1, output[i - 1]);
        if (i != output.size()) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
    return 0;
}

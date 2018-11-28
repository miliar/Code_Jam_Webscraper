#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <limits.h>

unsigned long cur_min = ULONG_MAX;

std::set<char> diffNumbers(std::string number){
    std::set<char> tmp;
    for(unsigned i = 0; i < number.size(); i++){
        tmp.insert(number[i]);
    }

    return tmp;
}

unsigned long intPow(unsigned x, unsigned p){
    unsigned long r = 1;
    for(unsigned i = 0; i < p; i++){
        r *= x;
    }
    return r;
}

unsigned long findMin(std::string number, unsigned index, std::vector<unsigned> remaining_numbers, std::map<char, unsigned> cur_mapping, unsigned long cur_sum, unsigned base){
    if(cur_sum > cur_min){
        return cur_sum;
    }

    if(index >= number.size()){
        return cur_sum;
    }

    std::map<char, unsigned>::iterator it = cur_mapping.find(number[index]);
    if(it != cur_mapping.end()){
        return findMin(number, index+1, remaining_numbers, cur_mapping, cur_sum + it->second*intPow(base, number.size()-index-1), base);
    }

    unsigned long child_min = ULONG_MAX;
    for(unsigned i = 0; i < remaining_numbers.size(); i++){
        if(index == 0 && remaining_numbers[i] == 0){
            continue;
        }
        std::map<char, unsigned> new_mapping = cur_mapping;
        unsigned m = remaining_numbers[i];
        new_mapping[number[index]] = m;

        std::vector<unsigned> new_remaining_numbers = remaining_numbers;
        new_remaining_numbers[i] = new_remaining_numbers.back();
        new_remaining_numbers.pop_back();

        unsigned long r = findMin(number, index+1, new_remaining_numbers, new_mapping,  cur_sum + m*intPow(base, number.size()-index-1), base);
        if(r < child_min){
            child_min = r;
        }
    }

    return child_min;
}

unsigned long findMin(std::string number){
    std::set<char> symbols = diffNumbers(number);
    unsigned min_base = symbols.size();
    for(unsigned cur_base = min_base; cur_base <= 36; cur_base++){
        std::vector<unsigned> available_numbers;
        for(unsigned i = 0; i < cur_base; i++){
            available_numbers.push_back(i);
        }
        unsigned long bm = findMin(number, 0, available_numbers, std::map<char, unsigned>(), 0, cur_base);
        if(bm < cur_min){
            cur_min = bm;
        }
    }

    return cur_min;
}

int main(int argc, char **argv){
    unsigned num_inputs;
    std::cin >> num_inputs;

    for(unsigned i = 0; i < num_inputs; i++){
        cur_min = ULONG_MAX;

        std::string number;
        std::cin >> number;

        unsigned long min = findMin(number);
        std::cout << "Case #" << i+1 << ": " << min << std::endl;
    }

    return 0;
}


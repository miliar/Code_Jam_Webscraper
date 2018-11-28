
#include <vector>
#include <iostream>
#include <cassert>
#include <string>

struct IndexEntry {
    std::vector<unsigned> all_matches;
    std::vector<int> num_result_matches;
    unsigned earliest_match, latest_match;
};

const std::string find_string("welcome to code jam");
std::vector<struct IndexEntry> index_matches;


void filterIndexMatches(void){
    for(unsigned i = 1; i < index_matches.size(); i++){
        std::vector<unsigned> filtered_matches;
        unsigned earliest = 0;
        bool found_earliest = false;

        for(unsigned j = 0; j < index_matches[i].all_matches.size(); j++){
            if(index_matches[i].all_matches[j] > index_matches[i-1].earliest_match){
                filtered_matches.push_back(index_matches[i].all_matches[j]);
                if(!found_earliest || filtered_matches.back() < earliest){
                    found_earliest = true;
                    earliest = filtered_matches.back();
                }
            }
        }
        index_matches[i].earliest_match = earliest;
        index_matches[i].all_matches = filtered_matches;
    }

    for(unsigned i = 0; i < index_matches.size()-1; i++){
        std::vector<unsigned> filtered_matches;
        unsigned latest = 0;
        bool found_latest = false;

        for(unsigned j = 0; j < index_matches[i].all_matches.size(); j++){
            if(index_matches[i].all_matches[j] < index_matches[i+1].latest_match){
                filtered_matches.push_back(index_matches[i].all_matches[j]);
                if(!found_latest || filtered_matches.back() > latest){
                    found_latest = true;
                    latest = filtered_matches.back();
                }
            }
        }
        index_matches[i].latest_match = latest;
        index_matches[i].all_matches = filtered_matches;
    }

    for(unsigned i = 0; i < index_matches.size(); i++){
        index_matches[i].num_result_matches = std::vector<int>(index_matches[i].all_matches.size(), -1);

    }
}

void buildIndex(std::string cur_string){
    for(unsigned i = 0; i < find_string.size(); i++){
        struct IndexEntry cur_letter_index;
        bool found_earliest = false, found_latest = false;

        for(unsigned j = 0; j < cur_string.size(); j++){
            if(cur_string[j] == find_string[i]){
                cur_letter_index.all_matches.push_back(j);
                if(!found_earliest || j < cur_letter_index.earliest_match){
                    found_earliest = true;
                    cur_letter_index.earliest_match = j;
                }
                if(!found_latest || j > cur_letter_index.latest_match){
                    found_latest = true;
                    cur_letter_index.latest_match = j;
                }
            }
        }
        index_matches.push_back(cur_letter_index);
    }

    filterIndexMatches();
}

unsigned solve(unsigned index, unsigned left_margin){
    if(index >= find_string.size()){ return 0; }
    
    unsigned sum = 0;

    for(unsigned i = 0; i < index_matches[index].all_matches.size(); i++){
        if(index_matches[index].all_matches[i] >= left_margin){
            if(index_matches[index].num_result_matches[i] != -1){
                sum = (sum + (unsigned)index_matches[index].num_result_matches[i])%10000;
            }
            else{
                unsigned r;
                if(index == find_string.size()-1){
                    r = 1;
                }
                else{
                    r = solve(index+1, index_matches[index].all_matches[i]+1);
                }
                sum = (sum + r)%10000;
                index_matches[index].num_result_matches[i] = r;
            }
        }
    }

    //std::cout << sum << std::endl;
    return sum;
}


unsigned solveForString(std::string cur_string){
    buildIndex(cur_string);
   
    /*
    for(unsigned i = 0; i < index_matches.size(); i++){
        for(unsigned j = 0; j < index_matches[i].all_matches.size(); j++){
            std::cout << index_matches[i].all_matches[j] << " ";
        }
        std::cout << ": " << index_matches[i].earliest_match << " " << index_matches[i].latest_match << std::endl;
    }
    */

    unsigned sum = solve(0, 0);
    return sum;
}

int main(int argc, char **argv){
    unsigned num_tests = 0;
    std::cin >> num_tests;
    getchar();

    for(unsigned i = 0; i < num_tests; i++){
        index_matches.clear();

        std::string cur_string;
        char cur_char;
        while((cur_char = getchar()) != '\n'){
            cur_string.push_back(cur_char);
        }

        unsigned r = solveForString(cur_string);
        std::cout << "Case #" << i+1 << ": ";

        if(r >= 1000){ std::cout << r << std::endl; }
        else if(r >= 100){ std::cout << "0" << r << std::endl; }
        else if(r >= 10){ std::cout << "00" << r << std::endl; }
        else if(r >= 0){ std::cout << "000" << r << std::endl; }
    }


    return 0;
}


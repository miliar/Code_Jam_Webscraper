
#include <iostream>
#include <cassert>
#include <string>
#include <vector>

unsigned word_length = 0;
unsigned dict_length = 0;
unsigned test_cases = 0;

std::vector<std::string> dictionary;


std::vector<std::string> filterDictionary(const std::vector<std::string> &cur_dict, unsigned letter_pos, char letter){
    std::vector<std::string> result;
    for(unsigned i = 0; i < cur_dict.size(); i++){
        if(cur_dict[i].at(letter_pos) == letter){
            result.push_back(cur_dict[i]);
        }
    }
    return result;
}

unsigned getNumDictMatches(std::vector<std::string> dict, const std::vector<std::vector<char> > &word_options, unsigned cur_letter){
    unsigned sum = 0;
    if(dict.size() == 0){
        return 0;
    }

    if(cur_letter == word_options.size()-1){
        for(unsigned i = 0; i < word_options[cur_letter].size(); i++){
            sum += filterDictionary(dict, cur_letter, word_options[cur_letter][i]).size();
        }
    }
    else{
        for(unsigned i = 0; i < word_options[cur_letter].size(); i++){
            sum += getNumDictMatches(filterDictionary(dict, cur_letter, word_options[cur_letter][i]), 
                                     word_options, cur_letter+1);
        }
    }

    return sum;
}


void printWordOptions(const std::vector<std::vector<char> > &word_options){
    for(unsigned i = 0; i < word_options.size(); i++){
        assert(word_options[i].size() > 0);
        if(word_options[i].size() > 1){
            std::cout << "(";
            for(unsigned j = 0; j < word_options[i].size(); j++){
                std::cout << word_options[i][j];
            }
            std::cout << ")";
        }
        else {
            std::cout << word_options[i].front();
        }
    }
    std::cout << std::endl;
}

unsigned doTestCase(void){
    char cur_char;
    std::vector<std::vector<char> > word_options;

    while((cur_char = getchar()) != '\n' && cur_char != EOF){
        std::vector<char> new_word_option;
        if(cur_char == '('){
            while((cur_char = getchar()) != ')'){
                new_word_option.push_back(cur_char);
            }
        }
        else{
            new_word_option.push_back(cur_char);
        }
        word_options.push_back(new_word_option);
    }

    assert(word_options.size() > 0);
    //printWordOptions(word_options);
    return getNumDictMatches(dictionary, word_options, 0);
}

void printDictionary(void){
    for(unsigned i = 0; i < dictionary.size(); i++){
        std::cout << dictionary[i] << std::endl;
    }
}

void readDictionary(void){
    for(unsigned i = 0; i < dict_length; i++){
        std::string dict_word;
        std::cin >> dict_word;
        assert(dict_word.length() == word_length);

        dictionary.push_back(dict_word);
    }
}

int main(int argc, char **argv){
    std::cin >> word_length;
    std::cin >> dict_length;
    std::cin >> test_cases;

    readDictionary();
    //printDictionary();
    getchar();

    for(unsigned i = 0; i < test_cases; i++){
        unsigned r = doTestCase();
        std::cout << "Case #" << (i+1) << ": " << r << std::endl;
    }

    return 0;
}


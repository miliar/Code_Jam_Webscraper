#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <stdlib.h>

char rules[] = {
    'y',
    'h',
    'e',
    's',
    'o',
    'c',
    'v',
    'x',
    'd',
    'u',
    'i',
    'g',
    'l',
    'b',
    'k',
    'r',
    'z',
    't',
    'n',
    'w',
    'j',
    'p',
    'f',
    'm',
    'a',
    'q'
};

void Solve(std::string& line, std::string& answer) {
    answer.clear();
    for(int i=0; i<line.size(); i++) {
        if(line[i] == ' ') {
            answer.push_back(' ');
        }
        else {
            answer.push_back(rules[line[i]-97]);
        }
    }
}

int main(int argc, char** argv){
    int lines_number;
    scanf("%d\n", &lines_number);
    std::string line, answer;
    int test_case = 0;
    while(lines_number--){
        getline(std::cin, line);
        Solve(line, answer);
        std::cout << "Case #" << ++test_case << ": " << answer << std::endl;
    }
}

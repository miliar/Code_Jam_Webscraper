#include <iostream>
#include <string>
#include <map>

int main() {
    std::string alpha  = "abcdefghijklmnopqrstuvwxyz";
    std::string mapped = "yhesocvxduiglbkrztnwjpfmaq";
    std::map<char, char> table;
    for(int i=0, max=alpha.size(); i < max; ++i) {
        table[alpha[i]] = mapped[i];
    }
    
    std::string line;
    std::getline(std::cin, line);
    int t = atoi(line.c_str());
    for(int i=0; i < t; ++i) {
        std::string input;
        std::getline(std::cin, input);

        std::string output(input);
        for(int j=0, max=input.size(); j < max; ++j) {
            output[j] = (input[j] == ' ') ? ' ' : table[input[j]];
        }
        
        printf("Case #%d: %s\n", i+1, output.c_str());
    }

    return 0;
}

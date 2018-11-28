#include <iostream>
#include <vector>
#include <string>
#include <sstream>

bool good(char c, int p) {
    char letter[] = "XO";
    return (c == letter[p] || c == 'T');
}

int main() {
    int cases;
    std::cin >> cases;
    std::cin.ignore(1000, '\n');
    for(int c = 0; c < cases; c ++) {
        std::vector<std::string> data;
        
        std::string line;
        for(int i = 0; i < 4; i ++) {
            std::getline(std::cin, line);
            data.push_back(line);
        }
        std::getline(std::cin, line);  // skip blank line
        
        bool won[2] = {false, false};
        bool hasAnEmpty = false;
        
        for(int i = 0; i < 4; i ++) {
            for(int j = 0; j < 4; j ++) {
                if(data[i][j] == '.') hasAnEmpty = true;
            }
        }
        
        for(int p = 0; p < 2; p ++) {
            int i;
            for(i = 0; i < 4; i ++) {
                if(!good(data[i][i], p)) break;
            }
            if(i == 4) won[p] = true;
            
            for(i = 0; i < 4; i ++) {
                if(!good(data[3-i][i], p)) break;
            }
            if(i == 4) won[p] = true;
            
            for(int z = 0; z < 4; z ++) {
                for(i = 0; i < 4; i ++) {
                    if(!good(data[z][i], p)) break;
                }
                if(i == 4) won[p] = true;
                
                for(i = 0; i < 4; i ++) {
                    if(!good(data[i][z], p)) break;
                }
                if(i == 4) won[p] = true;
            }
        }
        
        std::cout << "Case #" << (c+1) << ": ";
        if(won[0] && won[1]) {
            std::cout << "Draw\n";
        }
        else if(won[0] && !won[1]) {
            std::cout << "X won\n";
        }
        else if(!won[0] && won[1]) {
            std::cout << "O won\n";
        }
        else {
            if(hasAnEmpty) {
                std::cout << "Game has not completed\n";
            }
            else std::cout << "Draw\n";
        }
    }
    
    return 0;
}

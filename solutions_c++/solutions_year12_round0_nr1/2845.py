#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int dic[256];

void makedic() {
    std::ifstream s("a-solver-src.txt");
    std::ifstream d("a-solver-dst.txt");

    int rdic[256];
    rdic['a'] = 'y';
    rdic['o'] = 'e';
    rdic['z'] = 'q';

    for(int i = 0 ; i< 3 ; i++) {
        std::string sl, dl;
        std::getline(s, sl);
        std::getline(d, dl);
        for(int j = 0; j < int(sl.length()) ; j++) {
            rdic[sl[j]] = dl[j];
            //std::cout << char(sl[j]) << " -> " << char(dl[j]) << std::endl;
        }
    }

    int r[256] ={0};
    for(int i = 'a'; i <= 'z' ; i++) {
        r[rdic[i]] = 1;
    }

    for(int i = 'a' ; i<= 'z' ; i++ ) {
        if (!r[i]) {
            rdic['q'] = 'z';
        }
    }

    for(int i = 'a' ; i <= 'z' ; i++) {
        dic[rdic[i]] = i;
    }

/*
    for(int i = 'a'; i <= 'z' ; i++) {
        std::cout << char(i) << " -> " << char(dic[i]) << std::endl;
    }
*/
}


int main() {
    dic[' '] = ' ';
    makedic();

    int T; std::cin >> T;
    std::string dummy; std::getline(std::cin, dummy);
    for(int i = 0 ; i < T ; i++) {
        std::string line;
        std::getline(std::cin, line);
        for(int j = 0 ; j < int(line.length()) ; j++) {
            line[j] = dic[line[j]];
        }
        std::cout << "Case #" << (i+1) << ": " << line << std::endl;
    }
    
    return 0;
}

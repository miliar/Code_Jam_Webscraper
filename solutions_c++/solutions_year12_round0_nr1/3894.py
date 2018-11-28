//
//  main.cpp
//  gcj
//
//  Created by Milo Brandt on 4/13/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <map>

void useMapping(std::map<char,char>& anti,const char* out,const char* in);
void useMapping(std::map<char,char>& anti,const char* out,const char* in){
    while(*out != 0){
        anti[*out] = *in;
        ++out;
        ++in;
    }
}
int main (int argc, const char * argv[])
{
    std::map<char, char> antiReplace;
    antiReplace['y'] = 'a';
    antiReplace['e'] = 'o';
    antiReplace['q'] = 'z';
    antiReplace['z'] = 'q';

    useMapping(antiReplace, "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    useMapping(antiReplace, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    useMapping(antiReplace, "de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    
    std::string x;
    std::cout << "Filename: ";
    std::cin >> x;
    std::ifstream in(x.c_str());
    std::ofstream out("/Users/Milo/Documents/boobs.txt");
    if(!in.is_open()){
        std::cout << "Macs suck.\n";
        return EXIT_FAILURE;
    }
    int trials;
    in >> trials;
    std::getline(in, x);
    for(int t = 1;t <= trials;++t){
        std::string str;
        std::getline(in, str);
        std::string ans;
        for(int i = 0;i < str.size();++i){
            char v = str[i];
            if((v < 'a' || v > 'z') && v != ' '){
                std::cout << v << ", " << (int)v << "\n";
            }
            ans += antiReplace[v];
        }
        std::cout << "\nCase #" << t << ": " << ans <<"\n";
        out << "Case #" << t << ": " << ans <<"\n";
    }
    out.close();
    in.close();
    return 0;
}


//
//  main.cpp
//  gcj
//
//  Created by Milo Brandt on 4/13/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <fstream>
#include <iostream>

int main (int argc, const char * argv[])
{
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
    for(int t = 1;t <= trials;++t){
        int N,S,p,ans;
        ans = 0;
        in >> N >> S >> p;
        int unsup = 3*p - 2;
        int sup = 3*p - 4;
        for(int i = 0;i < N;++i){
            int num;
            in >> num;
            std::cout << num << " ";
            if(p == 0){
                ++ans;
                continue;
            }
            if(p == 1){
                if(num != 0){
                    ++ans;
                }
                continue;
            }
            if(num >= unsup){
                ++ans;
                continue;
            }
            if(S != 0 && num >= sup){
                --S;
                ++ans;
                continue;
            }
        }
        std::cout << "\nCase #" << t << ": " << ans <<"\n";
        out << "Case #" << t << ": " << ans <<"\n";
    }
    out.close();
    in.close();
    return 0;
}


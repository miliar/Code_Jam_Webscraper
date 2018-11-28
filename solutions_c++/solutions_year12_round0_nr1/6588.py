#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
//#include <stdio.h>
using namespace std;


int main() {
    
    int t;
    int i,c;
    char dict[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    
    cin >> t;
    
    getchar();
    
    for(i = 0; i < t; i++){
        
        string line;
        getline(cin, line);
        
        for(c = 0; c < line.length(); c++) {
            if(line[c] == ' ')
                continue;
            line[c] = dict[line[c] - 97];
        }
        cout << "Case #" << i + 1 << ": " << line << endl; 
    }

    return 0;
}


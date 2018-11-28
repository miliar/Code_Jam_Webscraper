#include <iostream>
#include <fstream>
#include <string>

using namespace std;

std::string convert(std::string str) {
    static const std::string hint[] = {
         "ejp mysljylc kd kxveddknmc re jsicpdrysi"
        ,"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
        ,"de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };
    
    static const std::string hint1[] = {
        "our language is impossible to understand"
        ,"there are twenty six factorial possibilities"
        ,"so it is okay if you want to just give up"
    };
    std::string ans = "";
    for(int i = 0; i < str.length(); i++){
        int pos = std::string::npos;
        for(int j = 0; j < 3; j++){
            pos = hint[j].find(str[i]);
            if(pos != std::string::npos){
                ans += hint1[j][pos];
                break;
            }
        }
        if(pos == std::string::npos){
            ans += (str[i] == 'q') ? 'z' : 'q';
        }
    }
    return ans;
}

int main(int argc, char* argv[]){    
    
    int n;
    std::string str;
    std::getline(std::cin, str);
    char* temp = 0;
    n = strtol(str.c_str(), &temp, 0);
    for(int i = 0; i < n; i++){
        std::getline(std::cin, str);
        
        std::cout << "Case #" 
                << (i+1)
                << ": "
                << convert(str)
                << std::endl;
    }
    return 0;
}

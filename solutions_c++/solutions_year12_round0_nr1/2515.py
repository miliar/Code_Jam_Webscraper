#include <iostream>
#include <string>
#include <map>

std::string translate(std::map<char,char> const& m, std::string str)
{
    for(int i = 0; i < str.size(); ++i){
        try{
        if(str[i] != ' ')
        str[i] = m.at(str[i]);
        }catch(...){
            std::cout << str[i] << std::endl;
            throw;
        }
    }
    return str;
}

int main()
{
    std::string alpha = "abcdefghijklmnopqrstuvwxyz";
    
    std::string input = "z"
                        "y qee"
                        "ejp mysljylc kd kxveddknmc re jsicpdrysi"
                        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                        "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    std::string output = "q"
                         "a zoo"
                         "our language is impossible to understand"
                         "there are twenty six factorial possibilities"
                         "so it is okay if you want to just give up";
    
    std::map<char, char> m;
    for(int     i = 0; i < input.size(); ++i){
        m[input[i]] = output[i];
    }
    
    int t;
    std::string tmp;
    std::getline(std::cin, tmp);
    t = std::stoi(tmp);
    
    std::cin.unsetf(std::ios_base::skipws);
    for(int i = 0; i < t; ++i){
        std::string line;
        std::getline(std::cin, line);
        std::string x = translate(m, line);
        std::cout << "Case #" << i + 1 << ": " << x << std::endl;
    }
}




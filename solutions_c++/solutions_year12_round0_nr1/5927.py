#include <iostream>
#include <string>
#include <sstream>

const char* dict = "yhesocvxduiglbkrztnwjpfmaq";

int main(int argc, char** argv)
{
    int cases;
    std::string line;
    std::getline(std::cin, line);   // case count
    std::stringstream(line) >> cases;   
    for (int n = 0; n < cases; ++n)
    {
        std::cout << "Case #" << n + 1 << ": ";
        std::getline(std::cin, line);
        for (int i = 0; i < line.length(); ++i)
        {
            char c = line[i];
            if (c >= 'a' && c <= 'z')
            {
                std::cout << dict[c - 'a'];  
            }
            else
            {
                std::cout << c;
            }
        }
        std::cout << std::endl;
    }
}


#include <iostream>
#include <vector>
#include <string>

int main (int argc, const char * argv[])
{
    std::vector<char> mapping;
    mapping.push_back('y');
    mapping.push_back('h');
    mapping.push_back('e');
    mapping.push_back('s');
    mapping.push_back('o');
    mapping.push_back('c');
    mapping.push_back('v');
    mapping.push_back('x');
    mapping.push_back('d');
    mapping.push_back('u');
    mapping.push_back('i');
    mapping.push_back('g');
    mapping.push_back('l');
    mapping.push_back('b');
    mapping.push_back('k');
    mapping.push_back('r');
    mapping.push_back('z');
    mapping.push_back('t');
    mapping.push_back('n');
    mapping.push_back('w');
    mapping.push_back('j');
    mapping.push_back('p');
    mapping.push_back('f');
    mapping.push_back('m');
    mapping.push_back('a');
    mapping.push_back('p');
        
    
    int count;
    std::cin >> count;
    std::cin.ignore();
    
    for (int c = 0; c < count; c++)
    {
        std::string s;
        std::getline( std::cin, s );
        std::cout << "Case #"<< c + 1 << ": ";
        for(int i = 0; i < s.length(); i++)
        {
            if (s[i] == ' ')
                std::cout << ' ';
            else
                std::cout << mapping[s[i]-'a'];
        }
        std::cout <<std::endl;
    }
    return 0;
}




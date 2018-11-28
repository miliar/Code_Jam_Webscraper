#include <iostream>
#include <string>

char table[] = {
    'y', // a
    'h', // b
    'e', // c
    's', // d
    'o', // e
    'c', // f
    'v', // g
    'x', // h
    'd', // i
    'u', // j
    'i', // k
    'g', // l
    'l', // m
    'b', // n
    'k', // o
    'r', // p
    'z', // q
    't', // r
    'n', // s
    'w', // t
    'j', // u
    'p', // v
    'f', // w
    'm', // x
    'a', // y
    'q'  // z
};

int main(void)
{
    int T;
    std::cin >> T;
    std::string s;
    std::getline(std::cin, s);
    for (int t = 1; t <= T; ++t) {
        std::getline(std::cin, s);
        for (unsigned i = 0; i < s.size(); ++i)
            if (s[i] >= 'a' && s[i] <= 'z')
                s[i] = table[s[i] - 'a'];
        std::cout << "Case #" << t << ": " << s << std::endl;
    }
}
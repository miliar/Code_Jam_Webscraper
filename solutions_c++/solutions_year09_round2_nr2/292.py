#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        std::string s;
        std::cin >> s;
        if (next_permutation(s.begin(), s.end())) {
            std::cout << "Case #" << i << ": " << s << std::endl;
        } else {
            int l = s.length();
            int pos;
            while (s[0] == '0') {
                s=s.substr(1);
            }
            std::string novy = s.substr(0,1);
            for (int j = 0; j < l - s.length()+1; j++) {
                novy += "0";
            }
            novy += s.substr(1);
            std::cout << "Case #" << i << ": " << novy << std::endl;
        }
    }
}

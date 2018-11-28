#include <iostream>
#include <string>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int x = 0;
        int o = 0;
        int b = 1;
        bool f = true;
        for (int i = 0; i < 4; ++i) {
            std::string s;
            std::cin >> s;
            for (int j = 0; j < 4; ++j) {
                switch (s[j]) {
                case 'X':
                    x |= b;
                    break;
                case 'O':
                    o |= b;
                    break;
                case 'T':
                    x |= b;
                    o |= b;
                    break;
                default:
                    f = false;
                }
                b <<= 1;
            }
        }

        std::cout << "Case #" << t << ": ";

        if ((x & 0x1248) == 0x1248 || (x & 0x8421) == 0x8421 ||
            (x & 0x000f) == 0x000f || (x & 0x00f0) == 0x00f0 || (x & 0x0f00) == 0x0f00 || (x & 0xf000) == 0xf000 ||
            (x & 0x1111) == 0x1111 || (x & 0x2222) == 0x2222 || (x & 0x4444) == 0x4444 || (x & 0x8888) == 0x8888) {
            std::cout << "X won\n";
        }
        else if ((o & 0x1248) == 0x1248 || (o & 0x8421) == 0x8421 ||
            (o & 0x000f) == 0x000f || (o & 0x00f0) == 0x00f0 || (o & 0x0f00) == 0x0f00 || (o & 0xf000) == 0xf000 ||
            (o & 0x1111) == 0x1111 || (o & 0x2222) == 0x2222 || (o & 0x4444) == 0x4444 || (o & 0x8888) == 0x8888) {
            std::cout << "O won\n";
        }
        else if (f) {
            std::cout << "Draw\n";
        }
        else {
            std::cout << "Game has not completed\n";
        }
    }
}

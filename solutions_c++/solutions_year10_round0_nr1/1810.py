#include <iostream>
#include <map>
#include <set>
#include <vector>

int main(int argc, char *argv[])
{
    int ncases;
    std::cin >> ncases;
    for(int i = 1; i <= ncases; ++i)
    {
        int N, K;
        std::cin >> N >> K;

        int mask = (1 << N) - 1;
//        std::cerr << "K = " << K << ", mask = " << mask << ", ANDed value = " << (K&mask) << std::endl;
        bool powered = ((K & mask) == mask);

        std::cout << "Case #" << i << ": ";
        if(powered) {
            std::cout << "ON";
        } else {
            std::cout << "OFF";
        }
        std::cout << std::endl;
    }
}

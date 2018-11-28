#include <iostream>

int main()
{
    int T;
    std::cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
	unsigned N, K;
	std::cin >> N >> K;
	unsigned on = (1 << N) - 1;
	std::cout << "Case #" << cs << ": ";
	if (on > 0 && (K & on) == on)
	    std::cout << "ON" << std::endl;
	else
	    std::cout << "OFF" << std::endl;
    }
}

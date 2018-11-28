#include <iostream>
#include <string>

int main(int argc, char * argv[])
{
	int t;
	std::cin >> t;

	for (int i = 0; i < t; i++) {
		int N;
		long long K;
		std::cin >> N >> K;
		bool on = true;
		for (int j = 0; j < N && on; j++) {
			on = K & 1;
			K >>= 1;
		}
		
		std::cout << "Case #" << (i+1) << ": " << (on ? "ON" : "OFF") << "\n";
	}

	return 0;
}


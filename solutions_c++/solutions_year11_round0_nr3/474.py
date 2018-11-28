#include <iostream>
#include <cstdio>

int piece[1100];

int main()
{
    int t, n;

    //freopen("a.txt", "r", stdin);
	

	std::cin >> t;

	//freopen("b.txt", "w", stdout);

	for (int i = 0; i < t; i++) {
		std::cin >> n;
		int check = 0;
		for (int j = 0; j < n; j++) {
			std::cin >> piece[j];
		    check ^= piece[j];
		}
		if (check == 0) {
		    int sum = piece[0];
			int min = piece[0];
			for (int j = 1; j < n; j++) {
				sum += piece[j];
				if (piece[j] < min) min = piece[j];
			}
			std::cout << "Case #" << i + 1 << ": " << sum - min << std::endl;
		} else {
			std::cout << "Case #" << i + 1 << ": NO" << std::endl;
		}
	}
}
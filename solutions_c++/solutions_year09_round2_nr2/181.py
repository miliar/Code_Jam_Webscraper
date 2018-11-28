#include <algorithm>
#include <iostream>
#include <string>

int
main()
{
	int n, c = 0;
	std::cin >> n;
	while (n--) {
		std::string item;
		std::cin >> item;
		std::string seq(500, '0');
		seq.append(item);
		std::next_permutation(seq.begin(), seq.end());
		std::cout << "Case #" << ++c << ": "
			<< seq.substr(seq.find_first_not_of('0')) << '\n';
	}
}

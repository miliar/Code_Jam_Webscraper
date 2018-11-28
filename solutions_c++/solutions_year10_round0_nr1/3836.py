#include <iostream>

void writeResult(int which, std::string ans) {
	std::cout << "Case #" << which << ": " << ans << std::endl;
}

std::string isLampOn(int n, int k) {
	std::string result = "OFF";
	int backToInitial = 1 << n;

	k %= backToInitial;

	if ((backToInitial - 1) == k) {
		result = "ON";
	}

	return result;
}

int main(int argc, char **argv) {
	int count, n, k, i;

	std::cin >> count;

	for (i = 0; i < count; ++i) {
		std::cin >> n >> k;
		writeResult(i + 1, isLampOn(n, k));
	}
}

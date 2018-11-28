#include <iostream>
#include <string>

static int abs(int x) {
	return x>=0 ? x : -x;
}

struct Bot {
	int location;
	unsigned int time;
	Bot(): location(1), time(0) { }
	unsigned int push(int button, unsigned int minTime) {
		time += abs(button-location);
		if (time<minTime)
			time = minTime;
		location = button;
		return ++time;
	}
};

static unsigned int runTest() {
	unsigned int N;
	std::cin >> N;
	Bot bots[2];
	unsigned int time = 0;
	for (unsigned int i=0; i<N; i++) {
		std::string color;
		int button;
		std::cin >> color >> button;
		unsigned int botIndex = color=="O" ? 0 : 1;
		time = bots[botIndex].push(button, time);
	}
	return time;
}

int main() {
	unsigned int T;
	std::cin >> T;
	for (unsigned int i=0; i<T; i++)
		std::cout << "Case #" << (i+1) << ": " << runTest() << std::endl;
}


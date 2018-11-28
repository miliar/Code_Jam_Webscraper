#include <fstream>
#include <iostream>

char f(char c) {
	switch (c) {
		case 'X':
			return 0x0F;
		case 'O':
			return 0xF0;
		case 'T':
			return 0xFF;
		default:
			return 0x00;
	}
}

const char* findWinner(const char* test) {
	const char* xwin = "X won";
	const char* owin = "O won";
	const char* draw = "Draw";
	const char* active = "Game has not completed";

	char a;
	// Check for standard wins.
	for (int i = 0; i < 4; i++) {
		// Rows.
		int p = 4 * i;
		if (a = f(test[p]) & f(test[p + 1]) & f(test[p + 2]) & f(test[p + 3])) {
			return a == 0x0F ? xwin : owin;
		}

		// Columns.
		if (a = f(test[i]) & f(test[i + 4]) & f(test[i + 8]) & f(test[i + 12])) {
			return a == 0x0F ? xwin : owin;
		}
	}
	// Diagonals.
	if (a = f(test[0]) & f(test[5]) & f(test[10]) & f(test[15])) {
			return a == 0x0F ? xwin : owin;
	}
	if (a = f(test[3]) & f(test[6]) & f(test[9]) & f(test[12])) {
			return a == 0x0F ? xwin : owin;
	}

	// No wins, so check if there are any dots.
	a = 0;
	for (int i = 0; i < 16; i++) {
		a |= (test[i] == '.');
	}

	// If there are dots, it is ongoing. Otherwise, draw.
	return a ? active : draw;
}

int main(int argc, char* args[]) {
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	// File size.
	in.seekg(0, std::ios::end);
	int size = in.tellg();
	in.seekg(0, std::ios::beg);

	std::cout << "File size: " << size << std::endl;

	// Read the file into a buffer.
	char* buffer = new char[size + 1];
	in.read(buffer, size);

	// Number of tests and pointer.
	int num_tests = 0, ptr = 0;
	while ('0' <= buffer[ptr] && buffer[ptr] <= '9') num_tests = 10 * num_tests + (buffer[ptr] - '0'), ptr++;

	std::cout << "There are " << num_tests << " tests." << std::endl;

	// Advance to the next line.
	while (buffer[ptr] == '\r' || buffer[ptr] == '\n') ptr++;

	// For each test.
	for (int i = 0; i < num_tests; i++) {
		char test[17];
		for (int j = 0; j < 4; j++) {
			test[4 * j + 0] = buffer[ptr++];
			test[4 * j + 1] = buffer[ptr++];
			test[4 * j + 2] = buffer[ptr++];
			test[4 * j + 3] = buffer[ptr++];
			// Advance to the next line.
			while (buffer[ptr] == '\r' || buffer[ptr] == '\n') ptr++;
		}

		const char* msg = findWinner(test);

		out << "Case #" << (i + 1) << ": " << msg << std::endl;
		std::cout << "Case #" << (i + 1) << ": " << msg << std::endl;
	}
}

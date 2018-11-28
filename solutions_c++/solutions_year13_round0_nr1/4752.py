#include "InputParser.h"

InputParser::InputParser(const string& path) {
	fin.open(path, ios::in);
	assert (fin.is_open());
	getline(fin, line);
	assert (!fin.fail());
	// cerr << "[InputParser] InputParser() '" << line << "'" << endl;
	sin.str(line);
	sin.clear();
}

void InputParser::finishLine() {
	getline(fin, line);
	// cerr << "[InputParser] finishLine() <- '" << line << "'" << endl;
	sin.str(line);
	sin.clear();	
}

int64_t InputParser::readInt() {
	int64_t value;
	sin >> value;
	// cerr << "[InputParser] readInt() -> " << value << endl;
	assert (!sin.fail());
	return value;
}

uint64_t InputParser::readUInt() {
	uint64_t value;
	sin >> value;
	// cerr << "[InputParser] readUInt() -> " << value << endl;
	assert (!sin.fail());
	return value;
}

double InputParser::readReal() {
	double value;
	sin >> value;
	// cerr << "[InputParser] readReal() -> " << value << endl;
	assert (!sin.fail());
	return value;
}

char InputParser::readChar() {
	char value;
	sin >> value;
	// cerr << "[InputParser] readChar() -> " << value << endl;
	assert (!sin.fail());
	return value;
}

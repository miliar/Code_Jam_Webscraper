#ifndef UNIVERSE_SAVER_H
#define UNIVERSE_SAVER_H

#include <vector>
#include <string>
using namespace std;

class UniverseSaver {

private:
	vector<string> searchEngines;
	vector<string> queries;

	int getNextOccurPos(const string engineName, const int currentPos);

public:
	UniverseSaver(const vector<string> searchEngines, const vector<string> queries);
	int solve();

};
#endif
// SaveUniverse.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <vector>
#pragma warning(disable : 4996)

bool IsNameChar(char c) {
	if (c>='A' && c<='Z')
		return true;
	if (c>='a' && c<='z')
		return true;
	if (c == ' ')
		return true;
	if (c>='0' && c<='9')
		return true;
	return false;
}

void GetSearchEngineName(FILE *instream, char* name) {
	char c = fgetc(instream);
	while (IsNameChar(c)) {
		*(name++) = c;
		c = fgetc(instream);
	}
	*name = '\0';
	fscanf(instream, " ");
}

class EngineVec {
private:
	typedef std::vector<std::string> StringVec;
	StringVec m_set;
public:
	void Add(char *name) {m_set.push_back(std::string(name));}
	void Remove(char *name);
	bool Empty() const {return m_set.empty();}
};

void EngineVec::Remove(char *name) {
	std::string nameStr(name);
	for (StringVec::iterator i=m_set.begin(); i!=m_set.end(); ++i)
		if (!nameStr.compare(*i)) {
			m_set.erase(i);
			return;
		}
}

void GetEngineNames(FILE *instream, EngineVec &vec) {
	int numEngines = 0;
	fscanf(instream, "%d ", &numEngines);
	char engineName[100];
	for (int i=0; i<numEngines; ++i) {
		GetSearchEngineName(instream, engineName);
		vec.Add(engineName);
	}
}

void ProcessCase(FILE *instream, int caseNum) {
	EngineVec vec;
	GetEngineNames(instream, vec);

	int linesRemaining = 0;
	fscanf(instream, "%d ", &linesRemaining);
	EngineVec vecRemaining(vec);
	int numSwitches = 0;
	while (linesRemaining) {
		char engineName[100];
		GetSearchEngineName(instream, engineName);
		vecRemaining.Remove(engineName);
		if (vecRemaining.Empty()) {
			vecRemaining = vec;
			vecRemaining.Remove(engineName);
			++numSwitches;
		}
		linesRemaining --;
	}
	printf("Case #%d: %d\n", caseNum, numSwitches);
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 1;
	FILE *stream = fopen(argv[1], "r");
	if (!stream)
		return 1;

	int numCases;
	fscanf(stream, "%d ", &numCases);
	for (int i=0; i<numCases; ++i)
		ProcessCase(stream, i+1);

	return 0;
}


#ifndef ENGINEDB_H
#define ENGINEDB_H

#include <string>
#include <iostream>
using std::string;

class EngineDB{
public:
	EngineDB(unsigned int NumOfEngines);
	~EngineDB();
	void AddEngine(string EngineName);
	void Query(string query);
	unsigned int Switches(){ return RequiredSwitches; };

//private:
	void AreAllFlagsSet();
	void ResetFlags();
	unsigned int FindEngine(string name);

	unsigned int TotalEngines;
	unsigned int CurrEngines;
	string *Engines;
	unsigned int SetCount;
	bool *EngineFlags;
	unsigned int RequiredSwitches;
};

#endif
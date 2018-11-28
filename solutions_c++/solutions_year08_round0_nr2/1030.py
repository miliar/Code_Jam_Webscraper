#ifndef TRAIN_H
#define TRAIN_H

#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

vector<string> Split(const string& line, char delim);

class Train
{
public:
	void readFromFile(string filename);
	void countTrain(int index);
	void countAll();
protected:
private:
	int m_Cases;
	int *m_RoundTime;
	vector<vector<pair<int, int>>> m_AB;
	vector<vector<pair<int, int>>> m_BA;
	vector<pair<int, int>> m_Count;
};

bool earlier(pair<int, int> p1, pair<int, int> p2);

#endif
// A-small.cpp

#pragma once

#include <stdio.h>
#include <tchar.h>
#include <windows.h>
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

static bool RemoveItem(list<string>* itemList, string target)
{
	list<string>::iterator it = itemList->begin();
	while (itemList->end() != it) {
		if (!(*it).compare(target)) {
			itemList->remove(*it);
			return true;
		}
		it++;
	}
	return false;
}

static string SelectSerchEngine(list<string> serchEngineList, list<string> queryList)
{
	list<string> temp = serchEngineList;

	list<string>::iterator it = queryList.begin();
	while (queryList.end() != it) {
		RemoveItem(&temp, *it);
		if (1 == temp.size()) {
			return temp.back();
		}
		it++;
	}
	return "";
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifs;
	ofstream ofs;

	if (2 > argc) {
		return -1;
	}

	string fileName = argv[1];
//	string fileName = "C:\\A-small\\A-small-attempt5.in";
	ifs.open(fileName.c_str(), ios::in);
	if (ifs.fail()) {
		printf("ifs.open() err=%d\n", ::GetLastError());
		return -1;
	}

	ofs.open("c:\\A-small\\A-small-output.txt", ofs.out);
	if (!ofs.is_open()) {
		printf("ofs.open() err=%d\n", ::GetLastError());
		return -1;
	}

	char input[100+1] = {0};
	while (!ifs.eof()) {
		ifs.getline(input, sizeof(input));
		int N = atoi(input);

		for (int i=0; i<N; i++) {
			ifs.getline(input, sizeof(input));
			int S = atoi(input);

			list<string> serchEngineList;
			for (int j=0; j<S; j++) {
				ifs.getline(input, sizeof(input));
				serchEngineList.push_back(input);
			}

			ifs.getline(input, sizeof(input));
			int Q = atoi(input);

			list<string> queryList;
			for (int k=0; k<Q; k++) {
				ifs.getline(input, sizeof(input));
				queryList.push_back(input);
			}

			int Y = 0;
			list<string>::iterator it = queryList.begin();
			string serchEngine = SelectSerchEngine(serchEngineList, queryList);
			while (queryList.end() != it) {
				if (!it->compare(serchEngine)) {
					serchEngine = SelectSerchEngine(serchEngineList, queryList);
					Y++;
				}
				it++;
				queryList.pop_front();
			}

			printf("Case #%d: %d\n", i+1, Y);

			char output[256] = {0};
			_snprintf_s(output, _TRUNCATE, "Case #%d: %d\n", i+1, Y);
			ofs.write(output, strlen(output));
		}
	}

	ifs.close();
	ofs.close();

	getc(stdin);
	return 0;
}


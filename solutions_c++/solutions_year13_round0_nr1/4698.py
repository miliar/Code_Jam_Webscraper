// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std; 

class tic_tacc_toe;

class testcase{
public:
	void parse_testcase(){
		string line;
		for(int i = 0; i < 4; ++i){
			getline(cin,line);
			_data.push_back(line);
		}
	}

	string solve() const;
	bool is_full() const;
	bool check_result(map<char, int>& char_count, string& res) const;
private:
	vector<string>      _data;
};

class tic_tac_toe {
public:
	void parse_testcase();

	void solve() const; 

private:
	vector<testcase> _tests;
};

bool testcase::is_full() const {
	for(int i = 0; i < 4; ++i){
		for(int j = 0; j < 4; ++j){
			if(_data[i][j] == '.') return false;
		}
	}

	return true;
}

bool testcase::check_result(map<char, int>& char_count, string& res) const {
	if(char_count['X'] + char_count['T'] == 4){
		res = "X won";
		return true;
	}
	else if(char_count['O'] + char_count['T'] == 4){
		res = "O won";
		return  true;
	}
	else 
		return false;
}

string  testcase::solve()const{
	map<char, int> char_count;
	string res;
	for(int i = 0; i < 4; ++i){
		char_count['X'] = 0;
		char_count['O'] = 0;
		char_count['T'] = 0;
		char_count['.'] = 0;
		for(int j = 0; j < 4; ++j){
			++char_count[_data[i][j]];
		}
		if(check_result(char_count, res))
			return res;
	}

	for(int i = 0; i < 4; ++i){
		char_count['X'] = 0;
		char_count['O'] = 0;
		char_count['T'] = 0;
		char_count['.'] = 0;
		for(int j = 0; j < 4; ++j){
			++char_count[_data[j][i]];
		}
		if(check_result(char_count,  res))
			return res;
	}

	char_count['X'] = 0;
	char_count['O'] = 0;
	char_count['T'] = 0;
	char_count['.'] = 0;

	for(int i = 0; i < 4; ++i){
		++char_count[_data[i][i]];
	}
	if(check_result(char_count, res))
		return res;

	char_count['X'] = 0;
	char_count['O'] = 0;
	char_count['T'] = 0;
	char_count['.'] = 0;
	for(int i = 0; i < 4; ++i){
		++char_count[_data[i][3 - i]];
	}
	if(check_result(char_count, res))
		return res;

	if(!is_full())
		return "Game has not completed";
	else
		return "Draw";
}

void tic_tac_toe::parse_testcase(){
	string line;
	getline(cin, line);
	istringstream is(line);
	int tc;
	is >> tc;

	for(int i = 0; i < tc; ++i){
		testcase t;
		t.parse_testcase();
		_tests.push_back(t);
		getline(cin, line);
	}
	return;
}

void tic_tac_toe::solve() const{
	int total = _tests.size();

	for(int i = 0; i <  total; ++i){
		cout << "Case #" << i + 1 << ": " << _tests[i].solve() << endl;
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	tic_tac_toe game;
	game.parse_testcase();
	game.solve();

	return 0;
}
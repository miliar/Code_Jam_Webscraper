#include <vector>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <string>
#include <iostream>
#include <set>
using namespace std;

typedef pair<char, char> PChar;
typedef set<PChar> SPair;
typedef map<PChar, char> MPairChar;
typedef vector<char> VChar;
typedef vector<int> VInt;

PChar my_pair(char a, char b) {
	a = toupper(a);
	b = toupper(b);
	if(a > b)
		swap(a, b);
	return PChar(a, b);
}

struct Buffer {
	VChar chars;
	VInt counts;
	Buffer() {
		clear();
	}
	void push_back(char c) {
		chars.push_back(c);
		counts[(unsigned char)c]++;
	}
	void pop_back() {
		char c = chars.back();
		chars.pop_back();
		counts[(unsigned char)c]--;
	}
	int get_count(char c) {
		return counts[(unsigned char)c];
	}
	void clear() {
		chars.clear();
		counts.assign(256, 0);
	}
};

void process(string &input, MPairChar & combine, SPair & cancel, VChar &result)
{
	Buffer buf;
	for(string::iterator it = input.begin(); it != input.end(); it++) {
		bool combined = false;
		if(!buf.chars.empty()) {
			MPairChar::iterator entry = combine.find(my_pair(buf.chars.back(), *it));
			if(entry != combine.end()) {
				buf.pop_back();
				buf.push_back(entry->second);
				combined = true;
			}
		}		
		if(combined) continue;
		
		bool canceled = false;
		for(VChar::iterator old = buf.chars.begin(); old != buf.chars.end(); old++)
			if(cancel.find(my_pair(*it, *old)) != cancel.end()) {
				canceled = true;
				break;
			}
		if(canceled) {
			buf.clear();
			continue;
		}

		buf.push_back(*it);
	}
	result = buf.chars;
}

void solve(int case_no)
{
	MPairChar combine;
	SPair cancel;
	VChar result;
	string input;

	// read the input
	int combine_count;
	cin >> combine_count;
	for(int i = 0; i < combine_count; i++) {
		string str;
		cin >> str;
		combine[my_pair(str[0], str[1])] = str[2];
	}

	int cancel_count;
	cin >> cancel_count;
	for(int i = 0; i < cancel_count; i++) {
		string str;
		cin >> str;
		cancel.insert(my_pair(str[0], str[1]));
	}

	int length;
	cin >> length;
	cin >> input;
	
	// solve
	process(input, combine, cancel, result);

	// format the result
	cout << "Case #" << case_no << ": [";
	for(VChar::iterator it = result.begin(); it != result.end(); it++) {
		if(it != result.begin())
			cout << ", ";
		cout << *it;
	}
	cout << "]" << endl;
}

int main() {
	int case_count;
	cin >> case_count;
	for(int i = 1; i <= case_count; i++)
		solve(i);
	return 0;
}

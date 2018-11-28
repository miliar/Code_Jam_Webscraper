// Magicka.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Magic {
	char src[2];
	char dst; // '\0' clears the list
};

int main(int argc, char* argv[])
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		vector<string> magics;

		int num = 0;
		cin >> num;
		for (int j = 0; j < num; j++) {
			string magic;
			cin >> magic;
			magics.push_back(magic);
		}
		cin >> num;
		for (int j = 0; j < num; j++) {
			string magic;
			cin >> magic;
			magics.push_back(magic);
		}

		string elems, result;
		cin >> num;
		cin >> elems;

		for (string::const_iterator e = elems.begin(); e != elems.end(); ++e) {
			bool addElem = true;
			if (result.length() > 0) {
				string::iterator re = result.end()-1;
				for (vector<string>::iterator m = magics.begin(); m != magics.end(); ++m) {
					if (m->length() > 2) {
						if (*e == (*m)[0] && *re == (*m)[1] || *e == (*m)[1] && *re == (*m)[0]) {
							*re = (*m)[2]; // combine
							addElem = false;
							break;
						}
					}
					else if (*e == (*m)[0] && string::npos != result.find((*m)[1]) || *e == (*m)[1] && string::npos != result.find((*m)[0])) {
						result.clear(); // clear
						addElem = false;
						break;
					}
				}
			}
			if (addElem)
				result += *e;
		}

		cout << "Case #" << i+1 << ": [";
		for (string::const_iterator e = result.begin(); e != result.end(); ++e) {
			cout << *e;
			if (e != result.end()-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}


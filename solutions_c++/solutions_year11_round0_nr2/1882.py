#include <string>
#include <vector>
#include <iostream>

using namespace std;

#define MAX_C 100
#define MAX_D 100
#define MAX_N 100

vector<string> c;
vector<string> q;
string base_elements;

string combine(string elements) {
	int last = elements.size() - 1;
	
	for (int i = 0; i < c.size(); i++) {
		if (	(elements[last - 1] == c[i][0] && elements[last] == c[i][1])
			||	(elements[last] == c[i][0] && elements[last - 1] == c[i][1])) {
			elements.erase(last - 1, 2);
			elements += c[i][2];
			break;
		}
	}
	
	return elements;
}

string oppose(string elements) {
	int last = elements.size() - 1;
	
	for (int i = 0; i < q.size(); i++)
		for (int j = 0; j < elements.size() - 1; j++)
			if (	(elements[j] == q[i][0] && elements[last] == q[i][1])
				||	(elements[last] == q[i][0] && elements[j] == q[i][1]))
				return "";
	
	return elements;
}

int main(void) {
	int tests; string tmp;
	
	cin >> tests;
	for (int current_test = 0; current_test < tests; current_test++) {
		int count;
		
		base_elements.clear();
		c.clear();
		q.clear();
		
		cin >> count;
		while (count--) {
			cin >> tmp;
			c.push_back(tmp);
		}
		cin >> count;
		while (count--) {
			cin >> tmp;
			q.push_back(tmp);
		}
		
		char element;
		cin >> count;
		while (count--) {
			cin >> element;
			base_elements += element;
			tmp = combine(base_elements);
			while (tmp != base_elements) base_elements = tmp;
			base_elements = oppose(base_elements);
		}
		
		cout << "Case #" << current_test + 1 << ": ";
		cout << "[";
		for (int i = 0; i + 1 < base_elements.size(); i++) {
			cout << base_elements[i] << ", ";
		}
		if (base_elements.size() != 0)
			cout << base_elements[base_elements.size() - 1];
		
		cout << "]\n";
	}
	
	return 0;
}

#include <iostream>
#include <string>
#include <vector>


using namespace std;


//
// Class for elements that combine
//

class combine {
	char elem1;
	char elem2;
	char result;
public:
	combine(const string& s);
	~combine();
	bool checkCombine(string& s);
};

combine::combine(const string& s)
{
	elem1  = s[0];
	elem2  = s[1];
	result = s[2];
}

combine::~combine()
{
	// no special actions needed
}

bool combine::checkCombine(string& s)
{
	int l = s.length();
	if (((s[l - 2] == elem1) && (s[l - 1] == elem2)) ||
		((s[l - 2] == elem2) && (s[l - 1] == elem1)))
	{
		s = s.erase(l - 2);
		s = s.append(1, result);
		return true;
	}
	else
		return false;
}


//
// Class for elements that oppose
//

class oppose {
	char elem1;
	char elem2;
public:
	oppose(const string& s);
	~oppose();
	bool checkOppose(string& s);
};

oppose::oppose(const string& s)
{
	elem1 = s[0];
	elem2 = s[1];
}

oppose::~oppose()
{
	// no special actions needed
}

bool oppose::checkOppose(string& s)
{
	if ((s.find(elem1) != string::npos) && (s.find(elem2) != string::npos)) {
		s.clear();
		return true;
	}
	else
		return false;
}


//
// Main Function
//

int main()
{
	// Obtain the number of test cases
	int T;
	cin >> T;
	
	// Handle each test case
	for (int i = 0; i < T; i++) {
		
		// Initialize definition lists for combining elements & opposed elements
		vector<combine> combDef;
		vector<oppose> oppDef;
		
		// Obtain the definitions for combining elements
		int C;
		cin >> C;
		for (int j = 0; j < C; j++) {
			string s;
			cin >> s;
			combDef.push_back(combine(s));
		}
		
		// Obtain the definitions for opposing elements
		int D;
		cin >> D;
		for (int j = 0; j < D; j++) {
			string s;
			cin >> s;
			oppDef.push_back(oppose(s));
		}
		
		// Obtain the element invocation list
		int N;
		cin >> N;
		string s;
		cin >> s;
		
		// Handle the invocation of each element
		string current;
		for (int j = 0; j < N; j++) {
			current.append(1, s[j]);
			
			// Check for any element combinations
			bool found = false;
			int num = combDef.size();
			if (num > 0) {
				int k = 0;
				do {
					found = combDef[k].checkCombine(current);
					k++;
				} while ((!found) && (k < num));
			}
			
			// Check for any opposing elements
			if (!found) {
				num = oppDef.size();
				if (num > 0) {
					int k = 0;
					do {
						found = oppDef[k].checkOppose(current);
						k++;
					} while ((!found) && (k < num));
				}
			}
			
		}
		
		// List the elements at the end of the invocation sequence
		cout << "Case #" << i + 1 << ": [";
		int l = current.length();
		for (int j = 0; j < l; j++) {
			if (j > 0)
				cout << ", ";
			cout << current[j];
		}
		cout << "]" << endl;
		
	}
	
	return 0;
}

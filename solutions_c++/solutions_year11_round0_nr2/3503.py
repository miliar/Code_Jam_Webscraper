#include <iostream>

#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>

#define FALSE 0
#define TRUE 1

using namespace std;

bool combine(char a, char b, vector<string> vec, char *erg) {
	for (int i = 0; i<vec.size(); i++)
		if ((vec[i][0] == a && vec[i][1] == b) || (vec[i][0] == b && vec[i][1] == a)) {
			*erg = (vec[i])[2];
			return TRUE;
		}
	return FALSE;
}

bool areOpposed(char a, string b, vector<string> vec) {
	for (int i = 0; i<vec.size(); i++)
		if ((vec[i][0] == a && b.find(vec[i][1]) != string::npos) || (b.find(vec[i][0]) != string::npos && vec[i][1] == a))
			return TRUE;
	return FALSE;
}

int main (int argc, char * const argv[]) {
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int cur_case=1; cur_case<=T; cur_case++) {
		int C;
		vector<string> a;
		cin >> C;
		for (int i=0; i<C; i++) {
			string buf;
			cin >> buf;
			a.push_back(buf);
		}
		int D;
		vector<string> b;
		cin >> D;
		for (int i=0; i<D; i++) {
			string buf;
			cin >> buf;
			b.push_back(buf);
		}
		int N;
	    string c;
		cin >> N >> c;
		string result = "[";
		char lastChar;
		
		for (int i=0; i<N; i++) {
			char buf;
			if (i == 0) {
				result.push_back(c[i]);
				result.append(", ");
				lastChar = c[i];
			} else if (combine(c[i],lastChar,a,&buf)) {
				result.erase(result.end()-3,result.end());
				result.push_back(buf);
				result.append(", ");
				lastChar = buf;
			} else if (areOpposed(c[i],result,b)) {
				result = "[";
				lastChar = '0';
			}
			else {
				result.push_back(c[i]);
				result.append(", ");
				lastChar = c[i];
			}
		}
		
		if (result.length() > 2) result.erase(result.end()-2,result.end());
		result.append("]");
		cout << "Case #" << cur_case << ": " << result << endl;
	}
	return 0;
}

#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPP(i,m,n) for (int i = m; i < m+n; i++)
#define REPR(i,a,b) for (int i = a; i <= b; i++)

#define foreach(it,type) for (typeof(type.begin()) it = type.begin(); it != type.end(); it++)

#define MAX(n,m) (((n) > (m)) ? (n) : (m))
#define MIN(n,m) (((n) < (m)) ? (n) : (m))

typedef vector<int> vi;

int main(int argc, char* argv[]) {
  ifstream fin (argv[1]);

  int M;
  fin >> M;

	REP(c,M) {
		int C,D,N;
		map<string, string> mergemap;
		set<string> badset;

		fin >> C;
		REP(i,C) {
			string str;
			fin >> str;
			string first = str.substr(0,2);
			mergemap[first] = string() + str[2];
			mergemap[string() + first[1] + first[0]] = string() + str[2];
		}

		fin >> D;
		REP(i,D) {
			string str;
			fin >> str;

			badset.insert(str);
			badset.insert(string() + str[1] + str[0]);
		}

		fin >> N;
		string input;
		fin >> input;

		string result = "";

		REP(i,input.length()) {
			char ch = input[i];
			result += ch;

			if (result.length() >= 2) {
				string end = result.substr(result.length() - 2);
				if (mergemap.find(end) != mergemap.end()) {
					result = result.substr(0, result.length() - 2) + mergemap[end];
				}
			}

			REP(j,result.length() - 1) {
				string pair = string() + result[j] + result[result.length() - 1];
				if (badset.find(pair) != badset.end()) {
					result = "";
					break;
				}
			}
		}

		cout << "Case #" << c+1 << ": [";
		if (result != "") {
			cout << result[0];
		}
		int len = result.length();
		REPR(s,1,len-1) {
			cout << ", " << result[s];
		}
		cout << "]" << endl;
	}

  return 0;
}

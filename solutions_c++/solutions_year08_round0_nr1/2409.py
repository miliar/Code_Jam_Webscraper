#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main() {
	int n;
	cin >> n;
	for(int caso = 1; caso <= n; caso++) {
		int s, q;
		string line;
		cin >> s;
		getline(cin, line);
		vector<string> server(s);
		for(int i = 0; i < s; i++)
			getline(cin, server[i]);
		
		cin >> q;
		getline(cin, line);
		vector<string> questions(q);
		for(int i = 0; i < q; i++)
			getline(cin, questions[i]);
		
		set<string> temp(server.begin(), server.end());
		
		int i = 0;
		int res = 0;
		while(i < questions.size()) {
			if(temp.find(questions[i]) != temp.end())
				temp.erase(questions[i]);
			
			if(temp.empty()) {
				temp = set<string>(questions.begin(), questions.end());
				temp.erase(questions[i]);
				res++;
			}
			
			i++;
		}
		cout << "Case #" << caso << ": " << res << endl;
	}
	
	return 0;
}

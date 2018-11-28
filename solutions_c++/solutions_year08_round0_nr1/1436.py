#include <iostream>
#include <string>
#include <vector>

using namespace std;

int findStr(vector<string> qs, string eng, int pos)
{
	int i = pos;
	for(; i < qs.size(); ++i) {
		if(qs[i] == eng) break;
	}
	return i;
}

string pickLast(vector<string> qs, vector<string> engs, int pos)
{
	vector<bool> cant;
	for(int i = 0; i < engs.size(); ++i) cant.push_back(false);

	for(int i = pos; i < qs.size(); ++i) {
		int howMany = 0, who = 0;
		for(int j = 0; j < cant.size(); ++j) {
			if(!cant[j]) {
				++howMany;
				who = j;
			}
		}
		if(howMany == 1) return engs[who];

		for(int j = 0; j < engs.size(); ++j) {
			if(qs[i] == engs[j]) cant[j] = true;
		}
	}

	return "noneed";
}

int main()
{
	int cases;
	cin >> cases;
	for(int count = 0; count < cases; ++count) {
		int eng;
		cin >> eng;
		cin.ignore();
		vector<string> engs;
		for(int i = 0; i < eng; ++i) {
			string aux;
			getline(cin, aux);
			engs.push_back(aux);
		}
		int q;
		cin >> q;
		cin.ignore();
		vector<string> qs;
		for(int i = 0; i < q; ++i) {
			string aux;
			getline(cin, aux);
			qs.push_back(aux);
		}
		
		int i = 0;
		int change = 0;
		while(1) {
			string engine = pickLast(qs, engs, i);
			if(engine == "noneed") break;
			i = findStr(qs, engine, i);
			if(i == qs.size()) break;
			++change;
			// cout << i << " ";
			// cout << engine << endl;
		}

		cout << "Case #" << count+1 << ": " << change << endl;
	}
}





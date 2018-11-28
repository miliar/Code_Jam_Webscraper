#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cassert>
#include<fstream>

using namespace std;

vector<string> language[512];

int main()
{
	ifstream myin("A-large.in");
	ofstream out("A-large.out");
    istream &in = myin;
	int L,D,N;
	in >> L >> D >> N;
	
	vector<string> words(D);
	for(int i = 0 ; i < D ; ++i) {
		in >> words[i];
	}
	string kase;
	for(int i = 0 ; i < N ; ++i) {
		in >> kase;
		string temp = "";
		bool start = false;
		for(int j = 0 ; j < kase.size() ; ++j) {
			if(kase[j] == '(') {
				start = true;
				temp = "";
			}
			if(kase[j] == ')') {
				language[i].push_back(temp);
				temp = "";
				start = false;
			}
			if(isalpha(kase[j]) && start) {
				temp += kase[j];
			}
			if(isalpha(kase[j]) && !start) {
				string sp = "";
				sp += kase[j];
				language[i].push_back(sp);
			}
		}
		assert(language[i].size() == L);
	}
	
	for(int i = 0 ; i < N ; ++i) {
		int ans = 0;
		for(int j = 0 ; j < D ; ++j) {
			int ok = 0;
			for(int k = 0 ; k < L ; ++k) {
				if(find(language[i][k].begin(),language[i][k].end(),words[j][k]) != language[i][k].end())
					ok ++;
			}
			if(ok == L) ans++;
		}
		out << "Case #" << (i + 1) << ": " << ans << endl;
	}
	
	return 0;
}
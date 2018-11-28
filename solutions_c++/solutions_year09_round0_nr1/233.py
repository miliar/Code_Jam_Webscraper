#include <iostream>
#include <string>
using namespace std;

const int MAXD = 5000;

string dict[MAXD];
int N, L, D;

string getRange(string p, int &ip){
	if (p[ip] == '('){
		string res = "";
		for(ip++; p[ip] != ')'; ip++)
			res.push_back(p[ip]);
		ip++;
		return res;
	}
	else
		return p.substr(ip++, 1);
}

inline bool match(string p, string w){
	int ip = 0;
	for(int i=0; i<L; i++){
		string range = getRange(p, ip);
		bool good = false;
		for(int j=0; j<range.size(); j++)
			if (w[i] == range[j])
				good = true;
		if (!good)
			return false;
	}
	return true;
}

int main(int argc, char* args[]){
	if (argc < 2){
		cout << "lack of args" << endl;
		return 0;
	}
	freopen(args[1], "r", stdin);
	freopen(args[2], "w", stdout);
	cin >> L >> D >> N;
	for(int i=0; i<D; i++)
		cin >> dict[i];
	for(int c=0; c<N; c++){
		int cnt = 0;
		string p;
		cin >> p;
		for(int i=0; i<D; i++)
			if (match(p, dict[i]))
				cnt++;
		printf("Case #%d: %d\n", c+1, cnt);
	}
}


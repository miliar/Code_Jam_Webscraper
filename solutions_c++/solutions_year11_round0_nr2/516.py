#include <iostream>
#include <string>
#include <cstring>
using namespace std;
const int OMEGA = 27;
int com[OMEGA][OMEGA], opp[OMEGA][OMEGA];

bool checkCom(string &str, char ch){
	if (str.size() > 0 && com[str[str.size() - 1] - 'A'][ch - 'A'] != -1){
		str[str.size() - 1] = com[str[str.size() - 1] - 'A'][ch - 'A'] + 'A';
		return true;
	}
	return false;
}

bool checkOpp(string &str, char ch){
	for (int i = 0; i < str.size(); ++i){
		if (opp[str[i] - 'A'][ch - 'A'] != -1){
			str = "";
			return true;
		}	
	}
	return false;
}

int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int c, d;
		memset(com, -1, sizeof(com));
		memset(opp, -1, sizeof(opp));
		cin >> c;
		for (int i = 0; i < c; ++i){
			string str;
			cin >> str;
			com[str[0] - 'A'][str[1] - 'A'] = com[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
		}
		cin >> d;
		for (int i = 0; i < d; ++i){
			string str;
			cin >> str;
			opp[str[0] - 'A'][str[1] - 'A'] = opp[str[1] - 'A'][str[0] - 'A'] = 0;
		}
		int n;
		string seq, res;
		cin >> n >> seq;
		for (int i = 0; i < n; ++i){
			if (!checkCom(res, seq[i])){
				if (!checkOpp(res, seq[i])){
					res = res + seq[i];
				}
			}
		}
		string formatRes = "[";
		for (int i = 0; i < res.size(); ++i){
			formatRes = formatRes + res[i] + ", ";
		}
		formatRes = formatRes.substr(0, formatRes.size() - 2) + "]";
		printf("Case #%d: %s\n",tt + 1, formatRes.c_str());
	}
	return 0;
}
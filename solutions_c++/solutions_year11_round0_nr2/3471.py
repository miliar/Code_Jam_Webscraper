#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int Combine[27][27];
int Oppose[27][27];
bool checkCom(string & res, char p){
	if (res.size() > 0 && Combine[res[res.size() - 1] - 'A'][p - 'A'] != -1){
		res[res.size() - 1] = Combine[res[res.size() - 1] - 'A'][p - 'A'] + 'A';
		return true;
	}
	return false;
}

bool checkOpp(string & res, char p){
	for (int i = 0; i < res.size(); ++i){
		if (Oppose[res[i] - 'A'][p - 'A'] != -1){
			res = "";
			return true;
		}
	}
	return false;
}

int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int C, D, N;
		string str;
		memset(Combine, -1, sizeof(Combine));
		memset(Oppose, -1, sizeof(Combine));
		cin >> C;
		for (int i = 0; i < C; ++i){
			cin >> str;
			Combine[str[0] - 'A'][str[1] - 'A'] = Combine[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
		}
		cin >> D;
		for (int i = 0; i < D; ++i){
			cin >> str;
			Oppose[str[0] - 'A'][str[1] - 'A'] = Oppose[str[1] - 'A'][str[0] - 'A'] = 1;
		}
		cin >> N;
		string final;
		cin >> final;
		
		string res = final.substr(0, 1);
		for (int i = 1; i < final.length(); ++i){
			if (!checkCom(res, final[i])){
				if(!checkOpp(res, final[i])){
					res = res + final[i];
				}
			}
		}
		
		cout << "Case #" << tt + 1 << ": [";
		for (int i = 0; i < res.length() - 1 && res.length() > 0; ++i){
			cout << res[i] << ", ";
		}
		if (res.length() > 0){
			cout << res[res.length() - 1];
		}
		cout << "]" << endl;
	}
	return 0;
}
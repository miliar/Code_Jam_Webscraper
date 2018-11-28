//slow solution

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, M;

bool LineUp(string &a, string &b, char c, int len) {
	for (int i = 0; i < len; i++) {
		bool x = (a[i] == c);
		bool y = (b[i] == c);
		if (x != y) return false;
	}
	return true;
}

bool Contains(string &a, char c, int len) {
	for (int i = 0; i < len; i++) {
		if (a[i] == c) return true;
	}
	return false;
}

string Solve(string &ord, vector<string> &dic) {
	int cost[100]; //cost to guess word i in dictionary
	bool cont[100][26]; //whether dic[i] contains ord[j]
	
	//set cont here
	for (int i = 0; i < N; i++) {
		for (int k = 0; k < 26; k++) {
			cont[i][k] = Contains(dic[i],ord[k],dic[i].size());
		}
	}
	
	for (int i = 0; i < N; i++) {
		cost[i] = 0;
		int diff[100]; //first letter at which each other word j differs from dic[i]
		for (int j = 0; j < N; j++) {
			diff[j] = 0;
			if (j == i || dic[i].size() != dic[j].size()) continue;
			//we have two different words of the same size
			int len = dic[i].size();
			int val = 0;
			for (int k = 0; k < 26; k++) {
				char c = ord[k];
				if (cont[i][k] != cont[j][k] || !LineUp(dic[i],dic[j],c,len)) {
					//we differ at this guess
					val = k+1;
					break;
				}
			}
			diff[j] = val;
		}
		//cout << dic[i] << endl;
		for (int k = 1; k <= 26; k++) {
			bool miss = false;
			for (int j = 0; j < N; j++) {
				if (j == i) continue;
				//look for diff[j] == k;
				if (diff[j] == k) {
					//we have to guess ord[k-1]
					if (!cont[i][k-1]) {
						miss = true;
						//cout << "diffing: " << dic[j] << " " << ord[k-1] << endl;
						
					}
				}
			}
			if (miss) cost[i]++;
		}
	}
	
	//find dic[i] with highest cost[i] (dictionary order)
	string res = dic[0];
	int best = cost[0];
	//cout << cost[0] << endl;
	for (int i = 1; i < N; i++) {
		//cout << cost[i] << endl;
		if (cost[i] > best) {
			res = dic[i];
			best = cost[i];
		}
	}
	
	return res;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cout << "Case #" << icase << ":";
		vector<string> dic, ord;
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			string str;
			cin >> str;
			dic.push_back(str);
		}
		for (int i = 0; i < M; i++) {
			string str;
			cin >> str;
			string res = Solve(str, dic);
			cout << " " << res;
		}
		cout << endl;
	}
	
	return 0;
}

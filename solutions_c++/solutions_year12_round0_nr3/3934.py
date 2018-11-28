#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>
#include <vector>
#include <algorithm>

using namespace std;

string inc(string num) {
	string temp = num;
	int carry = 1;
	for (int i = temp.length() - 1; i >= 0; i--) {
		if (((int)temp[i]-48) + carry <= 9) {
			temp[i] = (char)((int)temp[i]+carry);
			break;
		}
		else {
			temp[i] = '0';
			carry = 1;
		}
	}
	return temp;
}

/*
   -1 if num1 < num2
    0 if num1 = num2
	1 if num1 > num2
*/
int comp(string num1, string num2) {
	assert (num1.length() == num2.length());
	for (int i = 0; i < num1.length(); i++) {
		if (num1[i] < num2[i]) return -1;
		else if (num1[i] > num2[i]) return 1;
		else continue;
	}
	return 0;
}

string shift(string str) {
	string newStr = "";
	for (int i = 1; i < str.length(); i++) {
		newStr += str[i];
	}
	newStr += str[0];
	return newStr;
}

vector<string> genCombo(string str) {
	vector<string> ar;
	//ar.push_back(str);
	string curStr = str;
	for (int i = 1; i < str.length(); i++) {
		string temp = shift(curStr);
		curStr = temp;
		if (temp[0] == '0') continue;
		else ar.push_back(temp);
	}
	return ar;
}

/*void print(vector<string> ar, string pre) {
	for (int i = 0; i < ar.size(); i++) {
		cout << pre << ar[i] << endl;
	}
}*/

/*vector<string> remDup(vector<string> array) {
	vector<string> ans = array;
	for (int i = 0; i < ans.size() - 1; i++) {
		for (int j = i + 1; j < ans.size(); j++) {
			if (ans[i] == ans[j]) {
				ans.erase(ans.begin()+j);
				j--;
			}
		}
	}
	return ans;
}*/



int main() {
	ifstream fin ("b.in");
	ofstream fout ("b.out");
	
	int T;
	fin >> T;
	vector<string> array;
	for (int t = 0; t < T; t++) {
		string a, b;
		fin >> a >> b;
		//cout << comp(a, b) << endl;
		
		string curNum = a;
		int total = 0;
		while (true) {
			//cout << "CurNum: " << curNum << endl;
			vector<string> combo = genCombo(curNum);
			sort(combo.begin(), combo.end());
			combo.erase(unique(combo.begin(), combo.end()), combo.end());
			//print(combo, " - ");
			//cout << "PENIS" << endl;
			//combo = remDup(combo);
			for (int i = 0; i < combo.size(); i++) {
				if ((comp(curNum, combo[i]) == -1) && (comp(combo[i], b) != 1)) {
					total++;
					//cout << combo[i] << " is bigger than " << curNum << endl;
				}
			}
			if (curNum == b) break;
			curNum = inc(curNum);
		}
		fout << "Case #" << (t + 1) << ": " << total << endl;
		
	}
}
		
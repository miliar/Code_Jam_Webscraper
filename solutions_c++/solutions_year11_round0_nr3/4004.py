#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>

using namespace std;

string fromDecimalToRBinary(int num) {
	string str;
	while (num != 1) {
		str += char((num % 2) + '0');
		num = num / 2;
	}
	str += '1';
	return str;
}

string RbinaryAdd(string &sum, string &str) {
	string ans;
	if (sum.length() >= str.length()) {
		int i;
		for (i = 0; i < str.length(); i++) {
			if ((sum[i] == '1' && str[i] == '1') || 
				(sum[i] == '0' && str[i] == '0')) ans += '0';
			else ans += '1';
		}
		ans += sum.substr(i, sum.length() - i);
	} else {
		int i;
		for (i = 0; i < sum.length(); i++) {
			if ((sum[i] == '1' && str[i] == '1') || 
				(sum[i] == '0' && str[i] == '0')) ans += '0';
			else ans += '1';
		}
		ans += str.substr(i, str.length() - i);
	}
	
	return ans;
}

void reverseAndDePad(string &ans) {
	for (int i = 0; i < ans.length() / 2; i++) {
		char ch = ans[i];
		ans[i] = ans[ans.length() - i - 1]; 
		ans[ans.length() - i - 1] = ch;
	}
	
	int i;
	for (i = 0; ans[i] == '0'; i++);
	ans = ans.substr(i);
	if (ans.length() == 0) ans = "0";
}

bool sumComparison(priority_queue<int> pile1, priority_queue<int> pile2, map<int, string> &binaryMap) {
	string sumPile1 = "0", sumPile2 = "0";
	while (!pile1.empty()) {
		string str = binaryMap[pile1.top()];
		pile1.pop();
		sumPile1 = RbinaryAdd(sumPile1, str);
	}
	while (!pile2.empty()) {
		string str = binaryMap[pile2.top()];
		pile2.pop();
		sumPile2 = RbinaryAdd(sumPile2, str);
	}

	reverseAndDePad(sumPile1);
	reverseAndDePad(sumPile2);
	
	return sumPile1 == sumPile2;
}

int sum(priority_queue<int> &pq) {
	int sum = 0;
	while (!pq.empty()) {
		sum += pq.top();
		pq.pop();
	}
	return sum;
}

void permuteStock(int &maxSum, stack<int> candyStock, priority_queue<int> pile1, 
				  priority_queue<int> pile2, map<int, string> &binaryMap) {
	if (candyStock.empty()) {
		// Define base case...
		if (pile1.empty() || pile2.empty()) return;
		if (sumComparison(pile1, pile2, binaryMap) == true) {
		 	int maxPile = max(sum(pile1), sum(pile2));
		 	if (maxPile > maxSum) maxSum = maxPile;
		}
		return;
	}
	int elem = candyStock.top();
	priority_queue<int> temp = pile1;
	pile1.push(elem);
	candyStock.pop();
	permuteStock(maxSum, candyStock, pile1, pile2, binaryMap);
	
	pile2.push(elem);
	permuteStock(maxSum, candyStock, temp, pile2, binaryMap);
}

int main() {
	/* Input data file. */
	string filename;
	getline(cin, filename);
	ifstream inputFile;
	inputFile.open(filename.c_str(), ios::in);
	
	/* Output stored in gcjoutput.txt */
	ofstream outputFile;
	outputFile.open("gcjoutput.txt", ios::out);
	
	int T;
	inputFile >> T;
	for (int i = 0; i < T; i++) {
		int N;
		inputFile >> N;
		int x;
		stack<int> candyStock;
		map<int, string> binaryMap;
		for (int j = 0; j < N; j++) {
			inputFile >> x;
			candyStock.push(x);
			binaryMap.insert(make_pair(x, fromDecimalToRBinary(x)));
		}
		
		map<int , string>::iterator itr = binaryMap.begin();
		for (; itr != binaryMap.end(); itr++) {
			cout << itr->first << " " << itr->second << endl;
		}
		
		int maxSum = 0;
		priority_queue<int> pile1, pile2;
		permuteStock(maxSum, candyStock, pile1, pile2, binaryMap);
		
		if (maxSum == 0)
		outputFile << "Case #" << i + 1 << ": " << "NO" << endl;
		else
		outputFile << "Case #" << i + 1 << ": " << maxSum << endl;
		
		cout << "----------------" << endl;
		
	}
	
	/* Clearing file stream. */
	inputFile.close();
	outputFile.close();
	
	return 0;
}
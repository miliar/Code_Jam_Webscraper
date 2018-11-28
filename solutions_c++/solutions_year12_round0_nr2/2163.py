//============================================================================
// Name        : codejam_2012_q.cpp
// Author      : festony
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


static string process(int caseNum) {
	char buf[10240];
	string temp_str = "";
	string result = "";

	int N;	// total number of googlers
	int S;	// number of surprising scores
	int p;	// threshold

	cin >> N >> S >> p;

	vector<int> g;
	int temp;

	for(int i=0; i<N; i++) {
		cin >> temp;
		g.push_back(temp);
	}

	sort(g.begin(), g.end());

//	for(int i=0; i<N; i++) {
//		cout << g[i] << " ";
//	}
//	cout << endl;

	int threshold_total_with_surprising = p + ((p-2)>0 ? (p-2) : 0) * 2;
	int threshold_total_without_surprising = p + ((p-1)>0 ? (p-1) : 0) * 2;

	int i_with_s = N;
	int i_without_s = N;

	for(int i=0; i<N; i++) {
		if(i_with_s == N && g[i] >= threshold_total_with_surprising) {
			i_with_s = i;
		}
		if(i_without_s == N && g[i] >= threshold_total_without_surprising) {
			i_without_s = i;
		}
		if(i_with_s < N && i_without_s < N) {
			break;
		}
	}

	int n_with_s = N - i_with_s;
	int n_without_s = N - i_without_s;

	int extra_n = S;
	if(extra_n > (n_with_s - n_without_s)) {
		extra_n = n_with_s - n_without_s;
	}

	int r = n_without_s + extra_n;

	sprintf(buf, "Case #%d: %d\n", caseNum + 1, r);
	result.append(buf);
	return result;
}

int main() {
	int caseNum = 0;
	cin >> caseNum;
	cin.ignore(256, '\n');
	char buf[10240];

	string result = "";

	for (int i = 0; i < caseNum; i++) {
		result.append(process(i));
	}
	cout << result;

	return 0;
}



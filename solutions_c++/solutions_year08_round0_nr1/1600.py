#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
int N, Q, S;
string engines[100];
string keywords[1001];

bool isEngineName(string s)
{
	for (int i=0; i<S; i++)
	{
		if (s==engines[i])
			return true;
	}
	return false;
}

int main() {
	int minSwitchNum = 0;
	int i,j,k;
	int engineNum;
	int count[100];
	bool doubledEngine;
	string currentSet[100];
	string str;
	getline(cin, str);
	N = atoi(str.c_str());
	for (i=0; i<N; i++) {
		engineNum = 0;
		getline(cin, str);
		S = atoi(str.c_str());
		for (j=0; j<S; j++) {
			getline(cin, engines[j]);
			count[j] = 0;
		}
		getline(cin, str);
		Q = atoi(str.c_str());
		for (j=0; j<Q; j++) {
			getline(cin, keywords[j]);
		}

		minSwitchNum = 0;

		for (int j=0; j<Q; j++) {

			if (isEngineName(keywords[j])) {
				doubledEngine = false;
				for (k=0; k<engineNum; k++)
				{
					if (currentSet[k]==keywords[j])
					{
						doubledEngine = true;
						break;
					}
				}
				if (!doubledEngine)
				{
					currentSet[engineNum++] = keywords[j];
				}
				if (engineNum==S) {
					engineNum=1;
					currentSet[0] = keywords[j];
					minSwitchNum++;
				}
			}
		}
		cout << "Case #" << (i+1) <<": "<< minSwitchNum << endl;
	}
	return 0;
}
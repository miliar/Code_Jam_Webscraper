#include<iostream>
#include<fstream>
using namespace std;

int main() {
	ifstream cin("./input.txt");
	ofstream cout("./output.txt");

	int nCount;
	float P;
	cin >> nCount;
	
	for(int i=1;i<=nCount;++i) {
		int nKey;
		int nAll;
		float prob = 1;
		float prob1 = 1;
		float prob2 = 1;
		int n = 0;
		cin >> nKey >> nAll;
		for(int j=1;j<=nKey;++j) {
			cin >> P;
			prob *= P;
			if(j+1 == nKey) prob1 = prob;
			if(j+2 == nKey) prob2 = prob;
		}
		float ANS;
		int giveup   = nAll + 2;
		ANS = giveup;
		//cout << ANS<<" ";

		int keeptype = nAll - nKey + 1;
		int keeptypeE = keeptype + nAll + 1;
		float keeptypeA = prob * keeptype + (1-prob) * keeptypeE;
		if(keeptypeA < ANS) ANS = keeptypeA;

		//cout << keeptypeA<<" ";

		int  back1    = keeptype + 2;
		int  back1E   = back1 + nAll +1;
		float back1A  = prob1 * back1 + (1-prob1) * back1E;
		if(back1A < ANS) ANS = back1A;

		//cout << back1A<<" ";

		int back2    = keeptype + 4;
		int back2E   = back2 + nAll + 1;
		float back2A = prob2 * back2 + (1-prob2) * back2E;
		if(back2A < ANS) ANS = back2A;
		
		//cout << back2A<<" ";
		
		char a[10005];
		sprintf(a,"Case #%d: %.6f",i,ANS);
		cout <<a<<endl;
	}

	system("pause");
}

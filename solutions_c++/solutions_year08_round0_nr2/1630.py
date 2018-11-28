#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;


void tc(int cn) {
	int t, na, nb;
	vector<int> departA(1500,0);
	vector<int> arriveA(1500,0);
	vector<int> departB(1500,0);
	vector<int> arriveB(1500,0);
	cin>>t>>na>>nb;
	int h1,m1,h2,m2;

	for (int i=0;i<na;i++) { //Trains A->B
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		int d = h1*60+m1;
		int a = h2*60+m2+t;
		departA[d]++;
		arriveB[a]++;
	}

	for (int i=0;i<nb;i++) { //Trains B->A (Yay!copypaste)
		scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
		int d = h1*60+m1;
		int a = h2*60+m2+t;
		departB[d]++;
		arriveA[a]++;
	}

	int startA=0,startB=0;
	int atA=0,atB=0;
	for (int i=0;i<1500;i++) {
		atA += arriveA[i];
		atB += arriveB[i];
		if (atA < departA[i]) {
			startA += departA[i]-atA;
			atA = departA[i];
		}
		if (atB < departB[i]) {
			startB += departB[i]-atB;
			atB = departB[i];
		}
		atA -= departA[i];
		atB -= departB[i];
	}
	cout << "Case #"<<cn<<": "<<startA << " " << startB<<endl;
}
int main() {
	int n;
	cin>>n;
	for (int i=0;i<n;i++)
		tc(i+1);
}
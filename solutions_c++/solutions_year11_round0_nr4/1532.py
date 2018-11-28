

#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define mp make_pair()
#define SS stringstream

double fc[1010];
double dc[1010];

double getDerangementProb(int n){
	if(n <= 1)return 0;
	if(dc[n] > -0.5)return dc[n];
	double fac = 1;
	FOR(i,0,n)fac*=-1.0/(i+1);
	return dc[n] = getDerangementProb(n - 1) + fac;
}


double getExp(int n){
	if(n <= 1)return 0;
	if(fc[n] >= -0.5)return fc[n];
	double ret = 1.0;
	double fac = 1.0;
	double j = 1;
	FOR(i,1,n-1){
		ret+= fac*getExp(n-i)*getDerangementProb(n - i);		
		j++;
		fac*=1.0/j;
	}
	return fc[n] = ret/(1 - getDerangementProb(n));
	
}



int main(){
	int cases;
	FOR(i,0, 1010)fc[i] = dc[i] = -1;
	cin >> cases;
	FOR(caseNum, 0, cases){
		int n; 
		cin >> n;
		int samecount = 0;
		FOR(i,0,n){
			int tmp;
			cin>> tmp;
			if(tmp == i + 1)samecount++;
		}
		//cout << samecount << endl;
		//FOR(i,0,4)cout << getExp(i + 1) << endl;
		cout << "Case #"<< caseNum + 1 << ": " << getExp(n - samecount) << endl;//2.000000"
		
	}
	
}


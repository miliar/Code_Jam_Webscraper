#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;

long long gcd(long long a, long long b){
	if (a<b) return gcd(b,a);
	if (b==0) return a; 
	return gcd(b,a%b);
}





int main(){

	freopen("b_small.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	//cout << gcd(43152905+3559,gcd(26554817+3559,3559+26558405)) << endl;

	int cases,NN;
	cin >> cases;
	for (int casenum=1;casenum<=cases;casenum++){
		cin >> NN;
		//long num[5];
		vector<long long> num;
		bool rep=false;
		for (int i=0;i<NN;i++){
			bool rep = false;
			long long tmp;
			cin >> tmp;
			for (int j=0;j<num.size();j++) if (tmp==num[j]) rep=true;
			if (!rep) num.push_back(tmp);
		}
		long long x,m,n;
		int numsize = num.size();
		//cout << numsize << endl;
		sort(num.begin(),num.end());
		m = num[0];
		if (numsize==2) n = num[1] - m;
		else n = gcd(num[2]-num[1],num[1]-m);
		if (n>=m) cout << "Case #" << casenum << ": " << n-m << endl;
		else if (n==1 || m%n==0) cout << "Case #" << casenum << ": 0" << endl;
		else cout << "Case #" << casenum << ": " << n*((m/n)+1)-m << endl;
	}
	return 0;
}
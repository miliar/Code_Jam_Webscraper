#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

ifstream in("a.in");
//ofstream out("a.out");
FILE* out;
#define cin in


void solve(int test) {
	int a,b;
	cin>>a>>b;
	vector<double> v(a), d(a);
	for(int i = 0; i < a;i++) {
		cin>>v[i];
		d[i] = v[i] * (i>0 ? d[i-1] : 1.0);
	}
	
	double res;
	res = d[a-1]*(b-a+1) + (1-d[a-1]) * (b-a+1+b+1);
	res = min(res, b+2.0);
	for(int i = 1; i<a;i++) {
		double r = 	d[a-i-1]*(i+2+b-a) + (1-d[a-i-1]) * (i+2+b-a+b+1);
		res = min(res, r);
	}
	
	//cout << "Case #"<<test<<": "<<res<<endl;
	fprintf(out,"Case #%d: %.6lf\n", test,res);
}

int main() {
	out = fopen("a.out", "w");
	int t;
	cin>>t;
	for(int i = 0 ; i< t;i++) {
		solve(i+1);	
	}		
}
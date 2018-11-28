#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstring>
#include <numeric>
#include <utility>
using namespace std;

int main () {
	fstream filestr;
	ofstream outstr;
	int cases;
	
	int n,k,b,t;
	vector<int> p,v,x;
	int temp;
	filestr.open("/Users/HOOI/Downloads/B-small-attempt3.in");
	outstr.open("/Users/HOOI/Documents/XCode/CodeJam/OUTPUT.txt");
	filestr >> cases;
	for (int cs=1;cs<=cases;cs++){
		p.clear();
		v.clear();
		x.clear();
		filestr >> n >>k >> b >> t;
		cout << n << " " << k << " " << b << " " << t << endl;
		x.resize(n);
		cout << "p"<<endl;
		for (int i=0;i<n;i++){ filestr >> temp; p.push_back(temp); cout << p[i] << " ";}
		cout <<endl<< "v"<<endl;
		for (int i=0;i<n;i++){ filestr >> temp; v.push_back(temp); cout << v[i] << " ";}
		cout << endl;
		for (int i=0;i<n;i++){if ( (long long) p[i]+t*v[i]<b) {x[i]=-1; cout << "x["<<i<<"] is -1."<<endl;}}
		for (int i=0;i<n;i++){
			if (x[i]==-1) continue;
			
			x[i]=0;
			for (int j=0;j<n;j++){
				if (x[j]==-1 && p[j]>p[i]) x[i]++;}
			cout << "new value of x["<<i<<"] is "<<x[i]<<endl;
			
		}
		sort(x.begin(), x.end());
		int sum=0;
		for (int i=0;i<n;i++){
			if (k==0) break;
			if (x[i]==-1) continue;
			sum += x[i];
			k--;
		}
		
		if (k>0){
			outstr << "Case #"<<cs<<": "<< "IMPOSSIBLE"<<endl;
			cout << "Case #"<<cs<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{
			outstr << "Case #"<<cs<<": "<< sum<<endl;
			cout << "Case #"<<cs<<": "<<sum<<endl;
		}
	}
	filestr.close();
	outstr.close();
	return 0;
}
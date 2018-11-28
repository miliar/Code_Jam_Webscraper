#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
int strToInt(string str){
	int num;
	istringstream is(str);
	is >> num;
	return num;
}
string intToStr(int num){
	ostringstream os;
	os << num;
	return os.str();
}

int gcd(int a,int b){
	if(a<b){
		int tmp = a;
		a = b;
		b = tmp;
	}
	if(b==0)
		return a;
	int r = a%b;
	return gcd(b,r);
}

vector<int> ts,ds;

int main(){
	int C,N,t;
	int i,j,k;
	string ss;
	ifstream fin("B-small-attempt1.in");
	ofstream fout("B.out");
	getline(fin,ss);
	C = strToInt(ss);
	for(int c=1;c<=C;c++){
		ts.clear();
		ds.clear();
		getline(fin,ss);
		istringstream is(ss);
		is>>N;
		for(i=0;i<N;i++){
			is>>t;
			ts.push_back(t);
		}
		sort(ts.begin(),ts.end());
		for(i=1;i<N;i++){
			ds.push_back(ts[i]-ts[i-1]);
		}
		int gd1,gd2;
		gd1 = ds[0];
		for(i=1;i<N-1;i++){
			gd2 = ds[i];
			gd1 = gcd(gd1,gd2);
		}
		
		cout<<gd1<<endl;
		int re = ((ts[ts.size()-1]-1)/gd1+1)*gd1-ts[ts.size()-1];
		fout<<"Case #"<<c<<": "<<re<<endl;
	}
	return 0;
}
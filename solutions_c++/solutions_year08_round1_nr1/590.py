#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<cmath>

using namespace std;

int s2i(string s) { istringstream i(s); int x; i>>x; return x; }

bool absCompAsc(int &A, int &B){
	return A < B;
}

bool absCompDes(int &A, int &B){
	return A > B;
}

int main(){
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int i, j, k, l, n, t;
	long long res;
	string buf;
	vector<int > v1, v2;

	in >> t;
	for (i =0 ; i < t ; i++){
		in>>n;
		v1.clear();
		v2.clear();
		res = 0;
		for (j = 0 ; j < n ; j++){
			in >> buf;
			v1.push_back(s2i(buf));
		}
		for (j = 0 ; j < n ; j++){
			in >> buf;
			v2.push_back(s2i(buf));
		}
		sort(v1.begin(),v1.end(),absCompAsc);
		sort(v2.begin(),v2.end(),absCompDes);
		for (j = 0 ; j < n ; j++)
			res += (long long)v1[j]*v2[j];
		out << "Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}
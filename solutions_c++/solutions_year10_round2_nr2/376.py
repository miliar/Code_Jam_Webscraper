#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
	ifstream in("input");
	ofstream out("output");
	int cases;
	in >> cases;
	int N,K,T;
	long long B;
	
	for(int casenum = 1; casenum <= cases; casenum++){
		out << "Case #" << casenum << ": ";
		cout << "Case " << casenum << endl;
		in >> N >> K >> B >> T;
		vector<long long> pos;
		vector<int> v;
		int temp;
		for(int i = 0; i < N; i++){
			in >> temp;
			pos.push_back(temp);
		}
		for(int i = 0; i < N; i++){
			in >> temp;
			v.push_back(temp);
		}
		int pass = 0;
		int cnt = 0;
		int npass = 0;
		for(int i = N - 1; i >= 0; i--){
			long long dis = B - pos[i];
			double time = (double)dis / v[i];
			if(time <= (double)T){
			       pass++;
			       cnt += npass;
			}
			else npass++;
			if(pass >= K) break;
		}
		if(pass >= K) out << cnt << endl;
		else out << "IMPOSSIBLE" << endl;


	}
	return 0;
}

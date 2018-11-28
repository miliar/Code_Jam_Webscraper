//#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

ifstream cin("A-large.in");
ofstream cout("A.out");
int processString(string s){
	vector <int> vorange;
	vector <int> vblue;
	vector <int> seq;
	istringstream iss(s);
	int z;
	iss >> z;
	for(int j=0;j<z;j++){
		char c;
		int i;
		iss >> c;
		iss >> i;		
		if(c=='O'){
			vorange.push_back(i);
			seq.push_back(2*i);
		}
		else{
			vblue.push_back(2*i+1);
			seq.push_back(2*i+1);
		}
	}
	int lastopos =1, lastbpos=1, lastotime =0, lastbtime =0;
	
	for(int i=0;i<seq.size();i++){
		if(seq[i] & 1){
			int t1 = abs(seq[i]/2 - lastbpos);
			lastbpos = seq[i]/2;
			lastbtime = max(lastotime + 1,t1+lastbtime+1);
			
		}
		else{
			int t1 = abs(seq[i]/2 - lastopos);
			lastopos = seq[i]/2;
			lastotime = max(lastbtime + 1,t1+lastotime+1);
			
		}
	}	
	return max(lastotime,lastbtime);
}
int main(){
	int N;
	cin >> N;
	ws(cin);
	for(int i=0;i<N;i++){
		string s;
		getline(cin,s);
		int a = processString(s);
		//Case #1: 6
		cout << "Case #" << i+1 << ": " << a << endl;
	}
	return 0;
}
#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>

using namespace std;

#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) (EQ((a).real(),(b).real()) && EQ((a).imag(),(b).imag()))

typedef complex<double> P;
typedef long long ll;

const int MAX_SIZE = 10000;

int T;

int main(){

	ifstream ifs("input.txt");

	ifs >> T;
		ofstream ofs("output.txt");
	for(int i = 0; i < T; i++){
		int N;
		int C;
		int D;
		vector<string> cList;
		vector<string> dList;

		ifs >> C;
		for(int i = 0; i < C; i++){
			string s;
			ifs >> s;
			cList.push_back(s);
		}
		ifs >> D;
		for(int i = 0; i < D; i++){
			string s;
			ifs >> s;
			dList.push_back(s);
		}
		ifs >> N;
		string str;
		ifs >> str;
		
		string ss;
		for(int i = 0; i < N; i++){
			ss += str[i];
			// combine
			bool flag = false;
			for(int j = 0; (j < cList.size()) && (ss.size() != 0); j++){
				if(ss[ss.size()-1] == cList[j][0]){
					if(ss.size() >= 2 && ss[ss.size()-2] == cList[j][1]){
						ss = ss.substr(0,ss.size()-1);
						ss[ss.size()-1] = cList[j][2];
						flag = true;
						j = 0;
						break;
					}
				}
				else if(ss[ss.size()-1] == cList[j][1]){
					if(ss.size() >= 2 && ss[ss.size()-2] == cList[j][0]){
						ss = ss.substr(0,ss.size()-1);
						ss[ss.size()-1] = cList[j][2];
						flag = true;
						j = 0;
						break;
					}
				}
			}
			if(!flag){
			// opposed
			for(int j = 0; (j < dList.size()) && (ss.size() != 0); j++){
				if(ss[ss.size()-1] == dList[j][0]){
					for(int k = 0; k < ss.size()-1; k++){
						if(ss[k] == dList[j][1]){
							ss.clear();
//							ss = ss.substr(0,k);
							j = 0;
							flag = true;
							break;
						}
					}
					if(flag)
						break;
				}
				else if(ss[ss.size()-1] == dList[j][1]){
					for(int k = 0; k < ss.size()-1; k++){
						if(ss[k] == dList[j][0]){
							ss.clear();
//							ss = ss.substr(0,k);
							j = 0;
							flag = true;
							break;
						}
					}
					if(flag)
						break;
				}
			}
		}
		}

		if(ss.size() != 0){
			ofs << "Case #" << i+1 << ": [" << ss[0] << flush;
			for(int i = 1; i < ss.size(); i++){
				ofs << ", " << ss[i] << flush;
			}
			ofs << "]" << endl;
		}
		else{
			ofs << "Case #" << i+1 << ": []" << endl;
		}
	}
	
	//int x;
	//cin >> x;

	return 0;
}
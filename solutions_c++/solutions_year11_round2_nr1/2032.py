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

using namespace std;

int T;
int N;
vector<string> graph;


vector<double> calcOWP(vector<double> wp){
	vector<double> owp(N,0.0);
	for(int i = 0; i < N; i++){
		vector<int> check;
		for(int j = 0; j < N; j++){
			if(graph[i][j] == '1' || graph[i][j] == '0'){
				check.push_back(j);
			}
		}
		// ŒvŽZ
		double owpt = 0.0;
		for(int j = 0; j < check.size(); j++){
			double per = 0.0;
			int bunbo = 0;
			for(int k = 0; k < N; k++){
				if(k == check[j] || graph[check[j]][k] == '.' )
					continue;
				if(graph[check[j]][k] == '1'){
					per += 1.0;
					bunbo++;
				}
				else{
					bunbo++;
				}
			}
			per /= bunbo;
			owpt += per;
		}
		owpt/=check.size();
		owp.push_back(owpt);
	}
	return owp;
}

vector<double> solve(){
	vector<double> wp(N,0.0);
	for(int i = 0; i < N; i++){
		int win = 0;
		int game = 0;
		for(int j = 0; j < N; j++){
			if(graph[i][j] == '.')
				continue;
			else if(graph[i][j] == '1'){
				game++;
				win++;
			}
			else
				game++;
		}
		wp[i] = (double)win/game;
	}

	vector<double> owp(N,0.0);
	for(int i = 0; i < N; i++){
		vector<int> check;
		for(int j = 0; j < N; j++){
			if(graph[i][j] == '1' || graph[i][j] == '0'){
				check.push_back(j);
			}
		}
		// ŒvŽZ
		double owpt = 0.0;
		for(int j = 0; j < check.size(); j++){
			double per = 0.0;
			int bunbo = 0;
			for(int k = 0; k < N; k++){
				if(k == i || graph[check[j]][k] == '.' )
					continue;
				if(graph[check[j]][k] == '1'){
					per += 1.0;
					bunbo++;
				}
				else{
					bunbo++;
				}
			}
			per /= bunbo;
			owpt += per;
		}
		owpt/=check.size();
		owp[i]=(owpt);
	}

	vector<double> oowp(N,0.0);
	for(int i = 0; i < N; i++){
		vector<int> check;
		for(int j = 0; j < N; j++){
			if(graph[i][j] == '1' || graph[i][j] == '0'){
				check.push_back(j);
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= check.size();
		//oowp[i] = owp[

		//// ŒvŽZ
		//double owpt = 0.0;
		//for(int j = 0; j < check.size(); j++){


		//	//owpt += owp[check[j]];
		//	vector<int> check2;
		//	for(int k = 0; k < N; k++){
		//		if(graph[check[j]][k] == '.' || k == check[j]){
		//			continue;
		//		}
		//		else
		//			check2.push_back(k);
		//	}
		//	double iii = 0.0;
		//	// check2‚Ì’†g‚Ì‚Æ‚±‚ë‚É’Tõ‚ð‚©‚¯‚é
		//	for(int l = 0; l < check2.size(); l++){
		//		double per = 0.0;
		//		int bunbo = 0;
		//		for(int k = 0; k < N; k++){
		//			if(k == check2[l] || graph[check2[l]][k] == '.' )
		//				continue;
		//			if(graph[check2[l]][k] == '1'){
		//				per += 1.0;
		//				bunbo++;
		//			}
		//			else{
		//				bunbo++;
		//			}
		//		}
		//		per /= bunbo;
		//		iii += per;
		//	}
		//	iii /= check2.size();
		//	owpt += iii;
		//}
		//owpt/=check.size();
		//oowp[i]=(owpt);
	}

	vector<double> vec;
	for(int i = 0; i < N; i++){
		double d = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		vec.push_back(d);
	}
	return vec;
}

int main(){

	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	ifs >> T;
	for(int i = 0; i < T; i++){
		ifs >> N;
		string str;
		for(int j = 0; j < N; j++){
			ifs >> str;
			graph.push_back(str);
		}
		ofs << "Case #" << i+1 << ":" << endl;
		vector<double> v = solve();
		for(int j = 0; j < v.size(); j++){
			ofs << v[j] << endl;
		}

		graph.clear();
	}

	int x;
	cin >> x;
		
	return 0;
}
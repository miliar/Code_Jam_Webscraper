// codejam4.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	int winLose[100][100];
	int win[100], lose[100];
	double score[100], wp[100], owp[100], oowp[100];
	for(int t = 0; t < T; t++){
		int N;
		in >> N;
		for(int i = 0; i < N; i++){
			win[i] = lose[i] = 0;
			score[i] = 0;
			string str;
			in >> str;
			for(int j = 0; j < N; j++){
				if(str[j] == '1'){ 
					win[i]++;
					winLose[i][j] = 1;
				}
				else if(str[j] == '0'){
					lose[i]++;
					winLose[i][j] = -1;
				}
				else winLose[i][j] = 0;
			}
			wp[i] = win[i] / (double)(win[i] + lose[i]);
			owp[i] = 0;
			oowp[i] = 0;
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(winLose[i][j] == 1){
					owp[i] += win[j] / (double)(win[j] + lose[j] - 1);
				}
				else if(winLose[i][j] == -1){
					owp[i] += (win[j] - 1) / (double)(win[j] + lose[j] - 1);
				}
			}
			owp[i] /= (double)(win[i] + lose[i]);
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(winLose[i][j] != 0){
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= (double)(win[i] + lose[i]);
		}
		out << "Case #" << t + 1 << ":" << endl;
		for(int i = 0; i < N; i++){
			score[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			out << score[i] << endl;
		}
	}
	return 0;
}


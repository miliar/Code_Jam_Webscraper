// codejam2.cpp : 定义控制台应用程序的入口点。
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
	for(int t = 0; t < T; t++){
		int C, D, N;
		string combin[36], oppose[28], str;
		in >> C;
		for(int c = 0; c < C; c++)
			in >> combin[c];
		in >> D;
		for(int d = 0; d < D; d++)
			in >> oppose[d];
		in >> N >> str;
		bool finished = false;
		for(int i = 1; i < N; i++){
			finished = false;
			for(int j = 0; j < C; j++){
				if(str[i] == combin[j][0] && str[i - 1] == combin[j][1]
				|| str[i] == combin[j][1] && str[i - 1] == combin[j][0]){
					str[i] = combin[j][2];
					str[i-1] = '*';
					finished = true;
					break;
				}
			}
			if(finished)continue;
			for(int j = 0; j < D; j++){
				if(str[i] == oppose[j][0]){
					for(int k = 0; k < i; k++)
						if(str[k] == oppose[j][1]){
							for(int o = 0; o <= i; o++)str[o] = '*';
							finished = true;
							break;
						}
				}
				if(finished)break;
			}
			if(finished)continue;
			for(int j = 0; j < D; j++){
				if(str[i] == oppose[j][1]){
					for(int k = 0; k < i; k++)
						if(str[k] == oppose[j][0]){
							for(int o = 0; o <= i; o++)str[o] = '*';
							finished = true;
							break;
						}
				}
				if(finished)break;
			}
		}
		string answer = "";
		for(int j = 0; j < N; j++)
			if(str[j] != '*')answer += str[j];
		out << "Case #" << t + 1 << ": [";
		int test = answer.size() - 1;
		for(int j = 0; j < test; j++)
			out << answer[j] << ", ";
		if(answer.size() > 0)
			out << answer[answer.size() - 1];
		out << "]" << endl;
	}
	return 0;
}

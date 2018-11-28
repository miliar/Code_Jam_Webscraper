// codejam8.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

long dist[10000];
long total[10000];

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for(int t = 0; t < T; t++){
		long long L, speed, N, C;
		in >> L >> speed >> N >> C;
		for(int c = 0; c < C; c++){
			in >> dist[c];
			if(c == 0)total[c] = 0;
			else total[c] = dist[c - 1] + total[c-1];
		}
		for(int c = C; c < N; c++){
			dist[c] = dist[c - C];
			total[c] = dist[c - 1] + total[c-1];
		}
		long min = 1e11;
		if(L == 2){
			for(int i = 0; i < N; i++)
				for(int j = i + 1; j < N; j++){
					long time = total[i] * 2;
					if(time >= speed)time += dist[i];
					else if(time + dist[i] * 2 <= speed)time += dist[i] * 2;
					else{
						long first = (speed - time) / 2;
						long second = dist[i] - first;
						time += first * 2 + second;
					}
					time += (total[j] - total[i+1]) * 2;

					if(time >= speed)time += dist[j];
					else if(time + dist[j] * 2 <= speed)time += dist[j] * 2;
					else{
						long first = (speed - time) / 2;
						long second = dist[i] - first;
						time += first * 2 + second;
					}
					if(j < N - 1)time += (dist[N - 1] + total[N - 1] - total[j+1]) * 2;

					if(time < min){
						min = time;
						//out << i << " " << j << " " << min << endl;
					}
				}
			out << "Case #" << t + 1 << ": " << min << endl;
		}
		else if(L == 1){
			for(int i = 0; i < N; i++){
				long time = total[i] * 2;
				if(time >= speed)time += dist[i];
				else if(time + dist[i] * 2 <= speed)time += dist[i] * 2;
				else{
					long first = (speed - time) / 2;
					long second = dist[i] - first;
					time += first * 2 + second;
				}
				if(i < N - 1)time += (dist[N - 1] + total[N - 1] - total[i+1]) * 2;

				if(time < min){
					min = time;
					//out << i << " " << min << endl;
				}
			}
			out << "Case #" << t + 1 << ": " << min << endl;
		}
		else{
			out << "Case #" << t + 1 << ": " << (dist[N-1]+total[N-1])*2 << endl;
		}
	}
	return 0;
}


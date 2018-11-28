#include <bitset>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <deque>
#include <vector>
#include <list>
#include <queue>
#include <string>
using namespace std;
ofstream fout("A-large.out");
ifstream fin("A-large.in");

int main(){
	int T;
	fin >> T;
	for(int s=0;s<T;s++){
		fout << "Case #"<< s+1 << ": ";
		long long X, S, R, t, N;
		fin >> X >> S >> R >> t >> N;
		pair<long long, long long> wway[2 * N + 1];
		//pair<long long, long long> wway2[2 * N + 1];
		long long last = 0;
		for(int i=0;i<N;i++){
			long long b, e, a;
			fin >> b >> e >> a;
			wway[2 * i] = make_pair(0, b - last);
			//wway2[2 * i] = make_pair(0, b - last);
			wway[2 * i + 1] = make_pair(a, e - b);
			//wway2[i* 2 + 1] = make_pair(a, e - b);
			last = e;
		}
		wway[2 * N] = make_pair(0, X - last);
		//wway2[2 * N] = wway[2*N].first;
		sort(wway, wway+2*N + 1);
		
		double run = t;
		double total = 0;
		for(int i=0;i<2*N+1;i++){
			//cout << run << endl;
			if(run <= 0){
				total += ((double)wway[i].second) / (S + wway[i].first);
				continue;
			}
			if(run > ((double)wway[i].second) / (R + wway[i].first)){
				
				//total -= ((double)wway[i].first.second) / (S + wway[i].first.first);
				total += ((double)wway[i].second) / (R + wway[i].first);
				run -= ((double)wway[i].second) / (R + wway[i].first);
				//cout << wway[i].second << endl;
			} else {
				
				//total -= ((double)wway[i].first.second) / (S + wway[i].first.first);
				total += run + (wway[i].second - run * (R + wway[i].first))/(S + wway[i].first);
				run = -5;
				//cout << wway[i].second << endl;
			}
			
		}
		fout.precision(15);
		//cout << endl;
		fout << total;
		fout << endl;
	}
}

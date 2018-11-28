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
		int N;
		fin >> N;
		deque<pair<int, int> > orange;
		deque<pair<int, int> > blue;
		for(int i=0;i<N;i++){
			char c;
			int p;
			fin >> c >> p;
			if(c == 'O'){
				orange.push_back(pair<int, int>(p, i));
			} else {
				blue.push_back(pair<int, int>(p, i));
			}
		}
		int o = 1; // position of orange
		int b = 1; // position of blue
		int k = 0; // next button to press
		int i = 0; // number of steps taken
		while(k < N){
			int nextk = k;
			
			if(!orange.empty()){
				pair<int, int> n1 = orange.front();
				if(n1.first > o){
					o ++;
				} else if(n1.first < o){
					o --;
				} else if(n1.first == o && n1.second == k){
					orange.pop_front();
					nextk ++;
				}
			}
			if(!blue.empty()){
				pair<int, int> n2 = blue.front();
				if(n2.first > b){
					b ++;
				} else if(n2.first < b){
					b --;
				} else if(n2.first == b && n2.second == k){
					blue.pop_front();
					nextk ++;
				}
			}
			k = nextk;
			i++;
		}
		fout << "Case #"<< s+1 << ": " << i << endl;
	}
}

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <fstream>
#include <set>
#include <vector>
using namespace std;
#define INF 214748364
int T,N;
vector<int> candies;

int main(){
	ifstream in("Input.in");
	ofstream out("Output.out");
	in >> T;
	string str;
	for(int t = 0; t<T; t++){
		candies.clear();
		int num;
		in >> N;
		for(int j = 0; j<N; j++){
			in >> num;
			candies.push_back(num);
		}
		int ret = 0;
		for(int i = 0; i<candies.size(); i++)
			ret = ret ^ candies[i];
		if(ret != 0){
			out << "Case #" << t+1 << ": NO" << endl;
		}
		else{
			int ret = 0;
			sort(candies.begin(), candies.end());
			int temp = 0;
			for(int i = 0; i<candies.size(); i++){
				temp = temp ^ candies[i];
				int temp2=0,ret=0;
				for(int j = i+1; j<candies.size(); j++){
					temp2 = temp2 ^ candies[j];
					ret += candies[j];
				}
				if(temp == temp2){
					out << "Case #" << t+1 << ": " << ret << endl;
					break;
				}
			}
		}
	}
}


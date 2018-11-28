#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <iterator>
#include <algorithm>


using namespace std;


int main(void) {
	ifstream fin("A-small.in");
	ofstream fout("A-small.out");
	vector<int> res;
	int fin_res = 0;

	int T = 0;
	fin>>T;
	
	int cur = 0;
	vector<int> first;
	vector<int> second;
	
	int temp = 0;
	for(int i = 0; i < T ; i++){
		first.clear();
		second.clear();
		
		fin>>cur;
		for(int j = 0; j < cur ; j++){
			fin>>temp;
			first.push_back(temp);
		}
		for(int k = 0; k < cur ; k++) {
			fin>>temp;
			second.push_back(temp);
		}
		
		sort(first.begin(),first.end());
		sort(second.begin(),second.end());
		
		vector<int>::iterator f_iter = first.begin();
		vector<int>::reverse_iterator r_iter = second.rbegin();
		fin_res = 0;
		
		for(; f_iter != first.end() || r_iter != second.rend(); f_iter++ , r_iter++){
			fin_res += (*f_iter) * (*r_iter);
		}
		
		res.push_back(fin_res);
	}
	
	for(int p = 0; p < res.size(); p++){
		fout<<"Case #"<<p+1<<": "<<res[p]<<endl;
	}

	return 0;

}

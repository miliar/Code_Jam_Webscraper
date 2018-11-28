#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <stdint.h>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

size_t N;
vector<uint32_t> nums;

int main(int argc, char *argv[]){
    ifstream in(argv[1]);
    std::string line, t;
    getline(in,line);
    N = 0;
    int cases = atoi(line.c_str());
    for(size_t c = 0; c < cases; c++){
	getline(in,line);
	N = atoi(line.c_str());
	nums.clear();
	nums.reserve(N);
	getline(in,line);
	//cout << line << "\n";
	stringstream ss(line);
	size_t sum = 0;
	for(size_t i = 0; i < N; i++){
	    getline(ss,t,' ');
	    nums.push_back(atoi(t.c_str()));
	    sum ^= nums.back();
	}

	if(sum > 0){
	    cout << "Case #" << (c+1) << ": NO\n";
	    continue;
	}

	std::sort(nums.begin(), nums.end());
	unsigned long long s = 0;
	for(size_t i = 1; i < nums.size(); i++){
	    s += nums[i];
	}

	cout << "Case #" << (c+1) << ": " << s <<"\n";
    }
}

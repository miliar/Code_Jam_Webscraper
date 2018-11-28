#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>

typedef long long ll;

int c;
std::vector<std::string> words;
std::vector<std::vector<ll> > memo;
std::string seed;
const std::string reach = "welcome to code jam";

ll rec(int taken, int index) {
	if(taken == reach.size()) {
        return 1LL;
    }
    if(index == seed.size()) return 0LL;
	//if(seed.size()-index < reach.size()-taken) return 0LL;
	if(memo[taken][index] != 0) return memo[taken][index];
	ll sum = 0;
    if(reach[taken] == seed[index]) {
        sum += rec(taken+1,index+1);
    }
    sum += rec(taken,index+1);
    return memo[taken][index] = sum;
}

int main() {
	std::string line;
	std::getline(std::cin,line);
	std::istringstream is(line);
	is>>c;
	words.resize(c);
	for(int i = 0; i < c; ++i) {
        std::getline(std::cin,words[i]);
    }

    for(int i = 0; i < c; ++i) {
        seed = words[i];
    	memo.clear();
    	memo.resize(seed.size()+1);
        if(seed.size() >= reach.size()) {
            for(int j = 0; j < memo.size(); ++j) memo[j].resize(memo.size());
            for(int j = 0; j < memo.size(); ++j) for(int k = 0; k < memo[j].size(); ++k) memo[j][k] = 0;
            std::cout<<"Case #"<<i+1<<": "<<std::setfill('0')<<std::setw(4)<<rec(0,0)%10000<<std::endl;;
        } else {
            std::cout<<"Case #"<<i+1<<": "<<"0000"<<std::endl;;
        }
    }

    return 0;
}

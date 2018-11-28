#include <iostream>
#include <string>
#include <vector>
#include <map>

typedef long long ll;

ll pow(ll ind, int exp) {
	ll ret = 1;
	for(int i = 0; i < exp; ++i) {
		ret *= ind;
	}
	return ret;
}

ll in_base_10 (const std::vector<int>& num) {
	ll ret = 0;

	ll base = 0;

	for(int i = 0; i < num.size(); ++i) {
		if(num[i] > base) base = num[i];
	}

	base++;


	for(int i = 0; i < num.size(); ++i) {
		ret += num[i]*pow(base,num.size()-i-1);	
	}

	return ret;
}

void solve(int ind, std::string input) {
	ll ret;
	std::map<char,int> val;

	std::vector<int> num(input.size());

	val[input[0]] = 1;
	num[0] = 1;

	int next = 0;

	for(int i = 1; i < input.size(); ++i) {
		if(val.count(input[i]) == 0) {
			val[input[i]] = next;
			if(next == 0) next += 2;	
			else next++;
		}
		num[i] = val[input[i]];
	}

	/*
	for(int i = 0; i < num.size(); ++i) {
		std::cout<<num[i]<<" ";
	}
	std::cout<<std::endl;
	*/

	ret = in_base_10(num);

	std::cout<<"Case #"<<ind<<": "<<ret<<std::endl;
}

int main() {
	int cases;
	std::cin>>cases;

	for(int i = 0; i < cases; ++i) {
		std::string input;
		std::cin>>input;
		solve(i+1,input);
	}

	return 0;
}

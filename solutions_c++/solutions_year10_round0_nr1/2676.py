#include <iostream>
#include <string>

unsigned long long int result = 2;

unsigned long long int expt(unsigned long long int a){	
	if(a == 1) return result;
	result *= 2;
	expt(a-1);
}

int main(){
	unsigned long long int t, n, k, no=1;
	std::string state;
	
	std::cin >> t;

	for(int i=0; i < t; ++i){
		std::cin >> n >> k;
		result = 2;
		if(k == 0) state = "OFF";
		else if(((k+1) % expt(n)) == 0) state = "ON";
		else state = "OFF";
		
		std::cout << "Case #" << no << ": " << state << std::endl;
		++no;
	}
	return 0;
}

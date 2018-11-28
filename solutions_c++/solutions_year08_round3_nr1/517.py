#include <iostream>
#include <set>

int main(){
	long long int N;
	std::cin>>N;
	for (long long int case_id = 1; case_id <= N; ++case_id){
		long long int P, K, L;
		std::cin>>P>>K>>L;
		std::multiset<long long int> letter_freq;
		for(long long int letter = 1; letter <= L; ++letter){
			long long int freq;
			std::cin>>freq;
			letter_freq.insert(freq);
		}
		std::multiset<long long int>::reverse_iterator
				curr_biggest = letter_freq.rbegin();
		long long int total = 0;
		for (long long int presses = 1; presses <= P; ++presses){
			for(long long int key = 1; key <= K; ++key){
				total += presses * (*curr_biggest++);
				if(curr_biggest == letter_freq.rend()) break;
			}
			if(curr_biggest == letter_freq.rend()) break;
		}
		std::cout<<"Case #"<<case_id<<": ";
		if(curr_biggest != letter_freq.rend())
			std::cout<<"Impossible"<<std::endl;
		else
			std::cout<<total<<std::endl;
	}
	return 0;
}


#include <iostream>
#include <list>

int main(){
	unsigned long long int t, r, k, n, no=1, cost, tmp, people, size, loop;
	std::list<int> groups;
	
	std::cin >> t;
	for(int i=0; i < t; ++i){
		std::cin >> r >> k >> n;
		groups.clear();
		for(int j=0; j < n; ++j){
			std::cin >> tmp;	
			groups.push_back(tmp);
		}
		cost = 0;
		size = groups.size();
		for(int j=0; j < r; ++j){
			people = 0;
			loop = 0;
			while(people + (tmp = groups.front()) <= k){
				people += tmp;
				groups.pop_front();
				groups.push_back(tmp);
				++loop;
				if(size == loop) break;
			}
			cost += people;
		}
		std::cout << "Case #" << no << ": " << cost << std::endl;
		++no;
	}
	return 0;
}

#include <iostream>
#include <vector>

int main(){
	int t, n, tmp_l, tmp_r, count, cases=1;
	std::vector<int> left, right;
	std::vector<int>::iterator it_l, it_r, it_ll, it_rr;

	std::cin >> t;
	for(int i=0; i < t; ++i){
		std::cin >> n;

		left.clear();
		right.clear();
		count = 0;	

		for(int j=0; j < n; ++j){
			std::cin >> tmp_l >> tmp_r;
			left.push_back(tmp_l);
			right.push_back(tmp_r);
		}

		it_l = left.begin();
		it_r = right.begin();

		while(it_l != left.end()){ 
			it_ll = it_l + 1;
			it_rr = it_r + 1;
			
			while(it_ll != left.end()){
				if( (*it_l > *it_ll && *it_r < *it_rr) || (*it_l < *it_ll && *it_r > *it_rr) ) ++count;

				++it_ll;
				++it_rr;
			}

			++it_l;
			++it_r;
		}
	
		std::cout << "Case #" << cases << ": " << count << std::endl;
		++cases;

	}
	return 0;
}

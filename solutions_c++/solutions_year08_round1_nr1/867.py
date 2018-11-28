#include <iostream>
#include <set>
#include <vector>

int main(){
	int N;
	std::cin>>N;
	for(int i = 1; i <= N; ++i){
		int dim;
		std::cin>>dim;
		std::vector<std::multiset<int> > vectors(2);
		for (int j = 1; j <=2; ++j){
			for(int k = 1; k <= dim; ++k){
				int value;
				std::cin >> value;
				vectors[j - 1].insert(value);
			}
		}
		std::multiset<int>::reverse_iterator reverse = vectors[1].rbegin();
		int total = 0;
		for(std::multiset<int>::iterator forward = vectors[0].begin();
						(forward != vectors[0].end()) && (reverse != vectors[1].rend());
						)
		{
			total += (*forward++) * (*reverse++);
		}
		std::cout<<"Case #"<<i<<": "<<total<<std::endl;
	}
	return 0;
}


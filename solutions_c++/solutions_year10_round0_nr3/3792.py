#include <iostream>
#include <list>

class TestCase {
	short _id;
	long R, k, N, money;
	std::list<long> * groups;
	
public:
	TestCase(short id) : _id(id), money(0) {
		std::cin >> R;
		std::cin >> k;
		std::cin >> N;
		int temp;
		groups = new std::list<long>();
		for (long i = 0; i < N; i++) {
			std::cin >> temp;
			groups->push_back(temp);
		}
	}
	
	void process() {
		for (long i = 0; i < R; i++) {
			long curr = 0;
			std::list<long> temp;
			while(curr < k && groups->size() != 0) {
				if(curr + groups->front() <= k) {
					money += groups->front();
					curr += groups->front();
					temp.push_back(groups->front());
					groups->pop_front();
				}
				else {
					break;
				}
			}
			while(temp.size() != 0) {
				groups->push_back(temp.front());
				temp.pop_front();
			}
		}
		std::cout << "Case #" << _id << ": " << money << std::endl;
	}
	
};

int main() {
	
	std::list<TestCase*> cases;
	
	short t;
	
	std::cin >> t;
	
	for (short i = 0; i < t; i++) {
		cases.push_back(new TestCase(i+1));
	}
	
	for(std::list<TestCase*>::iterator it = cases.begin(); it != cases.end(); it++)
		(*it)->process();
	
	return 0;
}
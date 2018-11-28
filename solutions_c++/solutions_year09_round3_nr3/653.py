
#include <set>
#include <iostream>
#include <fstream>
#include <limits.h>

int cost(int start, int end, std::set<int> numbers) {
  if(numbers.empty())
    return 0;
  if(end < start)
    return 0;
  if(numbers.size() == 1)
    return end-start;
  int current_cost = end-start;
  int min_remaining_cost = INT_MAX;
  for(std::set<int>::iterator it = numbers.begin();
      it != numbers.end();
      it++) {
    int number = *it;
    std::set<int> left;
    std::set<int> right;
    for(std::set<int>::iterator it2 = numbers.begin();
	it2 != numbers.end();
	it2++) {
      if(*it2 < number)
	left.insert(*it2);
      if(*it2 > number)
	right.insert(*it2);
    }
    int left_cost = cost(start, number-1, left);
    int right_cost = cost(number+1, end, right);
    if(left_cost + right_cost < min_remaining_cost)
      min_remaining_cost = left_cost + right_cost;
  }
  return current_cost + min_remaining_cost;
}

int main(int argc, char * argv[]) {

  std::ifstream in_file(argv[1]);
  int num_cases;
  in_file >> num_cases;

  for(int i=0; i<num_cases; i++) {
    std::cout << "Case #" << i+1 << ": ";
    int P;
    in_file >> P;
    int Q;
    in_file >> Q;
    std::set<int> numbers;
    for(int j=0; j<Q; j++) {
      int number;
      in_file >> number;
      numbers.insert(number);
    }
    int min_cost = cost(1, P, numbers);
    std::cout << min_cost << std::endl;
  }
}

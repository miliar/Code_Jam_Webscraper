#include <iostream>
#include <string>
#include <map>
#include <cstdio>

int L, D, N;
std::map<std::string, bool> words;

int Count(std::string &s, int position, std::string result) {
  if (words.find(result) == words.end()) {
    return 0;
  }
  if (position == s.size()) {
    //std::cout << s << " " << result << std::endl;
    return 1;
  }
  int sum_result = 0;
  if (s[position] == '(') {
    int new_position = position;
    while (s[new_position++] != ')');
    for(int i = position + 1; i < new_position - 1; ++i) {
      sum_result += Count(s, new_position, result + s[i]);
    }
  } else {
    sum_result = Count(s, position + 1, result + s[position]);
  } 
  return sum_result;
}

int main() {
  std::cin >> L >> D >> N;
  words[""] = true;
  for(int i = 0; i < D; ++i) {
    std::string s, part_s;
    std::cin >> s;
    for(int j = 0; j < s.size(); ++j) {
      part_s += s[j];
    	words[part_s] = true;
    }
  }
  for(int i = 0; i < N; ++i) {
    std::string s;
    std::cin >> s;
    int result = Count(s, 0, "");
    std::cout << "Case #" << i + 1 << ": " << result << std::endl;
  }
	return 0;	                
}
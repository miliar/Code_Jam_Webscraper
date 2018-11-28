#include <iostream>
#include <set>
#include <vector>
#include <iterator>

int countWord
(const std::vector<std::string>& pv, int index,
 std::string word,
 const std::set<std::string>& dict)
{
  if(index > 0 && dict.find(word) == dict.end()) {
    return 0;
  }
  if(pv.size() == index) {
    return 1;
  }
  int count = 0;
  for(int i = 0; i < pv[index].size(); ++i) {
    count += countWord(pv, index+1, word+pv[index][i], dict);
  }
  return count;
}

int main() {
  int L, D, N;
  std::cin >> L >> D >> N;
  std::set<std::string> dic;
  for(int i = 0; i < D; ++i) {
    //std::cout << i << std::endl;
    std::string w;
    std::cin >> w;
    for(int j = 1; j <= w.size(); ++j) {
      // std::cout << w.substr(0, j) << std::endl;
      dic.insert(w.substr(0, j));
    }
  }
  for(int i = 1; i <= N; ++i) {
    std::string pattern;
    std::cin >> pattern;
    std::vector<std::string> pv;
    std::string::size_type index = 0;
    std::string c;
    bool inparen = false;
    for(int index = 0; index < pattern.size(); ++index) {
      switch(pattern[index]) {
      case '(':
	inparen = true;
	break;
      case ')':
	pv.push_back(c);
	c.clear();
	inparen = false;
	break;
      default:
	if(inparen) {
	  c += pattern[index];
	} else {
	  pv.push_back(pattern.substr(index,1));
	}
      }
    }
    //std::copy(pv.begin(), pv.end(), std::ostream_iterator<std::string>(std::cout, ","));
    std::cout << "Case #" << i << ": " << countWord(pv, 0, "", dic) << std::endl;
  }
}

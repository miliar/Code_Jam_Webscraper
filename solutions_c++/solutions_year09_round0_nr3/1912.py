#include <cstring>
#include <iostream>
#include <set>
#include <vector>
#include <iterator>
#include <algorithm>
#include <iomanip>

int memo[19][501];

static int countw(const std::vector<std::vector<int> >& v, int index, int pos)
{
  //std::cerr << "index = " << index << ", " << pos << std::endl;
  if(index == v.size()) {
    return 1;
  }
  if(memo[index][pos] > 0) {
    return memo[index][pos];
  }
  int count = 0;
  const std::vector<int>& vv = v[index];
  for(int i = 0; i < vv.size(); ++i) {
    if(vv[i] <= pos) continue;
    int c = countw(v, index+1, vv[i]);
    if(c == 0) break;
    count += c;
    count %= 10000;
  }
  memo[index][pos] = count;
  return count;
}

int main() {
  int N;
  std::cin >> N;
  std::string line;
  getline(std::cin, line);
  for(int n = 1; n <= N; ++n) {
    std::string line;
    getline(std::cin, line);
    std::vector<std::vector<int> > wc(123, std::vector<int>());
    for(int i = 0; i < line.size(); ++i) {
      wc[line[i]].push_back(i);
    }
    std::vector<std::vector<int> > v;
    v.push_back(wc['w']);
    v.push_back(wc['e']);
    v.push_back(wc['l']);
    v.push_back(wc['c']);
    v.push_back(wc['o']);
    v.push_back(wc['m']);
    v.push_back(wc['e']);
    v.push_back(wc[' ']);
    v.push_back(wc['t']);
    v.push_back(wc['o']);
    v.push_back(wc[' ']);
    v.push_back(wc['c']);
    v.push_back(wc['o']);
    v.push_back(wc['d']);
    v.push_back(wc['e']);
    v.push_back(wc[' ']);
    v.push_back(wc['j']);
    v.push_back(wc['a']);
    v.push_back(wc['m']);
    memset(memo, 0, sizeof(memo));
    int total = 0;
    for(int i = 0; i < wc['w'].size(); ++i) {
      int pos = wc['w'][i];
      total += countw(v, 1, pos);
    }
    total %= 10000;
    std::cout << "Case #" << n << ": " << std::setfill('0') << std::setw(4) << total << std::endl;
  }
}

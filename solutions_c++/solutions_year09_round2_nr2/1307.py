#include <iostream>
#include <vector>
#include <utility>
#include <map>

std::map<std::pair<long long, long long>, long long> dp;

long long doit(
    long long n,
    const std::string& h,
    const std::string& r) {

  long long hn = atol(h.c_str());
  long long rn = atol(r.c_str());

  std::map<std::pair<long long, long long>, long long>::iterator i =
      dp.find(std::make_pair(hn,rn));
  if(i != dp.end()) {
    return (*i).second;
  }

  //std::cout << h << "/" << r << std::endl;

  if( r == "" ) {
    return atoll(h.c_str());
  }

  long long mx = LONG_LONG_MAX;
  for(size_t i = 0 ; i < r.size() ; i++ ) {
    std::string hh = h + r[i];
    std::string rr = r;
    rr.erase(rr.begin() + i);
    long long m = doit(n,hh,rr);
    if( n < m && m < mx ) {
      mx = m;
    }
  }

  //std::cerr << r << ":" << mx << std::endl;

  return dp[std::make_pair(hn,rn)]=mx;
}
                 


int main() {
  int N;
  std::cin >> N;
  for( int i =  0 ; i< N ; i++ ) {
    std::string s;
    std::cin >> s;

    dp.clear();

    std::string ss = s;
    std::sort(ss.begin(),ss.end());
    std::reverse(ss.begin(),ss.end());
    long long n = atoll(s.c_str());
    if( ss == s ) {
      std::cout << "Case #" << (i+1) << ": " << doit(n,"",s+"0") << std::endl;
    } else {
      std::cout << "Case #" << (i+1) << ": " << doit(n,"",s) << std::endl;
    }
  }
  return 0;
}

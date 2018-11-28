#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <climits>
#include <boost/tuple/tuple.hpp>
#include <boost/tuple/tuple_comparison.hpp>

using namespace std;

char m[55][55];
int R, C, F;
int K;

typedef std::pair<int, int> addr;


struct Context {
  int x;
  int y;
  set<addr>  holes;

  bool operator<(const Context& c) const {
    return boost::make_tuple(x,y,holes) < boost::make_tuple(c.x,c.y,c.holes);
  }
};

int result;
std::set<Context> cache;
std::vector<Context> q;
std::vector<Context> qq;


bool wall(int y, int x, const std::set<addr>& s) {
  return m[y][x] && s.find(addr(y,x)) == s.end();
}

void doit(const Context& c) {
#if 0
  //std::cerr << c.y << "," << c.x << " ";
  for(set<addr>::const_iterator i = c.holes.begin() ; i != c.holes.end() ;++i ) {
    //cerr << "(" << (*i).first << "," << (*i).second <<") ";
  }
  //cerr << endl;
#endif
  if(c.y == R-1) {
    result = std::min(result, int(c.holes.size()));
    return;
  }

  if(cache.find(c) != cache.end()) {
    return;
  }

  cache.insert(c);

  if(!wall(c.y+1, c.x, c.holes)) {
    //cerr << "fall down ";
    // fall down
    int down = 0;
    while(c.y+down < R-1 && !wall(c.y+down+1,c.x,c.holes)) {
      down++;
    }
    //cerr << down << "/" << F << endl;
    if(F<down) { return; }
    if( c.y+down == R-1) {
      result = std::min(result, int(c.holes.size()));
      return;
    }      
    Context nc = c;
    nc.y = c.y+down;
    qq.push_back(nc);
    return;
  }
  if(0 < c.x && !wall(c.y, c.x-1, c.holes)) {
    Context nc = c;
    nc.x = c.x-1;
    qq.push_back(nc);
    if(wall(c.y+1, c.x-1, c.holes) && c.holes.size() < size_t(result)-1) {
      Context nc = c;
      nc.holes.insert(addr(nc.y+1,nc.x-1));
      qq.push_back(nc);
    }
  }
  if(c.x < C-1 && !wall(c.y, c.x+1, c.holes)) {
    Context nc = c;
    nc.x = c.x+1;
    qq.push_back(nc);
    if(wall(c.y+1, c.x+1, c.holes) && c.holes.size() < size_t(result)-1) {
      Context nc = c;
      nc.holes.insert(addr(nc.y+1,nc.x+1));
      qq.push_back(nc);
    }
  }
}

int foo(std::istream& is) {
  int N;
  is >> N;
  for(int i = 0 ;i < N ; i++ ) {
    is >> R >> C >> F;
    std::string line;
    std::getline(is, line);
    for(int y =0; y < R; y++ ) {
      for(int x = 0; x < C ; x++ ) {
        char c = is.get();
        m[y][x] = c == '#' ? 1 : 0;
      }
      std::getline(is, line);
    }

    result = INT_MAX;
    cache.clear();
    q.clear();
    qq.clear();

    Context ct;
    ct.x = 0;
    ct.y = 0;
    q.push_back(ct);

    while(!q.empty()) {
      for(size_t j = 0 ; j < q.size() ; j++ ) {
        doit(q[j]);
      }
        
      q.swap(qq);
      qq.clear();
    }

    if( result == INT_MAX) {
      cout << "Case #" << i+1 << ": No" << endl;
    } else {
      cout << "Case #" << i+1 << ": Yes " << result << endl;
    }
  }
  
  return 0;
}

int main() {
  //std::ifstream ifs("t.txt");
  foo(std::cin);
  return 0;
}

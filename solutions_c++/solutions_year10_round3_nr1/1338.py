#include <iostream>
#include <string>
#include <fstream>
#include <map>

int main(int argc, char **argv){

  try{
    std::ifstream in(argv[1]);
    std::ofstream out(argv[2]);
    std::size_t T;
    in >> T;
    for(std::size_t i(1) ; i <= T ; ++i){
      typedef   std::map<int, int> map_type;
      map_type lines;
      int n;
      in >> n;
      for(int j(0) ; j < n ; ++j){
	int l, r;
	in >> l >> r;
	lines[l] = r - l;
      }
      std::size_t res(0);
      for(map_type::iterator iter(lines.begin());
	  iter != lines.end();
	  ++iter){
	map_type::iterator iter2(iter);
	++iter2;
	for(;
	    iter2 != lines.end();
	    ++iter2){
	  if((iter2->first - iter->first) < (iter->second - iter2->second))
	    ++res;
	}
      }
      out << "Case #" << i << ": "<< res << std::endl;
    }
  }catch(std::exception& e){
    std::cout << e.what() << std::endl;
  }
  return 0;
}

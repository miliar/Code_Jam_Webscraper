#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>

class solver{
public:
  solver(){}
  typedef std::bitset<32> bits_type;
  bool operator()(std::ifstream& in){
    unsigned long size;
    unsigned long inclementations;
    in >> size >> inclementations;
    inclementations %= static_cast<unsigned long>(std::pow(static_cast<double>(2), static_cast<double>(size)));
    bits_type bits(inclementations);
    bool res(bits[0]);
    for(std::size_t i(1) ; i < size ; ++i){
      res &= bits[i];
    }
    return res;
    }
};





int main(int argc, char **argv){
  try{
    std::ifstream ifst(argv[1]);
    std::ofstream ofst(argv[2]);
    std::size_t cases(0);
    solver solve;
    ifst >> cases;
    for(std::size_t i(0); i < cases ; ++i){
      bool res(solve(ifst));
      ofst << "Case #" << i + 1 << ": "  <<  (res ? "ON" : "OFF") << std::endl;
    }
  }catch(std::exception& e){
    std::cout << e.what() << std::endl;
  }
}

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

template<typename T>
class ring_buffer{
public:
  typedef T value_type;
  ring_buffer(std::size_t size):
    buffer(size),
    index(0){
  }
  ~ring_buffer(){}
  
  value_type top(){
    return buffer[index];
  }

  void roll(){
    index = (index + 1)% buffer.size();
  }
  
  value_type& operator[](const std::size_t i){
    return buffer[i];
  }

private:
  std::vector<value_type> buffer;
  std::size_t index;
};

typedef ring_buffer<std::size_t> customer_buffer;

class solver{
public:

  std::string operator()(std::ifstream& in){
    std::size_t size, capacity, turns;
    in >> turns >> capacity >> size;
    customer_buffer customers(size);
    for(std::size_t i(0) ; i < size ; ++i){
      std::size_t value;
      in >> value;
      customers[i] =value;
    }
    std::size_t total_income(0);    
    for(std::size_t i(0) ; i < turns ; ++i){
      std::size_t filled(0);
      std::size_t groups(0);
      while(filled+customers.top() <= capacity && groups < size){
	filled+=customers.top();
	customers.roll();
	++groups;
      }
      total_income += filled;
    }
    std::ostringstream osst;
    osst << total_income;
    return osst.str();
    
  }
private:
  void solve(){

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
      ofst << "Case #" << i + 1 << ": "  <<  solve(ifst) << std::endl;
    }
  }catch(std::exception& e){
    std::cout << e.what() << std::endl;
  }
}

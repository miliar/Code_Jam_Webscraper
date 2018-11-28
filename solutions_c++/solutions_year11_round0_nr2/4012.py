
#include <map>
#include <vector>
#include <string>
#include <iostream>

int main( int argc, char * argv[] ) {
  //Q, W, E, R, A, S, D, F

  std::map<char, char> element_num;
  element_num['Q'] = 0;
  element_num['W'] = 1;
  element_num['E'] = 2;
  element_num['R'] = 3;
  element_num['A'] = 4;
  element_num['S'] = 5;
  element_num['D'] = 6;
  element_num['F'] = 7;

  int num_cases;
  std::cin >> num_cases;
  std::string test_case;
  for( int i=0; i<num_cases; ++i ) {
    char combine[8][8] = { {0} };
    char oppose[8][8] = { {0} };
    int num_combine;
    std::cin >> num_combine;
    for( int j=0; j<num_combine; ++j ) {
      std::string combine_case;
      std::cin >> combine_case;
      combine[element_num[combine_case[0]]][element_num[combine_case[1]]] = combine_case[2];
      combine[element_num[combine_case[1]]][element_num[combine_case[0]]] = combine_case[2];
    }
    int num_oppose;
    std::cin >> num_oppose;
    for( int j=0; j<num_oppose; ++j ) {
      std::string oppose_case;
      std::cin >> oppose_case;
      oppose[element_num[oppose_case[0]]][element_num[oppose_case[1]]] = '1';
      oppose[element_num[oppose_case[1]]][element_num[oppose_case[0]]] = '1';
    }
    int num_input;
    std::cin >> num_input;
    std::string input;
    std::cin >> input;
    std::vector<char> output;
    for( int j=0; j<num_input; ++j ) {
      output.push_back( input[j] );
      size_t op_size = output.size();
      if( op_size >=2 ) {
	char last = output[op_size - 1];
	char last_but_one = output[op_size - 2];
	int last_num = (element_num.find(last) != element_num.end()) ? element_num[last] : -1;
	int last_but_one_num = (element_num.find(last_but_one) != element_num.end()) ? element_num[last_but_one] : -1;
	char c = 0;
	if( last_num > -1 && last_but_one_num > -1 )
	  c = combine[last_num][last_but_one_num];
	if( c ) {
	  output.pop_back();
	  output.pop_back();
	  output.push_back( c );
	}
	else {
	  for( int k=0; k<op_size-1; ++k ) {
	    int k_num = (element_num.find(output[k]) != element_num.end()) ? element_num[output[k]] : -1;
	    char o = 0;
	    if( last_num > -1 && k_num > -1 )
	      o = oppose[last_num][k_num];
	    if( o ) {
	      output.clear();
	      break;
	    }
	  }
	}
      }
    }
    std::cout << "Case #" << i+1 << ": [";
    for( int j=0; j<output.size(); ++j ) {
      std::cout << output[j];
      if( j != output.size() - 1 )
	std::cout << ", ";
    }
    std::cout << "]" << std::endl;
  }
}

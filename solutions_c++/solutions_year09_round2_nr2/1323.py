#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>
#include <cmath>

// typedef
typedef __int64 int64;
typedef unsigned int uint;

// define
#ifdef _DEBUG
#	define CHECK_DATA 1
#else
#	define CHECK_DATA 0
#endif

#ifdef    WIN32
#	define DIRECTORY_SEPARATOR '\\'
#else
#	define DIRECTORY_SEPARATOR '/'
#endif

#define DEFAULT_INPUT "test.txt"
#define DEFAULT_OUTPUT "result.txt"

//=========================================================================//
//     next_combination
//=========================================================================//
template < class BidirectionalIterator >
bool next_combination ( BidirectionalIterator first1 ,
  BidirectionalIterator last1 ,
  BidirectionalIterator first2 ,
  BidirectionalIterator last2 )
{
  if (( first1 == last1 ) || ( first2 == last2 )) {
    return false ;
  }
  BidirectionalIterator m1 = last1 ;
  BidirectionalIterator m2 = last2 ; --m2;
  while (--m1 != first1 && !(* m1 < *m2 )){
  }
  bool result = (m1 == first1 ) && !(* first1 < *m2 );
  if (! result ) {
    // ‡@
    while ( first2 != m2 && !(* m1 < * first2 )) {
      ++ first2 ;
    }
    first1 = m1;
    std :: iter_swap (first1 , first2 );
    ++ first1 ;
    ++ first2 ;
  }
  if (( first1 != last1 ) && ( first2 != last2 )) {
    // ‡A
    m1 = last1 ; m2 = first2 ;
    while (( m1 != first1 ) && (m2 != last2 )) {
      std :: iter_swap (--m1 , m2 );
      ++ m2;
    }
    // ‡B
    std :: reverse (first1 , m1 );
    std :: reverse (first1 , last1 );
    std :: reverse (m2 , last2 );
    std :: reverse (first2 , last2 );
  }
  return ! result ;
}

template < class BidirectionalIterator >
bool next_combination ( BidirectionalIterator first ,
  BidirectionalIterator middle ,
  BidirectionalIterator last )
{
  return next_combination (first , middle , middle , last );
}

//=========================================================================//
//     Input Class
//=========================================================================//
class Input{
public:
	int64 N;
public:
	// for Stream
	friend std::istream& operator>>(std::istream& in, Input &input){
		in >> input.N;

		return in;
	}
	// for Stream
	friend std::ostream& operator<<(std::ostream& out, const Input& input){
		using std::endl;

		
		return out;
	}
};

//=========================================================================//
//     Result Class
//=========================================================================//
class Result{
private:
	int64 value_;
public:
	// Solve
	void Solve(const Input &input){
		int64 i = input.N;
		std::vector<int64> values;
		while(i!=0){
			values.push_back(i % 10);
			i /= 10;
		}
		values.push_back(0);
		std::reverse(values.begin(), values.end());
		std::next_permutation(values.begin(), values.end());
		
		
		value_ = 0;
		for(uint i=0; i<values.size(); ++i){
			value_ = value_ * 10 + values[i];
		}

	}
	// for Stream
	friend std::ostream& operator<<(std::ostream& out, const Result& result){
		using std::endl;

		out << " " << result.value_ << endl;

		return out;
	}
};

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(const std::string &file_name, std::vector<Input> *inputs){
	// Open File
	std::ifstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "Input File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}

	// get number
	uint T;
	file >> T;
	std::getline(file, std::string());
	// get data
	inputs->resize(T);
	for(uint i=0; i<T; ++i){
		file >> (*inputs)[i];
	}

	// close
	file.close();
	return 0;
}


//=========================================================================//
//     Output Data (for debug)
//=========================================================================//
void OutputData(std::ostream &out, const std::vector<Input> &inputs){
	using std::endl;

	out << "=====[Input]================" << endl;
	out << inputs.size() << endl;
	for(uint i=0; i<inputs.size(); ++i){
		out << inputs[i];
	}
	out << endl;
}

//=========================================================================//
//     Output Result
//=========================================================================//
void OutputResult(std::ostream &out, const std::vector<Result> &results){
	for(uint i=0; i<results.size(); ++i){
		out << "Case #" << (i+1) << ":" << results[i];
	}
}

int OutputResult(const std::string &file_name, const std::vector<Result> &results, double time){
	using std::cout;
	using std::endl;

	std::ofstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "Output File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	cout << "=====[Result]===============" << endl;
	OutputResult(cout, results);
	OutputResult(file, results);
	cout << endl;

	file.close();

	cout << "=====[Info]=================" << endl;
	cout << "time: "
	     << std::setprecision(2) << std::setiosflags(std::ios::fixed)
	     << time << "sec" << endl;
	cout << endl;
	return 0;
}


//=========================================================================//
//     Solve
//=========================================================================//
clock_t Solve(const std::vector<Input> &inputs, std::vector<Result> *result){
	clock_t start, end;
	start = clock();

	result->resize(inputs.size());
	for(uint i=0; i<inputs.size(); ++i){
		(*result)[i].Solve(inputs[i]);
	}

	end = clock();
	return end - start;
}

//=========================================================================//
//     Main
//=========================================================================//
int main(int argc, char *argv[]){
	// Get File Name
	std::string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	std::string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;

	// Get Input
	std::vector<Input> inputs;
	if(GetInput(input_file_name, &inputs) != 0){
		return -1;
	}

	// check data
#if CHECK_DATA
	OutputData(std::cout, inputs);
#endif

	// Solve
	std::vector<Result> results;
	uint time = Solve(inputs, &results);

	// Output Result
	if(OutputResult(output_file_name, results, (time / static_cast<double>(CLOCKS_PER_SEC))) != 0){
		return -1;
	}

	return 0;
}
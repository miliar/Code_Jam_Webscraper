#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
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
//     Input Class
//=========================================================================//
class Input{
public:
	struct Tree{
		double rate;
		std::string feature;
		Tree *yes, *no;
		bool leaf;
	};
	Tree *root;
	struct Animal{
		std::string name;
		std::set<std::string> features;
	};
	std::vector<Animal> animals;
public:
	Input(){
		root = NULL;
	}
	~Input(){
		if(root != NULL){
			DeleteTree(root);
		}
	}
	static Tree* LoadTree(std::istringstream &in){
		Tree* tree = new Tree();
		std::string tree_str[2];
		char c;

		in >> c >> tree->rate >> tree->feature;

		if(tree->feature != ")"){
			for(uint i=0; i<2; ++i){
				int count = 0;
				bool end = false;
				do{
					in.get(c);
					tree_str[i] += c;
					if(c == ')'){
						--count;
						end = true;
					}
					else if(c == '('){
						++count;
					}
				}while(count != 0 || !end);
			}

			tree->leaf = false;
			tree->yes = LoadTree(std::istringstream(tree_str[0]));
			tree->no = LoadTree(std::istringstream(tree_str[1]));
		}
		else{
			tree->leaf = true;
		}

		return tree;
	}
	static void DeleteTree(Tree *tree){
		if(!tree->leaf){
			DeleteTree(tree->yes);
			DeleteTree(tree->no);
		}
		delete tree;
	}
	// for Stream
	friend std::istream& operator>>(std::istream& in, Input &input){
		std::string line, tree_str;
		uint L, A, n;
		in >> L;
		std::getline(in, line);
		for(uint i=0; i<L; ++i){
			std::getline(in, line);
			tree_str += line;
		}
		input.root = LoadTree(std::istringstream(tree_str));
		in >> A;
		input.animals.resize(A);
		std::string feature;
		for(uint i=0; i<A; ++i){
			in >> input.animals[i].name;
			in >> n;
			for(uint j=0; j<n; ++j){
				in >> feature;
				input.animals[i].features.insert(feature);
			}
		}

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
	std::vector<double> values_;
public:
	// Solve
	void Solve(const Input &input){
		double rate;
		for(uint i=0; i<input.animals.size(); ++i){
			rate = Match(input.root, input.animals[i]);

			values_.push_back(rate);
		}
	}
	double Match(Input::Tree *tree, const Input::Animal &animal){
		double rate = tree->rate;
		if(!tree->leaf){
			if(animal.features.find(tree->feature) == animal.features.end()){
				rate *= Match(tree->no, animal);
			}
			else{
				rate *= Match(tree->yes, animal);
			}
		}
		return rate;
	}
	// for Stream
	friend std::ostream& operator<<(std::ostream& out, const Result& result){
		using std::endl;

		out << endl;
		for(uint i=0; i<result.values_.size(); ++i){
			out << std::setprecision(7) << std::setiosflags(std::ios::fixed) << result.values_[i] << endl;
		}

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
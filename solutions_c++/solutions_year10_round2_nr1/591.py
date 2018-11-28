#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <queue>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <climits>
#include <boost/iostreams/filtering_stream.hpp>
#include <boost/iostreams/device/file.hpp>

using namespace std;

// typedef
typedef __int64 int64;
typedef unsigned __int64 uint64;
typedef unsigned int uint;

#define TRUE 1
#define FALSE 0

// define
#define OUTPUT_CONSOLE TRUE
#define CHECK_DATA FALSE

#ifdef    WIN32
#	define DIRECTORY_SEPARATOR '\\'
#else
#	define DIRECTORY_SEPARATOR '/'
#endif

#define DEFAULT_INPUT "data.txt"
#define DEFAULT_OUTPUT "result.txt"
#define DEFAULT_LOG "log.txt"

class Result;

/*
	
*/

//=========================================================================//
//     Input Class
//=========================================================================//
class Input{
	friend class Result;

private:
	/*
		TODO: 一問分のデータを格納する変数を追加する
	*/
	vector<vector<string> > NL, ML;

public:
	// Get
	void Get(istream& in){
		/*
			TODO: 一問分のデータを読み込む
		*/
		uint N, M;
		in >> N >> M;
		in.get();
		string str;
		for(uint i=0; i<N; ++i){
			getline(in, str);
			NL.push_back(split(str, "/"));
		}
		for(uint i=0; i<M; ++i){
			getline(in, str);
			ML.push_back(split(str, "/"));
		}
	}

	vector<string> split(string str, string delim){
		vector<string> result;
		int cutAt;
		while( (cutAt = str.find_first_of(delim)) != str.npos ){
			if(cutAt > 0){
				result.push_back(str.substr(0, cutAt));
			}
			str = str.substr(cutAt + 1);
		}
		if(str.length() > 0){
			result.push_back(str);
		}
		return result;
	}

	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分のデータを出力する(※読み込みが成功したかどうかの確認用)
		*/
		out << NL.size() << " " << ML.size() << endl;
		for(uint i=0; i<NL.size(); ++i){
			for(uint j=0; j<NL[i].size(); ++j){
				out << "/" << NL[i][j];
			}
			out << endl;
		}
		for(uint i=0; i<ML.size(); ++i){
			for(uint j=0; j<ML[i].size(); ++j){
				out << "/" << ML[i][j];
			}
			out << endl;
		}
	}
};

//=========================================================================//
//     Result Class
//=========================================================================//
class Result{
private:
	/*
		TODO: 一問分の結果を格納する変数を追加する
	*/
	uint64 result;

	set<string> directories;
public:
	// Solve
	void Solve(const Input &in, ostream &debug){
		/*
			TODO: 問題を一問解く
		*/
		result = 0;
		stringstream stream;
		for(uint i=0; i<in.NL.size(); ++i){
			stream.str("");
			stream.clear();
			for(uint j=0; j<in.NL[i].size(); ++j){
				stream << "/" << in.NL[i][j];
				directories.insert(stream.str());
			}
		}
		for(uint i=0; i<in.ML.size(); ++i){
			stream.str("");
			stream.clear();
			for(uint j=0; j<in.ML[i].size(); ++j){
				stream << "/" << in.ML[i][j];
				string name = stream.str();
				if(directories.find(name) == directories.end()){
					++result;
					directories.insert(name);
				}
			}
		}
	}

	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分の結果を出力する
		*/

		out << " " << result << endl;
	}
};


//=========================================================================//
//     Input & Result Stream
//=========================================================================//
ostream& operator<<(ostream& out, const Result& result){
	result.Output(out);
	return out;
}

istream& operator>>(istream& in, Input &input){
	input.Get(in);
	return in;
}
ostream& operator<<(ostream& out, const Input& input){
	input.Output(out);
	return out;
}

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(const string &file_name, vector<Input> *inputs){
	// Open File
	ifstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "Input File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	// get number
	uint T;
	file >> T;
	getline(file, string());
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
//     Stdio Filter
//=========================================================================//
template <typename Ch>
class basic_stdio_filter
{
    static void stdout_write(const char* s, std::streamsize n) { std::cout.write(s, n); }
    static void stdout_write(const wchar_t* s, std::streamsize n) { std::wcout.write(s, n); }

public:
    typedef Ch char_type;
    struct category
        : boost::iostreams::dual_use
        , boost::iostreams::filter_tag
        , boost::iostreams::multichar_tag
        , boost::iostreams::optimally_buffered_tag
    {};

    basic_stdio_filter(){}

    std::streamsize optimal_buffer_size() const{
        return 0;
    }

    template<typename Source>
    std::streamsize read(Source& src, char_type* s, std::streamsize n){
        std::streamsize result = boost::iostreams::read(src, s, n);
		if(result == -1){
            return -1;
		}

        stdout_write(s, n);
        return result;
    }

    template<typename Sink>
    std::streamsize write(Sink& snk, const char_type* s, std::streamsize n){
        std::streamsize result = boost::iostreams::write(snk, s, n);
        stdout_write(s, n);
        return result;
    }
};
BOOST_IOSTREAMS_PIPABLE(basic_stdio_filter, 1)
typedef basic_stdio_filter<char> stdio_filter;

//=========================================================================//
//     Solve
//=========================================================================//
void Solve(const vector<Input> &inputs, vector<Result> *results, ostream &log){
	clock_t start, end;
	start = clock();

	results->resize(inputs.size());
	for(uint i=0; i<inputs.size(); ++i){
#if CHECK_DATA
		log << "=====[#" << setw(3) << (i+1) << "]============================================="
			<< endl << inputs[i]
			<< endl;
#endif
		log << "Case #" << (i+1) << ":";
		(*results)[i].Solve(inputs[i], log);
		log << (*results)[i];
	}
	end = clock();
	double time = (end - start) / static_cast<double>(CLOCKS_PER_SEC);
	log << "========================================================" << endl
		<< "time: "
		<< setprecision(2) << setiosflags(ios::fixed)
	    << time << "sec" << endl
		<< endl;
}

//=========================================================================//
//     Main
//=========================================================================//
int main(int argc, char *argv[]){
	// Get File Name
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
				log_file_name = dir + DEFAULT_LOG,
		        output_file_name = dir + DEFAULT_OUTPUT;
	// Open Stream
	boost::iostreams::file_sink log_sink(log_file_name.c_str());
	if(!log_sink.is_open()){
		cout << "Log File Open Error: [" << log_file_name << "]" << endl;
		return -1;
	}
#if OUTPUT_CONSOLE
	boost::iostreams::filtering_ostream log(stdio_filter() | log_sink);
#else
	boost::iostreams::filtering_ostream log(log_sink);
#endif
	ofstream file(output_file_name.c_str());
	if(!file.is_open()){
		cout << "Output File Open Error: [" << output_file_name << "]" << endl;
		return -1;
	}

	// Get Input
	vector<Input> inputs;
	if(GetInput(input_file_name, &inputs) != 0){
		return -1;
	}

	// Solve
	vector<Result> results;
	Solve(inputs, &results, log);

	// Output Result
	for(uint i=0; i<results.size(); ++i){
		file << "Case #" << (i+1) << ":" << results[i];
	}
	file.close();

	return 0;
}

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

#define NOT_FOUND 0xffffffff

int GetInput(
	const std::string &file_name,
	std::vector<std::string> *string_list
);
void OutputData(
	const std::vector<std::string> &string_list
);
std::vector<unsigned int> Solve(
	const std::vector<std::string> &string_list
);
unsigned int _Solve(
	const std::string &target, const unsigned int t, unsigned int target_char_count[256],
	const std::string &str, const unsigned int s, unsigned int str_char_count[256],
	std::vector<std::vector<unsigned int> > *counts
);
int OutputResult(const std::vector<unsigned int> &result);

//=========================================================================//
//     Main
//=========================================================================//
int main(int argc, char *argv[]){
	std::string file_name;
	if(argc > 1){
		file_name = argv[1];
	}
	else{
		file_name = "./test.txt";
	}

	std::vector<std::string> string_list;
	GetInput(file_name, &string_list);
	//OutputData(string_list);

	std::vector<unsigned int> result = Solve(string_list);
	OutputResult(result);
}

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(
	const std::string &file_name,
	std::vector<std::string> *string_list
){
	// File Open
	std::ifstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}
	// Input
	unsigned int N;
	file >> N;
	string_list->resize(N);
	std::getline(file, std::string());
	for(unsigned int i=0; i<N; ++i){
		std::getline(file, (*string_list)[i]);
	}

	return 0;
}

//=========================================================================//
//     Output Data
//=========================================================================//
void OutputData(const std::vector<std::string> &string_list){
	using std::cout;
	using std::endl;

	cout << string_list.size() << endl;
	for(unsigned int i=0; i<string_list.size(); ++i){
		cout << string_list[i] << endl;
	}
}

//=========================================================================//
//     Solve
//=========================================================================//
std::vector<unsigned int> Solve(const std::vector<std::string> &string_list){
	std::vector<unsigned int> result;
	const std::string target = "welcome to code jam";
	unsigned int target_char_count[256] = {};

	// targetに出てくる文字を数える
	for(unsigned int i=0; i<target.size(); ++i){
		++target_char_count[target[i]];
	}
	// 一度も出てこない文字を削る
	std::vector<std::string> tmp_string_list = string_list;
	for(unsigned int i=0; i<tmp_string_list.size(); ++i){
		for(unsigned int j=0; j<tmp_string_list[i].size(); ++j){
			if(target_char_count[tmp_string_list[i][j]] == 0){
				tmp_string_list[i].erase(j, 1);
				--j;
			}
		}
	}
	unsigned int string_char_count[256];
	std::vector<std::vector<unsigned int> > result_counts;
	for(unsigned int i=0; i<tmp_string_list.size(); ++i){
		// tmp_string_list[i]の文字数を数える
		for(unsigned int j=0; j<256; ++j){
			string_char_count[j] = 0;
		}
		for(unsigned int j=0; j<tmp_string_list[i].size(); ++j){
			++string_char_count[tmp_string_list[i][j]];
		}
		// 文字が足りているかチェック
		bool lack_of_character = false;
		for(unsigned int j=0; j<256; ++j){
			if(string_char_count[j] < target_char_count[j]){
				lack_of_character = true;
				break;
			}
		}
		if(lack_of_character){
			result.push_back(0);
		}
		else{
			result_counts.resize(target.size());
			for(unsigned int j=0; j<target.size(); ++j){
				result_counts[j].resize(tmp_string_list[i].size());
				for(unsigned int k=0; k<result_counts[j].size(); ++k){
					result_counts[j][k] = NOT_FOUND;
				}
			}
			result.push_back(_Solve(target, 0, target_char_count, tmp_string_list[i], 0, string_char_count, &result_counts));
		}
	}

	return result;
}

unsigned int _Solve(
	const std::string &target, const unsigned int t, unsigned int target_char_count[256],
	const std::string &str, const unsigned int s, unsigned int str_char_count[256],
	std::vector<std::vector<unsigned int> > *counts
){
	int count = 0;

	unsigned i;
	for(i=s; i<str.size(); ++i){
		--str_char_count[str[i]];
		if(str[i] == target[t]){
			if(t+1 >= target.size()){
				count += 1;
			}
			else{
				if((*counts)[t][i] == NOT_FOUND){
					--target_char_count[target[t]];
					(*counts)[t][i] = _Solve(target, t+1, target_char_count, str, i+1, str_char_count, counts);
					++target_char_count[target[t]];
				}
				count += (*counts)[t][i];
				count %= 10000;
			}
		}
		else if(str_char_count[str[i]] < target_char_count[str[i]]){
			break;
		}
	}
	for(unsigned j=s; j<=i && j<str.size(); ++j){
		++str_char_count[str[j]];
	}
	return count;
}

//=========================================================================//
//     Output Result
//=========================================================================//
int OutputResult(const std::vector<unsigned int> &result){
	using std::cout;
	using std::endl;

	std::string file_name = "./result.txt";
	std::ofstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	for(unsigned int i=0; i<result.size(); ++i){
		file << "Case #" << (i+1) << ": " << std::setfill('0')
			 << std::setw(4) << (result[i] % 10000) << endl;
		cout << "Case #" << (i+1) << ": " << std::setfill('0')
			 << std::setw(4) << (result[i] % 10000) << endl;
	}

	file.close();
	return 0;
}
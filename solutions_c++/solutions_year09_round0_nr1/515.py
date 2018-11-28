#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

//=========================================================================//
//     String Map Class
//=========================================================================//
class StringMap{
private:
	std::map<char, StringMap> next_;
public:
	StringMap(){Clear();}
	void Clear(){next_.clear();}
	void Add(const std::string &str){
		StringMap* p = this;
		for(unsigned int i=0; i<str.size(); ++i){
			p = p->Add(str[i]);
		}
	}
	StringMap* Contains(const char c){
		if(next_.find(c) == next_.end()){
			return NULL;
		}
		else{
			return &next_[c];
		}
	}
private:
	StringMap* Add(const char c){
		next_.insert(std::pair<char, StringMap>(c, StringMap()));
		return &next_[c];
	}
};

int GetInput(
	const std::string &file_name,
	unsigned int *L,
	std::vector<std::string> *DList,
	std::vector<std::vector<std::vector<char> > > *NList
);
void OutputData(
	const unsigned int L,
	const std::vector<std::string> &DList,
	const std::vector<std::vector<std::vector<char> > > &NList
);
std::vector<int> Solve(
	const unsigned int L,
	const std::vector<std::string> &DList,
	const std::vector<std::vector<std::vector<char> > > &NList
);
int ContainsPattern(StringMap *p, const int d, const std::vector<std::vector<char> > &pattern);
int OutputResult(const std::vector<int> &result);

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

	unsigned int L;
	std::vector<std::string> DList;
	std::vector<std::vector<std::vector<char> > > NList;

	GetInput(file_name, &L, &DList, &NList);
	OutputData(L, DList, NList);

	std::vector<int> result = Solve(L, DList, NList);
	OutputResult(result);
}

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(
	const std::string &file_name,
	unsigned int *L,
	std::vector<std::string> *DList,
	std::vector<std::vector<std::vector<char> > > *NList
){
	// File Open
	std::ifstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}
	// Input
	unsigned int D, N;
	file >> *L >> D >> N;
	for(unsigned int i=0; i<D; ++i){
		DList->resize(i+1);
		file >> (*DList)[i];
	}
	char c;
	for(unsigned int i=0; i<N; ++i){
		NList->resize(i+1);
		(*NList)[i].resize(*L);
		for(unsigned int j=0; j<*L; ++j){
			file >> c;
			if(c == '\n'){
				break;
			}
			else if(c == '('){
				while(file >> c){
					if(c == ')'){
						break;
					}
					(*NList)[i][j].push_back(c);
				}
			}
			else{
				(*NList)[i][j].push_back(c);
			}
		}
	}

	file.close();

	// Check
	if(DList->size() < D){
		std::cout << "DList Input Error !" << std::endl;
		return -1;
	}
	if(NList->size() < N){
		std::cout << "NList Input Error !" << std::endl;
		return -1;
	}
	for(unsigned int i=0; i<DList->size(); ++i){
		if((*DList)[i].size() != *L){
			std::cout << "DList[" << i << "] Input Error !" << std::endl;
			return -1;
		}
	}
	for(unsigned int i=0; i<NList->size(); ++i){
		if((*NList)[i].size() != *L){
			std::cout << "NList[" << i << "] Input Error !" << std::endl;
			return -1;
		}
	}

	return 0;
}

//=========================================================================//
//     Output Data
//=========================================================================//
void OutputData(
	const unsigned int L,
	const std::vector<std::string> &DList,
	const std::vector<std::vector<std::vector<char> > > &NList
){
	std::cout << L << std::endl;
	for(unsigned int i=0; i<DList.size(); ++i){
		std::cout << DList[i] << std::endl;
	}
	for(unsigned int i=0; i<NList.size(); ++i){
		for(unsigned int j=0; j<NList[i].size(); ++j){
			if(NList[i][j].size() == 1){
				std::cout << NList[i][j][0];
			}
			else{
				std::cout << "(";
				for(unsigned int k=0; k<NList[i][j].size(); ++k){
					std::cout << NList[i][j][k];
				}
				std::cout << ")";
			}
		}
		std::cout << std::endl;
	}
}

//=========================================================================//
//     Solve
//=========================================================================//
std::vector<int> Solve(
	const unsigned int L,
	const std::vector<std::string> &DList,
	const std::vector<std::vector<std::vector<char> > > &NList
){
	std::vector<int> result;
	result.resize(NList.size());

	StringMap string_map;
	for(unsigned int i=0; i<DList.size(); ++i){
		string_map.Add(DList[i]);
	}
	for(unsigned int i=0; i<NList.size(); ++i){
		result[i] = ContainsPattern(&string_map, L, NList[i]);
	}

	return result;
}

int ContainsPattern(StringMap *p, const int d, const std::vector<std::vector<char> > &pattern){
	if(p == NULL){
		return 0;
	}
	if(d == 0){
		return 1;
	}

	int count = 0;
	for(unsigned int i=0; i<pattern[pattern.size()-d].size(); ++i){
		count += ContainsPattern(p->Contains(pattern[pattern.size()-d][i]), d-1, pattern);
	}

	return count;
}

//=========================================================================//
//     Output Result
//=========================================================================//
int OutputResult(const std::vector<int> &result){
	// Result
	std::string file_name = "./result.txt";
	std::ofstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}

	for(unsigned int i=0; i<result.size(); ++i){
		std::cout << "Case #" << (i+1) << ": " << result[i] << std::endl;
		file << "Case #" << (i+1) << ": " << result[i] << std::endl;
	}

	file.close();
	return 0;
}
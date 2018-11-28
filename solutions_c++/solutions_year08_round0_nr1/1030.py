#include <string>
#include <fstream>
#include <vector>
#include <iostream>
#include <map>


class A
{
public:
	A(const std::string& file);
	virtual ~A() {;};
	
	void exec();

private:
	void nextCase();
	int count();
	bool isZeroCounter(
			std::map<std::string, int>& cnt);
	
	std::vector<std::string> search;
	std::vector<std::string> query;
	std::ifstream fin;
};

A::A(const std::string& file)
{
	fin.open(file.c_str(), std::ifstream::in);
}

void A::exec()
{
	int nofCases;
	fin >> nofCases;
	std::string empty;
	getline(fin, empty);
	std::cout << nofCases << std::endl;
	for (int icase = 0; icase < nofCases; icase++) {
		nextCase();
		std::cout << "Case #" << icase+1 << ": " << count() << std::endl;
	}
}

int A::count()
{
	int counter = 0;
	std::map<std::string, int> cnt;
	uint index = 0;
	
	for (uint i = 0; i < search.size(); i++) 
		cnt.insert(std::pair<std::string, int> (search[i], 0));

	uint ii = 0;
	do {
		if (index != 0) 
			for(std::map<std::string, int>::iterator i = cnt.begin(); i != cnt.end(); i++)
				(*i).second = 0;
		
		for(uint i = index; i < query.size(); i++) {
			cnt[query[i]]++;
			if (!isZeroCounter(cnt)) {
				//std::cout << "change: " << query[i] << std::endl;
				counter++;
				index = i;
				break;
			}
		}
		ii++;
	} while (ii < query.size());

	
	return counter;
}

bool A::isZeroCounter(
		std::map<std::string, int>& cnt)
{
	for(std::map<std::string, int>::iterator i = cnt.begin(); i != cnt.end(); i++) 
		if ((*i).second == 0) return true;
	return false;
}

void A::nextCase()
{
	search.clear();
	query.clear();
	int nofSearch;
	fin >> nofSearch;
	std::string empty;
	getline(fin, empty);
	//std::cout << "SEARCH " << nofSearch << ":" << std::endl;
	for (int isearch = 0; isearch < nofSearch; isearch++) {
		std::string se;
		getline(fin, se);
		//std::cout << se << " | ";// std::endl;
		search.push_back(se);
	}
	//std::cout << std::endl;
	int nofQuery;
	fin >> nofQuery;
	getline(fin, empty);
	//std::cout << "QUERY "<< nofQuery << ":" << std::endl;
	for (int iquery = 0; iquery < nofQuery; iquery++) {
		std::string qu;
		getline(fin, qu);
		//fin >> qu;
	//	std::cout << qu << " | "; //<< std::endl;
		query.push_back(qu);
	}
	//std::cout << std::endl;
}   


int main() {
	A a("A-large.in");
	a.exec();
	return 0;
}



#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <set>

class CmpDepLess: 
	public std::binary_function<
		const std::pair<int, int>&,
	    const std::pair<int, int>&,
	    bool> 
{
public:
	bool operator()(const std::pair<int, int>& a1, const std::pair<int, int>& a2) const {
		return a1.first < a2.first;
	}
};

class B
{
public:
	B(const std::string& file);
	virtual ~B() {;};
	
	void exec();

private:
	void nextCase();
	int count(
			std::vector<std::pair<int, int> >& a,
			std::vector<std::pair<int, int> >& b);
	
	std::vector<std::pair<int, int> > at;
	std::vector<std::pair<int, int> > bt;
	int delay;
	int NA, NB;
	
	std::ifstream fin;
};

B::B(const std::string& file)
{
	fin.open(file.c_str(), std::ifstream::in);
}

void B::exec()
{
	int nofCases;
	fin >> nofCases;
	std::cout << nofCases << std::endl;
	for (int icase = 0; icase < nofCases; icase++) {
		nextCase();
		std::cout << "Case #" << icase+1 << ": " << count(at, bt) << " " << count(bt, at) << std::endl;
	}
}

int B::count(
		std::vector<std::pair<int, int> >& a,
		std::vector<std::pair<int, int> >& b)
{
	int na = 0;
	std::sort(a.begin(), a.end(), CmpDepLess());
	for (uint i = 0; i < a.size(); i++) {
		bool isFree = false;
		for (uint j = 0; j < b.size(); j++){
			if ( b[j].second != -1 && a[i].first >= b[j].second){
				isFree = true;
				b[j].second = -1;
				break;
			}
		}
		if (!isFree) na++;
	}
	return na;
}

void B::nextCase()
{
	at.clear();
	bt.clear();
	fin >> delay;
	fin >> NA >> NB;
	int h1, m1, h2, m2;
	char c;
	for (int i = 0; i < NA; i++) {
		fin >> h1 >> c >> m1 >> h2 >> c >> m2;
		at.push_back(std::pair<int, int>(h1 * 60 + m1, h2 * 60 + m2 + delay));
		//std::cout << h1 << c << m1 << h2 << c << m2 << std::endl;
	}
	
    for (int i = 0; i < NB; i++) {
		fin >> h1 >> c >> m1 >> h2 >> c >> m2;
		bt.push_back(std::pair<int, int>(h1 * 60 + m1, h2 * 60 + m2 + delay));
    }
    
}

int main() {
	B b("B-large.in");
	b.exec();
	return 0;
}



#include <fstream>
#include <list>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

typedef pair<set<string>, list<string> > SearchCase;

SearchCase readCase(istream& strm){
	SearchCase aCase;
	int engines(0), queries(0);
	strm >> engines;
	string tmp;
	strm.ignore();
	do 
	{
		getline(strm, tmp);
		aCase.first.insert(tmp);
	} while (--engines);

	strm >> queries;
	if(queries == 0) return SearchCase();
	strm.ignore();
	do 
	{
		getline(strm, tmp);
		aCase.second.push_back(tmp);
	} while (--queries);

	return aCase;
}

template<class EContainer, class QContainer>
int doSwitch(EContainer& engines, QContainer& queries){	
	EContainer tmp(engines);
	EContainer::value_type lastValue;
	int rtn = 0;
	while(1){		
		while(tmp.size() != 0){
			if(queries.size()==0) return rtn;
			lastValue = queries.front();
			EContainer::iterator fnd = tmp.find(lastValue);
			if(fnd != tmp.end() && tmp.size() == 1){
				tmp = engines;
				tmp.erase(tmp.find(lastValue));
				queries.pop_front();
				break;
			}
			else if(fnd != tmp.end()){
				tmp.erase(fnd);				
			}
			queries.pop_front();
		}
		++rtn;
	}
	return rtn;
}

int main(){
	ifstream input("A-small.in");
	ofstream output("A-large.out", ios_base::out);
	int cases(0);	
	input >> cases;
	int total = cases;
	do 
	{
		SearchCase aCase(readCase(input));
		if (aCase.second.size() == 0){
			output << "Case #"  << total-cases+1 << ": " << 0 << '\n';
			continue;
		}
		int tmp = doSwitch(aCase.first, aCase.second);
		output << "Case #"  << total-cases+1 << ": " << tmp << '\n';
	} while (--cases);
}
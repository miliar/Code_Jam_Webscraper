#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <fstream>
#include <assert.h>

using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

std::vector< std::string > tokenize(const std::string &_str, const std::string &_delim)
{
	std::vector< std::string > result;
	
	char * pch;
	//	printf ("Splitting string \"%s\" into tokens:\n",str);
	
	char *str = strdup(_str.c_str());
	char *delim = strdup(_delim.c_str());
	pch = strtok(str, delim);
	while (pch != NULL)
	{
		result.push_back(pch);
		//		printf ("%s\n",pch);
		pch = strtok (NULL, delim);
	}
	free(str);
	free(delim);
	
	return result;
}

unsigned long long sum(std::vector< int > &value, unsigned long long select)
{
	unsigned long long result = 0;
	unsigned long long mask = 0x1;
	for(int i=0;i< value.size();i++){
		if(mask & select){
			result += value[i];
		}
		mask<<=1;
	}
	return result;
}

unsigned long long _xor(std::vector< int > &value, unsigned long long select)
{
	unsigned long long result = 0;
	unsigned long long mask = 0x1;
	for(int i=0;i< value.size();i++){
		if(mask & select){
			result ^= value[i];
		}
		mask<<=1;
	}
	return result;
}


//#define PRINT

int main (int argc, char * const argv[]) {
//	std::stringstream input;
//	input<< "2\n \
//5\n \
//1 2 3 4 5\n \
//3\n \
//3 5 6";
	
	std::ifstream input("/Users/Chen/Downloads/C-small-attempt0.in");
	std::ofstream ofile("output");
	
	
	int inputCount;
	input >> inputCount;
	std::cout<< "inputCount:"<< inputCount<< std::endl;
	
	std::string result;file:
	input.get();	// \n
	
	for(int c=0;c< inputCount;c++){
		std::string s;
		std::getline(input, s);
		int candyCount = atoi(s.c_str());

		std::getline(input, s);
//		std::cout<< "line: "<< s<< std::endl;

		std::vector< std::string > list = tokenize(s, " ");
		std::vector< int > value;
		for(int i=0;i< candyCount;i++){
			value.push_back(atoi(list[i].c_str()));
		}

		unsigned long long select = 1;
		unsigned long long limit = (1<< candyCount) -1;
//		std::cout<< "limit: "<< limit<< std::endl;

		unsigned long long max = 0;
		while(select< limit){
			unsigned long long s = sum(value, select);
			unsigned long long v1 = _xor(value, select);
			unsigned long long v2 = _xor(value, ~select);

//			std::cout<< "v1: "<< v1<< std::endl;
//			std::cout<< "v2: "<< v2<< std::endl;
			if(v1 == v2
			   && max < s)
			{
				max = s;
			}
			select++;
		}
		// -------------------------------------------------		
//		std::string combined = combine(invoke, combineList, oppos);
		
		// -------------------------------------------------
		ofile.setf(ios::fixed, ios::floatfield);
		ofile.precision(8);
		
		//		ofile<< "Case #"<< c+1<< ": "<< second<< endl;
		std::stringstream ss;
		ss<< "Case #"<< c+1<< ": ";
		if(max == 0){
			ss<< "NO";
		}else{
			ss<< max;
		}
		ss<< "\n";
//		for(int j=0;j< combined.length();j++){
//			if(j>0){
//				ss<< ", ";
//			}
//			ss<< combined[j];
//		}
//		ss<< "]\n";
		std::cout<< ss.str();
		ofile<< ss.str();
		
	}
    return 0;
}

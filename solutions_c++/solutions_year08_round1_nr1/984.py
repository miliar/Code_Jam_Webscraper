#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <list>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
#include <algorithm>

using namespace std;

int calc(vector<int> x, vector<int>y, int nowValue)
{
	if(x.size() == 0)return nowValue;
	int i1 = x.at(0) * y.at(y.size()-1);
	int i2 = y.at(0) * x.at(y.size()-1);
	int minV = min(i1, i2);
	if(i1 < i2)
	{
		x.erase(x.begin());
		y.erase(y.end()-1);
	}else{
		y.erase(y.begin());
		x.erase(x.end()-1);
	}

	return calc(x, y, nowValue + minV);
}


int main(int argc, char **argv){
	int T;
	string buff;
	vector<string> nodes;
	ifstream ifs(argv[1]);
	
	getline(ifs, buff);
	T = boost::lexical_cast<int>(buff);

	for(int t=0; t<T; t++)
	{
		int value = 0;
		// read
		getline(ifs, buff);
		int n = boost::lexical_cast<int>(buff);
		vector<int> x(n);
		vector<int> y(n);
		nodes.clear();
		getline(ifs, buff);
		boost::algorithm::split( nodes, buff, boost::is_any_of("\t ") );
		for(int i=0; i<n; i++)x.at(i) = boost::lexical_cast<int>(nodes[i]);
		nodes.clear();
		getline(ifs, buff);
		boost::algorithm::split( nodes, buff, boost::is_any_of("\t ") );
		for(int i=0; i<n; i++)y.at(i) = boost::lexical_cast<int>(nodes[i]);

		// sort
		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		/*
		cout << "target" << endl;
		for(int i=0; i<n; i++)cout << " " << x.at(i);
		cout << endl;
		for(int i=0; i<n; i++)cout << " " << y.at(i);
		cout << endl;
		*/

		// calc
		int retValue = calc(x,y, 0);

		// output
		cout << "Case #" << t+1 << ": " << retValue << endl;
	}

	return 0;
}

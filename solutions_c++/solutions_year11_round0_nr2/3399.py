// CodeJam2011R1B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <sstream>
#include <map>

using std::vector;
using std::string;
using std::map;
using std::pair;
using std::make_pair;
//using std::priority_queue;
using std::cin;
using std::cout;
using std::endl;
using std::istringstream;


int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream ifstr;
	std::ofstream ofstr;
	ifstr.open("C://Users//Simon//College//CodeJam11//12//B-large.in");
	ofstr.open("C://Users//Simon//College//CodeJam11//12//outtest.txt");

	int n;
	ifstr>>n;
	cout<<n<<endl;
	for(int i = 0; i < n; ++i){
		int combos;
		ifstr>>combos;
		map<pair<char,char>,char> cos;
		for(int j = 0; j < combos; j++){	//map 3rd char with 1,2 and 2,1
			string ln;
			ifstr>>ln;
			pair<char,char> t = make_pair(ln[0],ln[1]);
			cos[t] = ln[2];
			t = make_pair(ln[1],ln[0]);
			cos[t] = ln[2];
		}
		int clashes;
		ifstr>>clashes;
		vector<pair<char,char>> clas;
		for(int j = 0; j < clashes; j++){		//map clashes to eachother
			string ln;
			ifstr>>ln;
			pair<char,char> t = make_pair(ln[0],ln[1]);
			clas.push_back(t);
			t = make_pair(ln[1],ln[0]);
			clas.push_back(t);
		}

		int len;
		ifstr>>len;
		string line;		//read line
		ifstr>>line;

		vector<char> res;
		for(string::const_iterator it = line.begin(); it != line.end(); ++it){
			res.push_back(*it);
			int x = res.size();
			if(x>1){		//check combos
				pair<char,char> t = make_pair(res[x-2], res[x-1]);
				map<pair<char,char>,char>::iterator mit = cos.find(t);
				if(mit != cos.end()){
					res.pop_back();
					res.pop_back();
					res.push_back(mit->second);
					--x;
				}
			}
			
			if(x>1){		//check clashes
				bool clear = 0;
				for(vector<char>::const_iterator vit = res.begin(); !clear && vit != res.end()-1; ++vit){
					for(vector<pair<char,char>>::const_iterator vpit = clas.begin(); vpit != clas.end(); ++vpit){
						if(vpit->first == *vit && vpit->second == res[x-1]){
							clear = 1;
						}
					}
				}
				if(clear) res.clear();
			}
		}
		ofstr<<"Case #"<<i+1<<": [";
		if(res.size()>0){
			for(vector<char>::const_iterator vit = res.begin(); vit != res.end()-1; ++vit){
				ofstr<<*vit<<", ";
			}
			ofstr<<*(res.end()-1);
		}
		ofstr<<"]"<<endl;
	}

	ifstr.close();
	ofstr.close();

	cout<<"done"<<endl;
	int exit;
	cin>>exit;
	return 0;
}


#include <iostream>
#include <string>
#include <list>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
	filebuf ifb;
	ifb.open ("B-large.in",ios::in);
	istream min(&ifb);
	//istream min(min);
	
	filebuf ofb;
	ofb.open ("B-large.out.txt",ios::out);
	ostream mout(&ofb);
	//ostream mout(mout);
	
	int t;
	min >> t;
	int i, j;
	for(i = 0; i < t; i++){
		string line;
		min >> line;
		mout << "Case #" << i+1 << ": ";
		list<int> int_list;
		for(j = 0; j < line.size(); j++){
			int_list.push_back(line[j]-'0');
		}
		if( next_permutation(int_list.begin(),int_list.end()) ){
			list<int>::iterator it = int_list.begin();
			for(; it != int_list.end(); it++)
				mout << *it;
			mout << endl;
		}
		else{
			int_list.sort();
			
			//for(list<int>::iterator it = int_list.begin(); it != int_list.end(); it++)	mout << *it;      mout << endl;
			
			list<int>::iterator it = int_list.begin();
			list<int>::iterator first;
			for(; it != int_list.end(); it++){
				if(*it != 0){
					first = it;
					break;
				}
			}
			it = int_list.begin();
			int t = *first;
			*first =*it;
			*it = t;
			it++;
			
			//for(list<int>::iterator it = int_list.begin(); it != int_list.end(); it++)	mout << *it;      mout << endl;
			
			int_list.insert(it,0);
			it = int_list.begin();
			for(; it != int_list.end(); it++)
				mout << *it;
			mout << endl;
		}
	}
	
	return 0;
}

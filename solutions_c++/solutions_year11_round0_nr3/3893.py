/*
 * magicka.cpp
 *
 *  Created on: 2011-5-7
 *      Author: sky
 */
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
using namespace std;
void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    string::size_type pos     = str.find_first_of(delimiters, lastPos);
    while (string::npos != pos || string::npos != lastPos)
    {
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}
void readline(string line,vector<int> &list){
	vector<string> temp;
	Tokenize(line,temp," ");
	for(int i=0;i<temp.size();i++){
		int tempint=atoi(temp[i].c_str());
		list.push_back(tempint);
	}
}
inline bool compare(int a, int b){return (a>b);}
void analyze(vector<int> &list){
	int store[21]={0};
	vector<vector <int> > newlist;
	sort(list.begin(),list.end(),compare);
	for(int i=0;i<list.size();i++){
		vector<int> temp;
		for(int j=0;j<21;j++){
			if((list[i])&(1<<j)) {
				temp.push_back(j);
				store[j]++;
			}
		}
		newlist.push_back(temp);
	}
	for(int i=0;i<21;i++){
		if(store[i]%2==1){cout<<"NO"<<endl;return;}
	}
	long long int total=0;
	for(int i=0;i<list.size()-1;i++){
		total+=list[i];

	}
	cout<<total<<endl;
	return;
}


int main(){
	ifstream infile("new");
	string line;
	int linenumber=0;
	int candynumber=0;
	int casenumber=1;
	while(getline(infile,line)){
		if(!linenumber){linenumber++;continue;}
		if(linenumber%2==1){
			candynumber=atoi(line.c_str());
			linenumber++;
			continue;
		}
		if(linenumber%2==0){
			vector< int > list;
			readline(line,list);
			linenumber++;
			cout<<"Case #"<<casenumber<<": ";
			analyze(list);
			casenumber++;
			continue;
		}

	}

	return 1;
}

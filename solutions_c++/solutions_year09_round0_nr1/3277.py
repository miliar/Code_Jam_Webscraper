#ifndef __PARSER_HPP__
#define __PARSER_HPP__

#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
class Parser{

private:

	fstream fs;
	
public:
	typedef list<string> StringList;
	typedef list<int> IntList;

	
	Parser(string filename){
		fs.open(filename.c_str(), fstream::in);
	}
	
	~Parser(){
		fs.close();
	}
	
	
	static StringList split(string src){
		char c;
		StringList result;

		stringstream ss;
		unsigned int i;
		bool save=false;
		for(i=0;i<src.size();i++){
			c = src.at(i);
			if(c == ' ' || c == '\t'){
				string 	s = ss.str();
					if(s.size() != 0){
						save=true;
						result.push_back(s);
						ss.str("");
					}
			}else{
				save=false;
				ss << c;
			}
		}

		if(!save){
			result.push_back(ss.str());
		}
	
		return result;		
	}
	
	
	static string trim(string src){
		StringList list = split(src);
		StringList::iterator it; 
			
		stringstream ss;
		for(it=list.begin();it!=list.end();it++){
			ss << *it << " ";
		}
		
		string result = ss.str();
		unsigned int size = result.size();
		if(size != 0){
			result.resize(size-1);
		}
	
		return result;
	}

	int getInt(){
		int n;
		fs >> n;
		return n;
	}
	
	
	StringList getStringList(){
		return split(getLine());
	}
	
	
	string getLine(){
		string line;
		while(getline(fs, line)){
			if(line != ""){
				return line;
			}
		}	
	
		return "";
	}
	
		
	string getTrimLine(){
		return trim(getLine());
	}	
	
};

#endif

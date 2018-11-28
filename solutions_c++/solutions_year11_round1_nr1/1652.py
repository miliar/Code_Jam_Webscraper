#ifndef HELPER_H
#define HERPER_H
#include <string>
using namespace std;
bool split(string& str,char token,vector<string>& v_str) {
//this fuction is for splitting the whole line of command into sections, each section should be divided by a single given charachter
//typically, when processing a command the token character should be space (' ') and when processing a parameter group the toke character should be comma (',')
	int str_count=0;	//number of sub strings
	string temp="";		//temp sub string storage
//	tolower(str);		//change all charachters into lower case, so that commands are not case sensitive

	for (int i=0;i<str.size();++i) {
		if (str[i]==';') {
			if (!temp.empty()) {
				v_str.push_back(temp);
				++str_count;
				temp.clear();
				v_str.push_back(";");
				break;
			} else {
				v_str.push_back(";");
				break;
			}
		} else if (str[i]!=token) {
			temp=temp+str[i];
		} else {					//str[i]==token
			if (!temp.empty()) {
				v_str.push_back(temp);
				temp.clear();
				++str_count;
			}
		}
	}
	if (!temp.empty()) {
		v_str.push_back(temp);
		++str_count;
		temp.clear();
	}
	return true;
}

double str_int(const string &str){
	double num=0;
	for(string::const_iterator it=str.begin();it!=str.end();++it){//the original "for(string::iterator it=str.begin();it!=str.end();++it)" is erronous. Check if this one works!
		if(*it>=48 && *it<=57)	//ASCII '0'=0x30=48 ; '9'=0x39=57
			num=num*10+(*it)-48;
		else{
			cout<<"This is an error message generated in Helper_h.h\nYou are seeing this because the \"int str_int(const string &str)\"\nfunction ws expecting a numeric parameter while the program sent something else."<<endl;
			return 0;
		}
	}//for(string::size_type i=0;i<str.size();i++)
	return num;
}//int str_int(string str)

#endif
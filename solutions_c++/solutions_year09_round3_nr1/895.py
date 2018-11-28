#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
using namespace std;

int main()
{
	int tCase;
	cin >> tCase;

	map<int, char> dtc;

	for(int i=0; i < 10; ++i)
		dtc[ i ] = '0'+i;
	for(int i=0; i < 6; ++i)
		dtc[ i+10 ] = 'a'+i;

	for(int _case=1; _case <= tCase; ++_case){

		string str;
		cin >> str;
		int strSize = (int)str.size();
		
		set<char> cc;
		for(int i=0; i < strSize; ++i)
			cc.insert(str[i]);

		int minDigit = (int)cc.size();
		if ( minDigit == 1 ) 
			minDigit += 1;

		map<char,int> mapping;

		int num=0;
		mapping[str[0]]=1;
		for(int i=1; i < strSize; ++i){
			if( mapping.find( str[i] ) == mapping.end()){
				mapping[ str[i] ] = num++;
				if( num==1 ) num++;
			}
		}

		string newStr="";
		for(int i=0; i < strSize; ++i){
		//	cout << str[i] << " " << mapping[str[i]] << " " <<  dtc[ mapping[str[i]] ] << endl;
			newStr += (dtc[ mapping[str[i]] ]);
			newStr += " ";
		}

		//cout << newStr << endl;

		__int64 result=0;
		istringstream is(newStr);
		string digit;
		int index = strSize-1;

		while( is >> digit ){
			int num = atoi(digit.c_str());
			__int64 tmp=1;
			for(int i=index; i > 0; --i)
				tmp *= (__int64)minDigit;
			tmp *= (__int64)num;
			result += tmp;
			index--;
		}
		cout << "Case #" << _case << ": " << result << endl;

		
	}
	

	return 0;
}

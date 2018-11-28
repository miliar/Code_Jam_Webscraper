#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cstring>

int main()
{
	using namespace std;
	const int chars = 26;
	char input_char[chars];
	char output_char[chars];
	const int num = 3;
	string input_line[num] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string output_line[num] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up"};
	
	for( int i=0 ; i<=chars ; ++i){
		input_char[i] = i + 'a';
		output_char[i] = '\0';
	}
	
	output_char[ 'a' - 'a'] = 'y';
	output_char[ 'o' - 'a'] = 'e';
	output_char[ 'z' - 'a'] = 'q';
	
	
	for( int i=0 ; i<num ; ++i){
		int length = static_cast<int>( min( input_line[i].length() ,output_line[i].length()) );
		
		for( int j=0 ; j<length ; ++j){
			if( input_line[i][j] == ' ')
				continue;
			if( input_line[i][j] == '\n')
				break;
			output_char[ input_line[i][j] - 'a'] = output_line[i][j];
		}
	}
	
	{
		set<char> charset;
		map< char ,int> output_char_map;
		for( int i=0 ; i<chars ; ++i){
			charset.insert( i + 'a');
			output_char_map.insert( map< char ,int>::value_type( output_char[i] ,i));
		}
		map< char ,int>::iterator it = output_char_map.begin();
		while( it != output_char_map.end()){
			if( it->first != '\0'){
				set<char>::iterator it2 = charset.find( it->first);
				charset.erase( it2);
				output_char_map.erase( it++);
				continue;
			}
			++it;
		}
		
		it = output_char_map.begin();
		set<char>::iterator it2 = charset.begin();
		output_char[ it->second] = *it2;
		
	}
	
	
	stringstream ss;
	string line;
	int line_num;
	
	getline( cin ,line);
	line_num = atoi(line.c_str());
	//cout << line_num << endl;
	for( int i=0 ; i<line_num ; ++i){
		getline( cin ,line);
		int length = line.length();
		cout << "Case #" << i+1 << ": ";
		for( int j=0 ; j<length ; ++j){
			if( line[j] == ' '){
				cout << line[j];
			}
			else{
				cout << output_char[ line[j] - 'a'];
			}
		}
		cout << endl;
	}
	
	
	
	return 0;
}

		
	
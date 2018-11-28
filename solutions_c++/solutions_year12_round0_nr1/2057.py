//============================================================================
// Name        : speaking_in_tongues.cpp
// Author      : Yoram Versluis
// Description : Speaking in tongues assignment
//============================================================================
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <algorithm>


using namespace std;

typedef map<char, char> mapType;
mapType translationMap;

void feedKnowledge(const std::string& input, const std::string& translation) {

	assert(input.size() == translation.size());

	for (size_t i = 0; i < input.size();i++)
	{
		translationMap[translation[i]] = input[i];
	}
}


char translate(char c)
{
	mapType::iterator it = translationMap.find(c);
	if (it!=translationMap.end())
		return it->second;
	else if (c==' ')
		return c;

	assert(false);
}

int main(int argc, char **argv) {

	if (argc < 2) {
		cerr << "Usage: " << argv[0] << " <input_file>" << endl;
		return 1;
	}

	ifstream input(argv[1]);
	if (!input.is_open())
	{
		cerr <<  "error opening " << argv[1] << endl;
		return 1;
	}


	//feed knowledge from the samples
	feedKnowledge("a zoo","y qee");
	feedKnowledge("our language is impossible to understand","ejp mysljylc kd kxveddknmc re jsicpdrysi");
	feedKnowledge("there are twenty six factorial possibilities","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	feedKnowledge("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv");

	translationMap['z'] = 'q';
	cerr << "Translation map size: " << translationMap.size() << endl;

	//just for checking if our translation map is usable
	assert(translationMap.size() == 27);
	set<char> testSet;
	for(mapType::iterator it=translationMap.begin(); it != translationMap.end(); ++it)
	{
		testSet.insert(it->second);
	}
	assert(testSet.size()==27);

	//now the real work
	int lines=0;

	char buf[200];

	input.getline(buf,sizeof(buf));
	lines = atoi(buf);

	cerr << "Lines: " << lines << endl;

	string line;
	string outStr;
	int i=0;
	while(input.good() && i < lines){
		i++;
		input.getline(buf, sizeof(buf));
		line.assign(buf);
		cout << "Case #" << i << ": ";
		transform(line.begin(),line.end(),line.begin(), translate);
		cout << line << endl;

	}

	cerr<< "Lines translated" << i << endl;
	return 0;
}

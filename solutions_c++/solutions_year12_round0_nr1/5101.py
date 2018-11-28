// SpeakingInTongues.cpp : Defines the entry point for the console application.
//

#include <map>
#include <iostream>
#include <cstring>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	std::map<char,char> Googlerese;
	const char *keys =	"ejp mysljylc kd kxveddknmc re jsicpdrysi"
						"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
						"de kr kd eoya kw aej tysr re ujdr lkgc jv"
						"y qee"
						"z";

	const char *values =	"our language is impossible to understand"
							"there are twenty six factorial possibilities"
							"so it is okay if you want to just give up"
							"a zoo"
							"q";
	
	int size = strlen(keys);
	for(const char *k = keys, *v = values; k != (keys+size);k++,v++)
	{
		Googlerese[*k] = *v;

	}
	
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	int N;
	in>>N;
	string line;
	getline(in,line);
	for(int i=0;i<N;i++)
	{
		getline(in,line);
		out<<"Case #"<<i+1<<": ";
		for(string::iterator it = line.begin(); it != line.end(); it++)
		{
			out<<Googlerese[*it];
		}
		out<<endl;
	}
	return 0;
}


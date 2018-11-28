//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char transfer(char source)
{
	char map[26]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char target;
	if (source==' ')
	target=' ';
	else
	{
		target=map[(int)source-97];
	}
	
	return target;
}

//calculate the target string

string target(string source_language)
{
	
	string target_language;
	
	//
	for (int i=0;i<source_language.length();i++)
	{
		target_language+=transfer(source_language[i]);
	}

		return target_language;
}

int main()
{   
	ifstream fin("A-small-attempt0.in");
	//ifstream fin("A-small-practice.in");
	//ifstream fin("A-large-practice.in");
	int N;
	fin>>N;
	ofstream fout("A-small-attempt0.out");
	//ofstream fout("A-small-practice.out");
	//ofstream fout("A-large-practice.out");	
	
	
	string source_language;
	string target_language;
	
	
    for (int i=0; i<=N;i++)
    {
        getline(fin,source_language);
		target_language=target(source_language);
		if (i)
		fout<<"Case #"<<i<<": "<<target_language<<endl;
    }

	/*
	for (int n=1;!fin.eof();n++)
	{
		fin>>source_language;
		
		
	}
	
	*/
	/*
	string source_language="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string target_language=target(source_language);
	cout<<target_language;
	*/
	return 0;
}
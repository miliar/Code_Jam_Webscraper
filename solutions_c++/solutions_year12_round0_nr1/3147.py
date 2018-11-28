#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;

struct keymap{
	char value;
};

class Dictionary{
private:
	keymap dictionary[26];
public:
	void initializeDict()
	{
		string str1("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z");
		string str2("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a o z q");

		int position = str1.find(" ");
		while(position != string::npos)
		{
			str1.replace(position,1,"");
			position = str1.find(" ",position+1);
		}

		position = str2.find(" ");
		while(position != string::npos)
		{
			str2.replace(position,1,"");
			position = str2.find(" ",position+1);
		}

		for(int i=0;i<(unsigned)str2.length();i++)
		{
			dictionary[((int)str1.at(i))-97].value=str2.at(i);
		}
	}
	char getKey(char a)
	{
		int index = (int)a - 97;
		if(index <0 || index >=26)
		{
			return a;
		}
		else
		{
			int test = dictionary[index].value - 97;
			if( test <0 || test>=26)
				return a;
			else
				return dictionary[index].value;
		}
	}
};

void main ()
{
	ifstream input("A-small-attempt2.in",ios::in);
	ofstream output("A-small-attempt2.out",ios::out);

	string case1;
	getline(input,case1);

	int cases = atoi(case1.c_str());

	Dictionary dict;
	dict.initializeDict();

	if( cases < 1 || cases >30)
	{
		output << "Invalid Number of test cases";
	}else
	{
		int solvedCases=0;
		while(solvedCases < cases)
		{
			string str;
			
			getline(input,str);
			string::const_iterator iterator1 = str.begin();
			output<<"Case #"<<solvedCases+1<<": ";
			while ( iterator1 != str.end() )                      
			{                                                         
				output << dict.getKey(*iterator1); // dereference iterator to get char
				iterator1++; // advance iterator to next char          
			}
			output << endl;
			solvedCases++;
		}
	}
	input.close();
	output.close();

	//for (int i =0;i<26;i++)
	//	cout <<(char)(i+97) << ":"<<dict.getKey((char)(i+97)) << endl;
}

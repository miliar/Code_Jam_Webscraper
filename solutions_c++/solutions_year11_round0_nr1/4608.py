#include <iostream>
#include <fstream>
#include <conio.h>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using std::endl;
using std::vector;
using std::ifstream;
using std::cout;
using std::string;
using std::istringstream;
using std::ofstream;
using std::map;


void WriteToFile(vector<string>& solution, const string& filename)
{
	ofstream writestream;
	writestream.open(filename);
	
	vector<string>::iterator iter;
	int count = 0;
	
	for(iter=solution.begin();iter!= solution.end();++iter)
	{
		writestream << "Case #" << ++count << ": " << *iter << endl;
	}

	writestream.close();

}


vector<vector<string>> ReadFile_bottrust(string filename)
{
	ifstream readstream;
	vector<vector<string>> wordlist;

	readstream.open(filename);
	
	if(readstream.is_open() == false)
	{
		cout << "Unable to open file" << endl;
		getch();
		return wordlist;
	}

	string str;
	
	while(getline(readstream,str))
	{
		istringstream in(str);
		string s;
		vector<string> line;
		while(in>>s)
		{
			line.push_back(s);
		}
		wordlist.push_back(line);
	}
	return wordlist;
}

void increment_iter(vector<string>& seq,vector<string>::iterator& iter)
{
	if(iter != seq.end())
		++iter;
}

string calculate_bottrust(vector<string>& values)
{
	int totalcases = atoi(values[0].c_str());
	vector<string> oseq;
	vector<string> bseq;
	vector<string> actualseq;
	int totalsecs=0;
	int prevvalo = 1;
	int prevvalb = 1;
	for(int idx=1;idx<values.size();idx+=2)
	{
		int temp = atoi(values[idx+1].c_str());
		int val = 0;
		actualseq.push_back(values[idx]);
		string str;
		string final_str;
		if(values[idx] == "O")
		{
			val = temp-prevvalo;
			prevvalo = temp;
			str = "MO";
			final_str = "PO";
		}
		else
		{
			val = temp-prevvalb;
			prevvalb = temp;
			str = "MB";
			final_str = "PB";
		}
		if(val < 0)
			val = -val;

		for(int index=0;index<val;++index)
		{
			if(values[idx] == "O")
				oseq.push_back(str);
			else
				bseq.push_back(str);
		}

		if(values[idx] == "O")
				oseq.push_back(final_str);
			else
				bseq.push_back(final_str);
	}

	vector<string>::iterator oiter(oseq.begin());
	vector<string>::iterator biter(bseq.begin());
	vector<string>::iterator actualiter(actualseq.begin());
		
	while(actualiter!=actualseq.end())
	{
		if(*actualiter == "O")
		{
			if(oiter != oseq.end() && *oiter == "PO" &&  biter != bseq.end() && *biter != "PB")
					increment_iter(bseq,biter);
			while(oiter != oseq.end() && *oiter!="PO")
			{
				if(biter != bseq.end() && *biter != "PB")
					increment_iter(bseq,biter);
				increment_iter(oseq,oiter);
				if(oiter != oseq.end() && *oiter == "PO" && biter != bseq.end() && *biter != "PB")
					increment_iter(bseq,biter);
				++totalsecs;
			}
			increment_iter(oseq,oiter);
			++totalsecs;
		}
		else
		{
			if(biter != bseq.end() && *biter == "PB" && oiter != oseq.end() && *oiter != "PO")
					increment_iter(oseq,oiter);
			while(biter != bseq.end() && *biter!="PB")
			{
				if(oiter != oseq.end() && *oiter != "PO")
					increment_iter(oseq,oiter);
				increment_iter(bseq,biter);
				if(biter != bseq.end() && *biter == "PB" && oiter != oseq.end() && *oiter != "PO")
					increment_iter(oseq,oiter);
				++totalsecs;
			}
			increment_iter(bseq,biter);
			++totalsecs;
		}
	++actualiter;
	}
	
	
	char* str = new char(sizeof(int)*8+1);
	char* ch = itoa(totalsecs,str,10);
	return string(ch);
}

int main()
{
	vector<vector<string>> wordlist = ReadFile_bottrust("A-large.in");
	
	vector<string> count = wordlist[0];
	int totaltestcases = atoi(count[0].c_str());
	int currentindex = 0;
	
	vector<string> solution;
	for(int index=1;index<=totaltestcases;++index)
	{
		solution.push_back(calculate_bottrust(wordlist[index]));
	}

	WriteToFile(solution,"output.txt");
}


#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

int testCases;

using namespace std;

bool match(string word, string line, int L)
{
	string tem; stringstream s(line);
	
	for(int i=0; i<L; i++)
	{
		s >> tem;
		// cout << i << " " << word << " " << tem << endl;
		bool ok = false;
		for(int j=0; j<tem.length(); j++)
		{
			if(tem[j] == word[i]) ok = true;
		}
		
		if(!ok) return false;
	}
	
	return true;
			
}


int main(void)
{
	ifstream in("B-small.in");
	ofstream out("B-output.out");
	string line;
	
	int L, D, N;
	in >> L >> D >> N;
	
	vector <string> words;
	
	for(int i=0; i<D; i++) 
	{
		in >> line;
		words.push_back(line);
	}
	
	for(int i=0; i<N; i++)
	{
		in >> line;
		bool inside = false;
		if(line[0]=='(') inside = true;
		
		for(int j=1; j<line.size(); j++)
		{
			if(line[j]=='(') inside = true;
			if(line[j]==')') inside = false;
			
			if((line[j]-'a'>=0&&line[j]-'a' <=25)&&(line[j-1]-'a'>=0&&line[j-1]-'a'<=25)&&!inside)
			{
				line = line.substr(0,j) + "()" + line.substr(j);
			}
		}
		
		for(int j=0; j<line.size(); j++)
		{
			if(line[j]=='('||line[j]==')') line[j] = ' ';
		}
		
		
		int ret = 0;
		for(int j=0; j<words.size(); j++)
		{
			if(match(words[j],line, L)) ret++;
		}
		
	out << "Case #" << i+1 << ": " << ret << endl;;
	}
	


}
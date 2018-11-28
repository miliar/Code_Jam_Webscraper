#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
	fstream infile("B-large.in");
	fstream outfile("B-large.out");
	int T;
	infile >> T;
	int index = 1;
	while(T)
	{
		vector<string> comRules;
		vector<string> oppRules;
		int numCom,numOpp;
		infile >> numCom;
		while(numCom)
		{
			string str;
			infile >> str;
			comRules.push_back(str);
			numCom--;
		}
		infile >> numOpp;
		while(numOpp)
		{
			string str;
			infile >> str;
			oppRules.push_back(str);
			numOpp--;
		}

		vector<char> chars;
		int num;
		infile >> num;
		while(num)
		{
			char ch;
			infile >> ch;
			if(chars.empty())
				chars.push_back(ch);
			else
			{
				bool isCom = false;
				char t = chars[chars.size()-1];
				for(int i = 0; i < comRules.size(); i++)
				{
					string rule = comRules[i];
					if((rule[0] == t && rule[1] == ch) || (rule[0] == ch && rule[1] == t))
					{
						isCom = true;
						chars.pop_back();
						chars.push_back(rule[2]);
						break;
					}
				}

				bool isOpp = false;
				if(!isCom)
				{
					for(int i = 0; i < oppRules.size(); i++)
					{
						char oppChar = ' ';
						string rule = oppRules[i];
						if(rule[0] == ch)
							oppChar = rule[1];
						if(rule[1] == ch)
							oppChar = rule[0];
						if(oppChar != ' ')
						{
							for(int j = chars.size()-1; j >= 0; j--)
							{
								if(chars[j] == oppChar)
								{
									isOpp = true;
									break;
								}
							}

							if(isOpp)
								chars.clear();
						}					
					}	
				}
				
				if(!isCom && !isOpp)
					chars.push_back(ch);
			}
			num--;
		}

		outfile << "Case #" << index << ": " << "[";
		for(int k = 0; k < chars.size(); k++)
		{
			if(k != chars.size()-1)
				outfile << chars[k] << ", ";
			else
				outfile << chars[k];
		}
		outfile << "]" << endl;

		index++;
		T--;
	}
	infile.close();
	outfile.close();
}
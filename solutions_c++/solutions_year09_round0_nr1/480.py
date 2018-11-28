#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int Count(const vector<string> & words, const vector<string> & tokens)
{
	int answer = 0;
	for(int i = 0; i < words.size(); i++)
	{
		int match = 1;
		for(int j = 0; j < tokens.size() && match; j++)
			match = tokens[j].find(words[i][j]) != string::npos;
		answer += match;
	}
	return answer;
}

int main()
{
	string buf, tmp;
	int l, d, n;
	ifstream in("in.txt");
	in >> l >> d >> n;
	vector<string> tokens;
	vector<string> words(d);	
	for(int i = 0; i < d; i++)
		in >> words[i];
	for(int i = 0; i < n; i++)
	{
		in >> buf;
		tokens.clear();
		for(int j = 0; j < buf.size(); j++)
			if(buf[j] == '(')		
			{
				j++;
				tmp.clear();
				while(buf[j] != ')')
					tmp += buf[j++];
				tokens.push_back(tmp);
			}
			else
			{
				tokens.push_back("");
				tokens.back() += buf[j];
			}
		cout << "Case #" << i + 1 <<": " << Count(words, tokens) << endl;
	}
	return 0;
}
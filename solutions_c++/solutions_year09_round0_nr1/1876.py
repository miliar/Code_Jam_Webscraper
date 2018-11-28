#include<string>
#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>

using namespace std;

class WordInfo
{
public:
	WordInfo() {}
	WordInfo(int index, const string & content): index(index), content(content) {}
	int index;
	string content;
};

bool wordInfoPtLesser (WordInfo * const &a, WordInfo * const &b)
{
   return a->index < b->index;
}

class WordInfoPtLess
{
public:
	bool operator()(WordInfo * const &a, WordInfo * const &b) const
	{
		 return a->index < b->index;
	}
};


typedef vector<WordInfo*> WordInfoPtVec;
typedef map<char, WordInfoPtVec> CharDic;

class Data
{
public:
	Data(string filename);
	void ComputWordSet(void);
	void SaveResult(string filename);

private:
	vector<CharDic> dicVec;
	vector<WordInfo> wordVec;
	vector<string> caseVec;
	vector<WordInfoPtVec> resultVec;
};

Data::Data(string filename)
{
	ifstream in(filename.c_str());
	int wordLen, dicWordsCount, casesCount;
	in>>wordLen>>dicWordsCount>>casesCount;
	this->dicVec.resize(wordLen);
	this->wordVec.resize(dicWordsCount);
	string str;
	for(int i=0; i<dicWordsCount; i++)
	{
		in>>str;
		wordVec[i].index = i;
		wordVec[i].content = str;
		for(int j=0; j<wordLen; j++)
		{
			if(dicVec[j].count(str[j]))
			{
				dicVec[j][str[j]].push_back(&wordVec[i]);
			}
			else
			{
				dicVec[j].insert(CharDic::value_type(str[j], WordInfoPtVec(1, &wordVec[i])));
			}
		}
	}
	this->caseVec.resize(casesCount);
	for(int i=0; i<casesCount; i++)
	{
		in>>caseVec[i];
	}
	this->resultVec.resize(casesCount);
}

void Data::ComputWordSet()
{
	for(vector<string>::size_type caseIndex=0; caseIndex < this->caseVec.size(); caseIndex++)
	{
		string &currentString = this->caseVec[caseIndex];
		bool isInBra = false;
		int charPos = 0;
		for(string::size_type strIndex = 0; strIndex < currentString.length(); strIndex++, charPos++)
		{
			if(currentString[strIndex] == '(')
			{
				strIndex++;
				set<WordInfo*, WordInfoPtLess> possibleSet;
				while(currentString[strIndex] != ')')
				{
					WordInfoPtVec &tempPossibleWords = this->dicVec[charPos][currentString[strIndex]];
					possibleSet.insert(tempPossibleWords.begin(), tempPossibleWords.end());
					strIndex++;
				}
				if(charPos == 0)
				{
					this->resultVec[caseIndex].insert(this->resultVec[caseIndex].end(), possibleSet.begin(),possibleSet.end());
				}
				else
				{
					WordInfoPtVec newPossibleWords;
					set_intersection(
						resultVec[caseIndex].begin(),resultVec[caseIndex].end(),
						possibleSet.begin(),possibleSet.end(),
						inserter(newPossibleWords, newPossibleWords.begin()), wordInfoPtLesser);
					this->resultVec[caseIndex] = newPossibleWords;
				}
			}
			else
			{
				WordInfoPtVec &possibleWords = this->dicVec[charPos][currentString[strIndex]];
				if(charPos == 0)
					this->resultVec[caseIndex] = possibleWords;
				else
				{
					WordInfoPtVec newPossibleWords;
					set_intersection(
						resultVec[caseIndex].begin(),resultVec[caseIndex].end(),
						possibleWords.begin(),possibleWords.end(),
						inserter(newPossibleWords, newPossibleWords.begin()), wordInfoPtLesser);
					this->resultVec[caseIndex] = newPossibleWords;
				}
			}
		}
	}
}

void Data::SaveResult(string filename)
{
	ofstream out(filename.c_str());
	for(vector<string>::size_type caseIndex=0; caseIndex < this->caseVec.size(); caseIndex++)
	{
		out<<"Case #"<<caseIndex+1<<": "<<this->resultVec[caseIndex].size()<<endl;
	}
}

int main(int argc, char *argv[])
{
	Data data("A-large.in");
	data.ComputWordSet();
	data.SaveResult("A-large.out");
	return 0;
}
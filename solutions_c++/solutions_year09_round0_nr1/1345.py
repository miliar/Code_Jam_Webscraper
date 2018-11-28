#include<string>
#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<algorithm>

using namespace std;

class Data
{
public:
	Data(string filename);
	void ComputResult(void);
	void SaveResult(string filename);

private:
	int wordLen;
	vector<string> wordVec;
	vector<string> caseVec;
	vector<int> resultVec;
};

Data::Data(string filename)
{
	ifstream in(filename.c_str());
	int dicWordsCount, casesCount;
	in>>this->wordLen>>dicWordsCount>>casesCount;
	this->wordVec.resize(dicWordsCount);
	this->caseVec.resize(casesCount);
	string str;
	for(int i=0; i<dicWordsCount; i++)
	{
		in>>this->wordVec[i];
	}
	this->caseVec.resize(casesCount);
	for(int i=0; i<casesCount; i++)
	{
		in>>caseVec[i];
	}
	this->resultVec.resize(casesCount);
}

void Data::ComputResult()
{
	string::size_type wordIndex;
	string::size_type caseStringIndex;
	bool isPossible;

	for(vector<string>::size_type caseIndex = 0; caseIndex < this->caseVec.size(); caseIndex++)
	{
		string & caseString = this->caseVec[caseIndex];
		for(vector<string>::iterator wordIter = this->wordVec.begin(); wordIter != this->wordVec.end(); wordIter++)
		{
			string & wordString = *wordIter;
			wordIndex = 0;
			caseStringIndex = 0;
			isPossible = true;
			for(;caseStringIndex < caseString.length(); caseStringIndex++, wordIndex++)
			{
				if(caseString[caseStringIndex] == '(')
				{
					caseStringIndex++;
					bool match = false;
					while(caseString[caseStringIndex] != ')')
					{
						if(match == false && caseString[caseStringIndex] == wordString[wordIndex])
							match = true;
						caseStringIndex++;
					}
					if(!match)
					{
						isPossible = false;
						break;
					}
				}
				else
					if(caseString[caseStringIndex] != wordString[wordIndex])
					{
						isPossible = false;
						break;
					}
			}
			if(isPossible)
				this->resultVec[caseIndex]++;
		}
		cout<<caseIndex<<endl;
	}
}

void Data::SaveResult(string filename)
{
	ofstream out(filename.c_str());
	for(vector<int>::size_type resultIndex=0; resultIndex < this->resultVec.size(); resultIndex++)
	{
		out<<"Case #"<<resultIndex+1<<": "<<this->resultVec[resultIndex]<<endl;
	}
}

int main(int argc, char *argv[])
{
	Data data("A-large.in");
	data.ComputResult();
	data.SaveResult("A-large.out");
	//Data data("A-small-attempt1.in");
	//data.ComputResult();
	//data.SaveResult("A-small-attempt1.out");
	return 0;
}
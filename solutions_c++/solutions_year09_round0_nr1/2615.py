#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class PrintString
{
public:
	void operator () (string elem) const
	{
		cout << elem << endl;	
	}
};


class Analyzer 
{
private:
	void splinter(vector<string> &EveryPosWords,string TestWord)
	{
		EveryPosWords.clear();

		string tmp = "";
		int pos;
		bool HasLeftCase = false;
		for (int i=0;i<TestWord.length();++i)
		{
			if (TestWord[i] == '(')
			{
				HasLeftCase = true;
				tmp = "";
			}
			else if (TestWord[i] == ')')
			{
				HasLeftCase = false;
				EveryPosWords.push_back(tmp);
			}
			else
			{
				if (HasLeftCase)
				{
					tmp += TestWord[i];
				}
				else
				{
					tmp = TestWord[i];
					EveryPosWords.push_back(tmp);
				}
			}
		}

	}
	
	int Compare(vector<string> &KnowedWords,vector<string> &EveryPosWords)
	{
		int Count = 0;
		vector<string> tmpKnowedWords,ResultWords;	
		tmpKnowedWords.assign(KnowedWords.begin(),KnowedWords.end());
		
		int i=0;
		for (vector<string>::iterator iter=EveryPosWords.begin();iter!=EveryPosWords.end();++iter)
		{
			string tmp = *iter;

			string KnowedWord = tmpKnowedWords[i];
			
			bool Eql = false;
			for (int j=0;j<KnowedWord.length();++j)
			{
				Eql = false;
				for (int k=0;k<tmp.length();++k)
				{
					if (KnowedWord[j]==tmp[k])
					{
						Eql = true;
						break;
					}
				}
				if (Eql)
					KnowedWord[j] = '1';
				else
					KnowedWord[j] = '0';
			}

			tmpKnowedWords[i] = KnowedWord;
			++i;
		}

		transForm(tmpKnowedWords,ResultWords);

		string CompareStr = "";
		for (int i=0;i<WordLenth;++i)
			CompareStr += "1";

		for (vector<string>::iterator iter=ResultWords.begin();iter!=ResultWords.end();++iter)
		{
			if (*iter == CompareStr)
				Count++;
		}
		
		return Count;
	}
public:
	int WordLenth;

	Analyzer(int wordLenth):WordLenth(wordLenth)
	{
	}

	void transForm(vector<string> &From,vector<string> &To)
	{
		if (From.empty())
			return;

		int Len = From[0].length();
		To.resize(Len);	
		for (vector<string>::iterator iter=From.begin();iter!=From.end();++iter)
		{
			string tmp = *iter;
			
			for (int i=0;i<Len;++i)
			{
				To[i] += tmp[i];		
			}
		}
	}

	int Analysis(vector<string> &KnowedWords,string TestWord)
	{
		string Result;
		vector<string> EveryPosWords;
		splinter(EveryPosWords,TestWord);
		
		int SameNum = Compare(KnowedWords,EveryPosWords);

		return SameNum;
	}
};

int main(int argc, char* argv[])  
{
    if(argc != 3)  
    {  
  		cout << "Usage: AlienLanguage INPUT_FILE OUTPUT_FILE" << endl;
//        return 0;  
    }  

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	if (!fin)
    {
        cout << "Read fail!" << endl;
        return 1;  
    }


	int WordOfLength;  
	int KnowedNumber;  
	int CaseNumber; 
	
	string CaseNums;  
    std::getline(fin, CaseNums);
	int pos = CaseNums.find_first_of(" ");
	WordOfLength = atoi(CaseNums.substr(0,pos).c_str());
	CaseNums = CaseNums.substr(pos+1,CaseNums.length()-pos);
	pos = CaseNums.find_first_of(" ");
	KnowedNumber = atoi(CaseNums.substr(0,pos).c_str());
	CaseNums = CaseNums.substr(pos+1,CaseNums.length()-pos);
	CaseNumber = atoi(CaseNums.c_str());

	//cout << "Word Of Length:" << WordOfLength << " Knowed Number:" << KnowedNumber << " Case Number:" << CaseNumber << endl;

	vector<string> KownedWords;
	vector<string> TransKownedWords;
	vector<string> Cases;

	string ReadinLine;
	for (int i=0;i<KnowedNumber;++i)
	{
		getline(fin, ReadinLine);
		KownedWords.push_back(ReadinLine);		
	}
	
	for (int i=0;i<CaseNumber;++i)
	{
		getline(fin, ReadinLine);
		Cases.push_back(ReadinLine);		
	}
	
	int CasesResult;

	Analyzer analyzer(WordOfLength);
	
	analyzer.transForm(KownedWords,TransKownedWords);

	int i=1;
	for (vector<string>::iterator iter = Cases.begin();iter!=Cases.end();++iter)
	{
    	CasesResult = analyzer.Analysis(TransKownedWords,*iter);

		fout << "Case #" << i++ << ": " << CasesResult << endl;	

	}
}


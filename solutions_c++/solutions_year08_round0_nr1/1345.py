//Visual Syudio 2008 
#include<iostream>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

class STU
{
public:
	static vector<string> SearchEngines;
	static vector<bool> Used;
	static int Switches;
public:
	static void InitUsed()
	{
		for (unsigned int i=0;i<Used.size();i++)
		{
			Used[i]=0;
		}
	}
	static void InitAll()
	{
		SearchEngines.clear();
		SearchEngines.resize(0);
		Used.clear();
		Used.resize(0);
		InitUsed();
		Switches=0;
	}
	static bool Complete()
	{
		bool answer=1;
		for (unsigned int i=0;i<Used.size();i++)
		{
			answer=answer && Used[i];
		}
		return answer;
	}
	static void InsertSearchEngine(string s)
	{
		SearchEngines.insert(SearchEngines.end(),s);
		Used.insert(Used.end(),0);
	}
	static void InsertWord(string s)
	{
		for(unsigned int i=0;i<SearchEngines.size();i++)
		{
			if(s==SearchEngines[i])
			{
				Used[i]=1;
				if(Complete())
				{
					InitUsed();
					Used[i]=1;
					Switches++;
				}

				return ;
			}
		}
		throw(int());

	}
	static int GetSwitches()
	{
		return Switches;
	}

};

vector<string> STU::SearchEngines;
vector<bool> STU::Used ;

int STU::Switches=0;


void main()
{
	ofstream outFile;
	outFile.open("Out.txt",ios::out);

	ifstream inFile;
	inFile.open("In.in",ios::in);
	char TempString[101];

	int N=0;
	inFile>>N;
//	inFile.getline (TempString,101);

	for(int i=1;i<=N;i++)
	{
		STU::InitAll();
		int S=0;
		inFile>>S;
		inFile.getline (TempString,101);
		for(int j=0;j<S;j++)
		{
			inFile.getline (TempString,101);
			//if(TempString=="")throw(int());//goto Again;
//			inFile>>TempString;
			STU::InsertSearchEngine(TempString);
		}
		int Q=0;
		inFile>>Q;
		inFile.getline (TempString,101);
		for(int j=0;j<Q;j++)
		{
			inFile.getline (TempString,101);
//			inFile>>TempString;
			STU::InsertWord(TempString);
		}
		outFile<<"Case #"<<i<<": "<<STU::GetSwitches()<<endl;		
	}
	inFile.close();
	outFile.close();

}

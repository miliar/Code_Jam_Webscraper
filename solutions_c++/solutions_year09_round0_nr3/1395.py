#include<iostream>
#include <iomanip>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>

using namespace std;

class Data
{
public:
	vector<string> data;

	Data(string fileName);
	void display(void);

private:
	Data();
};

Data::Data(string fileName)
{
	ifstream in(fileName.c_str());
	string firstLine;
	getline(in, firstLine);
	istringstream firstLineStream(firstLine);
	int dataLength;
	firstLineStream >> dataLength;
	for(int i=0; i<dataLength; i++)
	{
		string line;
		getline(in, line);
		this->data.push_back(line);
	}
}

void Data::display()
{
	cout<<this->data.size()<<endl;
	for(vector<string>::iterator iter=data.begin(); iter != data.end(); iter++)
		cout<<*iter<<endl;
}


int violent_countSeq(const string & source, const string & target)
{
	const int length = target.length();
	vector<int> strPos(length);
	strPos[0] = -1;
	int counter = 0;
	int currentCharNum = 0;

	while(true)
	{
		string::size_type pos = source.find(target[currentCharNum], strPos[currentCharNum] + 1);
		if(pos == string::npos)
		{
			currentCharNum--;
			if(currentCharNum == -1)
				break;
		}
		else
		{
			strPos[currentCharNum] = pos;
			if(currentCharNum == length - 1)
			{
				counter++;
			}
			else
			{
				currentCharNum++;
				strPos[currentCharNum] = pos;
			}
		}
	}

	return counter;
}


int countSeq(const string & source, const string & target)
{
	typedef pair<int, string::size_type> SubSeqInfo; //(first: possible sequences count, second: related character position)
	typedef vector<SubSeqInfo> TargetCharInfo; //one character in target string may appear many times in source string
	
	string::size_type targetLength = target.length();
	vector<TargetCharInfo> targetCharInfoVector(targetLength);


	TargetCharInfo * pCurrenTargetCharInfo = &targetCharInfoVector[0];
	TargetCharInfo * pPreviousTargetCharInfo = NULL;
	for(vector<TargetCharInfo>::size_type targetIndex = 0; targetIndex != targetCharInfoVector.size(); targetIndex++)
	{
		TargetCharInfo * pCurrenTargetCharInfo = &targetCharInfoVector[targetIndex];
		TargetCharInfo * pPreviousTargetCharInfo = NULL;
		if(targetIndex > 0)
		{
			pPreviousTargetCharInfo = &targetCharInfoVector[targetIndex-1];
			if(pPreviousTargetCharInfo->size() == 0)
				break; // miss previous charactor. impossible to find any sequence.
		}
		
		TargetCharInfo::iterator possibleGrowPoint;
		if(targetIndex > 0)
		{
			possibleGrowPoint = pPreviousTargetCharInfo->begin();
		}
		TargetCharInfo::size_type seqGrowPt = 0; //point to previous TargetCharInfo item
		string::size_type searchPos = 0; //point to character in source string

		while(true)
		{
			string::size_type pos = source.find(target[targetIndex], searchPos);
			if(pos == string::npos)
				break;
			searchPos = pos + 1;
			if(targetIndex == 0)
				pCurrenTargetCharInfo->push_back(SubSeqInfo(1, pos));
			else
			{
				for(; possibleGrowPoint != pPreviousTargetCharInfo->end(); possibleGrowPoint++) //find possible sequences
				{
					if(pos < possibleGrowPoint->second) //first sequence break
						break;
				}
				int sequenceCount = 0;
				for(TargetCharInfo::iterator iter = pPreviousTargetCharInfo->begin();
					iter != possibleGrowPoint;
					iter++)
				{
					sequenceCount += iter->first;
					if(sequenceCount > 999999)
					{
						stringstream ss;
						string s;
						ss<<sequenceCount;
						ss>>s;
						s = s.substr(s.length() - 4);
						istringstream iss(s);
						iss>>sequenceCount;
					}
				}
				if(sequenceCount > 0)
					pCurrenTargetCharInfo->push_back(SubSeqInfo(sequenceCount, pos));
			}
		}
	}

	
	
	{
		int sequenceCount = 0;
		pCurrenTargetCharInfo = &targetCharInfoVector.back();
		for(TargetCharInfo::iterator iter = pCurrenTargetCharInfo->begin();
			iter != pCurrenTargetCharInfo->end();
			iter++)
		{
			sequenceCount += iter->first;
			if(sequenceCount > 9999)
			{
				stringstream ss;
				string s;
				ss<<sequenceCount;
				ss>>s;
				s = s.substr(s.length() - 4);
				istringstream iss(s);
				iss>>sequenceCount;
			}
		}
		return sequenceCount;
	}
}


int main(int argc, char *argv[])
{
	Data data(string("C-large.in"));
	//data.display();

	string target("welcome to code jam");
	

	fstream outputFile("C-large.out",ios::out);
	for(vector<string>::size_type i=0; i<data.data.size(); i++)
	{
		int result = countSeq(data.data[i], target);
		//int result = violent_countSeq(data.data[i], target);
		cout<<i<<": "<<result<<endl;
		outputFile<<"Case #"<<i+1<<": "<<setfill('0')<<setw(4)<<setiosflags(ios::right)<<result<<endl;
	}
}

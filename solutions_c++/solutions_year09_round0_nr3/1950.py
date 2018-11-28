#include <fstream>
#include <vector>
#include <string>
#include <assert.h>
#include <iomanip>

using namespace std;
const char *fileName = "C-small-attempt0.in";
//const char *fileName = "test.in";
const char *outFileName = "c-small.out";
ifstream inFile(fileName);
ofstream outFile(outFileName);

string welcomeString("welcome to code jam");

int FindMatchNumber(const string &inputString, const string &tplString)
{
	if (tplString.empty() || inputString.empty())
	{
		return 0;
	}
	if(inputString.size() < tplString.size())
		return 0;
	
	if (inputString == tplString)
	{
		return 1;
	}
	

	string subInputString, subTplString;

	int num = 0;

	if (tplString.size() == 1)
	{
		int ps = inputString.find(tplString[0]);
		while (ps != string::npos)
		{
			num++;

			ps = inputString.find(tplString[0], ps+1);
		}
		return num;
	}
	subTplString = tplString.substr(1);
	int pos = inputString.find(tplString[0]);
	if (pos == string::npos)
	{
		return 0;
	}
	subInputString = inputString.substr(pos);
	if (subInputString.empty())
	{
		return 0;
	}
	int idx = 0;
	while(!subInputString.empty())
	{

		subInputString = subInputString.substr(1);
		int matchNum = FindMatchNumber(subInputString, subTplString);
		if (matchNum==0)
			break;

			idx++;
			num +=  matchNum;
	
		pos = subInputString.find(tplString[0]);
		if (pos == string::npos)
		{
			break;
		}
		subInputString = subInputString.substr(pos);

	}

	return num;

}
int main()
{
	int N =0;
	assert(inFile.is_open());
	inFile >> N;
	string inputString;
	getline(inFile, inputString);

	for (int caseNum = 0; caseNum < N; caseNum++)
	{
		getline(inFile, inputString);
		int num = FindMatchNumber(inputString, welcomeString);
		if (num > 9999)
		{
			num %= 10000;
		}
		outFile << "Case #" << caseNum+1 << ": " << setw(4) << setfill('0') << num << endl; 
	}
	return 0;
}
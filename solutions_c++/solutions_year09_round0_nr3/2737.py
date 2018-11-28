#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

void partString(string str,int len){
	for(int i=0;i<=len;i++){
		cout << str[i];
	}
	cout << endl;
}

long int getPatternCount(string iStr,string pattern,int iStart, int pStart, int iLength, int pLength){
	
	if(pStart==pLength)
		return 1;

	if(iStart>=iLength)
		return 0;


	long int count=0;
	int curr_count = 0, pat_count = 0;
	
	int i=iStart;{
		if(iStr[i]==pattern[pStart]){
			if(pStart==pLength-1)
				count = count + 1;
			else{
				for(int j=i+1;j<iLength;j++){
					pat_count = getPatternCount(iStr,pattern,j,pStart+1,iLength,pLength);
					if(pat_count > 0)
						//cout << "+1" << endl;
					count = count + pat_count;
				}
			}
		}
	}

	return count;
}


void WelcomeToCodeJam(){
	string pattern="welcome to code jam";

	ifstream inputFile("C:\\Users\\nishit\\Documents\\Visual Studio 2008\\Projects\\test\\Debug\\input.txt",ios_base::in);
	ofstream outputFile("C:\\Users\\nishit\\Documents\\Visual Studio 2008\\Projects\\test\\Debug\\output.txt",ios_base::out);

	if(!inputFile.is_open())
		cout << "error opening file";

	int n;
	char buff;

	inputFile >> n >> buff;

	string inputStr;

	int iPtr,pPtr;
	int iLength, pLength;
	long int pCnt=0;
	int currIPtr,currPPtr;
	bool found(false);


	for(int i=0;i<n;i++){
		pCnt = 0;
		getline(inputFile,inputStr);

		iLength = inputStr.size();
		pLength = pattern.length();

		for(int start_i=0;start_i<inputStr.length();start_i++)
			pCnt += getPatternCount(inputStr,pattern,start_i,0,iLength,pLength);

		outputFile << "Case #" << i+1 << ": "; 
		outputFile << setw(4) << setfill('0') << pCnt%10000 << endl;

	}
	inputFile.close();
	outputFile.close();
}

int main()
{
	WelcomeToCodeJam();
	system("PAUSE");
}


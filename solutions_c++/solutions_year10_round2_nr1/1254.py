#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
#include<map>

using namespace std;
const int sizeAtt = 100;
ifstream inputFile("c:/in/Ainput.txt");

void findMkDirs(int n,int M,int CaseNum);
int main()
{
	int tCaseNums=0,i=0;
		
	inputFile>>tCaseNums;
	int numN=0,numM=0;
	string dirPath;
	

	for(i=0;i<tCaseNums;i++)
	{

		inputFile>>numN>>numM;
		findMkDirs(numN,numM,i);
	}
}
void findMkDirs(int n,int M,int CaseNum)
{
ofstream  outputFile("C:/in/Aoutput.txt",ios_base::app);
int myiter=0;
map<string,int> dirListHash;
int PosSlash=0;
string interStr,dirPath;
int count=0;

for(myiter=0;myiter<n;myiter++)
		{
			inputFile>>dirPath;
			dirListHash[dirPath]=1;
			PosSlash=dirPath.find('/',1);
			while(PosSlash != string::npos)
			{
			interStr=dirPath.substr(0,PosSlash);

			dirListHash[interStr]=1;
			PosSlash=dirPath.find('/',PosSlash+1);
			}
		}



		for(myiter=0;myiter<M;myiter++)
		{
			inputFile>>dirPath;
			if(dirListHash.count(dirPath)>0)
			{
				continue;
			}
			dirListHash[dirPath]=1;
			count++;
			PosSlash=dirPath.rfind('/');
			interStr=dirPath;
			while(PosSlash != string::npos)
			{
			if(PosSlash == 0)
			{
				break;
			}
			interStr=interStr.substr(0,PosSlash);

			if(dirListHash.count(interStr)>0)
			{
				break;
			}
			dirListHash[interStr]=1;
			count++;
			PosSlash=interStr.rfind('/');

			}
		}
		outputFile<<"Case #"<<CaseNum+1<<": "<<count<<endl;

}

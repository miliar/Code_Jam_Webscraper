#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
	ifstream inFile("B-large.in");
	ofstream outFile("B-large.out");
	//ifstream inFile("B-small-attempt1.in");
	//ofstream outFile("B-small-attempt1.out");
	//ifstream inFile("test.in");
	//ofstream outFile("test.out");
	int caseCount;
	inFile>>caseCount;
	inFile.ignore();
	for(int i=0; i<caseCount; i++)
	{
		string line;
		getline(inFile, line);
		vector<int> digitVec;
		stringstream ss;
		int j;
		for(j=0; j<line.length(); j++)
		{
			int digit;
			ss.clear();
			ss<<line[j];
			ss>>digit;
			digitVec.push_back(digit);
		}

		for(j=line.length()-1; j>0; j--)
		{
			if(digitVec[j-1] <  digitVec[j])
			{
				break;
			}
		}

		int firstChange = j-1;

		//if(firstChange == -1)
		//{
		//	cout<<"Case #"<<i+1<<": "<<digitVec[line.length()-1];
		//	outFile<<"Case #"<<i+1<<": "<<digitVec[line.length()-1];
		//	cout<<'0';
		//	outFile<<'0';
		//	for(int k=line.length()-2; k>=0; k--)
		//	{
		//		cout<<digitVec[k];
		//		outFile<<digitVec[k];
		//	}
		//	cout<<endl;
		//	outFile<<endl;
		//	continue;
		//}
		
		for(j=line.length()-1; j>firstChange; j--)
		{
			if(firstChange == -1)
			{
				if(digitVec[j] > 0)
					break;
			}
			else if(digitVec[j] > digitVec[firstChange])
				break;
		}

		int swapIndex = j;
		{
			cout<<"Case #"<<i+1<<": ";
			outFile<<"Case #"<<i+1<<": ";
			for(int k=0; k<firstChange; k++)
			{
				cout<<digitVec[k];
				outFile<<digitVec[k];
			}
			cout<<digitVec[swapIndex];
			outFile<<digitVec[swapIndex];
			for(int k=line.length()-1; k>firstChange; k--)
			{
				if(k == swapIndex)
				{
					if(firstChange == -1)
					{
						cout<<'0';
						outFile<<'0';
					}
					else
					{
						cout<<digitVec[firstChange];
						outFile<<digitVec[firstChange];
					}
				}
				else
				{
					cout<<digitVec[k];
					outFile<<digitVec[k];
				}
			}
			cout<<endl;
			outFile<<endl;
			continue;
		}
	}

	system("pause");
	return 0;
}
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<fstream>
using namespace std;

int main()
{
	vector<string> engineVector, queryVector;
	map<int, string> searchMap;
	map<int, string>::const_iterator iteratorMap;
	ofstream fout;
	fout.open("output.txt");
	fout.clear();
	int DPArray[1001][101];
	int testCase;
	cin >> testCase;
	for(int i = 0 ; i<testCase; i++)
	{
		queryVector.clear();
		searchMap.clear();
		int enginesNumber;
		cin >> enginesNumber;
		cin.ignore();
		for(int j = 0; j < enginesNumber; j++)
		{
			string engineString;			
			getline(cin, engineString, '\n');			
			//enginesVector.push_back(engineString);		
			searchMap.insert(pair<int, string>(j, engineString));
		}

		int queryNumber;
		cin >> queryNumber;
		cin.ignore();
		for(int j = 0; j < queryNumber; j++)
		{
			string queryString;			
			getline(cin, queryString, '\n');			
			queryVector.push_back(queryString);		
		}
		if(queryNumber == 0)
		{
			fout << "Case #" << i+1 << ": "<< "0" << endl;
			continue;
		}
		for(int j = 0; j < enginesNumber; j++)
		{
			iteratorMap = searchMap.find(j);
			if(iteratorMap->second != queryVector[0])
			{
				DPArray[0][j] = 0;
			}
			else
			{
				DPArray[0][j] = -1;
			}
		}
		for(int k = 1; k < queryNumber; k++)
		{
			for(int j = 0; j< enginesNumber; j++)
			{
				iteratorMap = searchMap.find(j);
				if(iteratorMap->second != queryVector[k])
				{
					int min = 10000;
					for(int m = 0; m<enginesNumber; m++)
					{
						if(DPArray[k-1][m] == -1)
							continue;
						if(m == j)
						{
							if(DPArray[k-1][m] < min)
								min = DPArray[k-1][m];
						}
						else 
						{
							if(DPArray[k-1][m]+1 < min)
								min = DPArray[k-1][m]+1;
						}
					}
					DPArray[k][j] = min;
				}
				else DPArray[k][j] = -1;
			}
		}
		//output
		int tempMin = 10000;
		for(int j = 0 ; j < enginesNumber; j++)
		{
			if(DPArray[queryNumber-1][j] == -1)
				continue;
			if(DPArray[queryNumber-1][j] < tempMin)
				tempMin = DPArray[queryNumber-1][j];
		}
		fout << "Case #" << i+1 << ": "<< tempMin << endl;

	}
	fout.close();
}

#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <sstream>
#include <vector>
using namespace std;
int caseNum;
int answer[20];

struct caseStruct
{
	int engineNum;
	vector<string> engineName;
	int searchNum;
	vector<string> searchName;
};

caseStruct *caseArray;

int CompareMin(vector<int> compare,int caseID)
{
	int min = 1000;
	for(int i=0;i<caseArray[caseID].engineNum;i++)
	{
		if(compare[i] < min)
			min = compare[i];
	}
	return min;
}


//i is the order of this case.
int DoSingleCase(int caseID)
{
	if (caseArray[caseID].searchNum == 0)
	{
		answer[caseID] = 0;
		return 0;
	}
	//create array
	int **record = new int*[caseArray[caseID].engineNum];
    for (int i = 0;  i < caseArray[caseID].engineNum;  i++)
    {
		record[i] = new int[caseArray[caseID].searchNum];
		// set first column of the array;
		if ( caseArray[caseID].engineName[i] == caseArray[caseID].searchName[0] )
			record[i][0] = 1000;
		else
			record[i][0] = 0;
    }

	//begin with second column
	for (int col=1; col < caseArray[caseID].searchNum; col++ )
	{
		for ( int row=0; row < caseArray[caseID].engineNum; row++)
		{
			vector<int> compare;
			if(caseArray[caseID].engineName[row] == caseArray[caseID].searchName[col])
			{
				record[row][col] = 1000;
				continue;
			}
			for (int u=0;u<caseArray[caseID].engineNum;u++)
			{
				if(row == u)
					compare.push_back(record[u][col-1]);
				else
					compare.push_back(record[u][col-1]+1);
			}
			int min = CompareMin(compare,caseID);
			record[row][col] = min;
		}
	}
	//cout result
	vector<int> compare;
	for(int n =0; n<caseArray[caseID].engineNum;n++)
	{
		compare.push_back(record[n][caseArray[caseID].searchNum-1]);
	}
	answer[caseID] = CompareMin(compare,caseID);

	for (int m = 0; m < caseArray[caseID].engineNum; m++)
    {
		delete[] record[m];
    }
    delete[] record;
    record = NULL;
    return 0;
}


void PrintCase(struct caseStruct *caseArray)
{
	for(int c=0;c<caseNum;c++)
	{
		cout<< "engineNum is " << caseArray[c].engineNum << endl;
		for(int i = 0; i< caseArray[c].engineNum;i++)
		{
			cout<< caseArray[c].engineName[i]<<endl;
		}
		cout << "searchNum is " << caseArray[c].searchNum << endl;
		for(int i = 0; i< caseArray[c].searchNum;i++)
		{
			cout<< caseArray[c].searchName[i]<<endl;
		}
	}
}



string IntToString(int x)
{
	std::stringstream temp;
	temp << x; 
	return temp.str(); 
    }

int StringToInt(std::string x)
{
	int i;
	std::stringstream temp(x);
	temp >> i;
	return i;
}

void WriteToFile()
{
	ofstream ofile("output");
	for (int i=0;i<caseNum;i++)
	{
		ofile << "Case #" << i+1 << ": " << answer[i] <<endl;
	}
	ofile.close();
}

int main(int argc, char *argv[])
{
	cout<<"please input the filename"<<endl;
	string filename;
	getline(cin,filename);
	ifstream infile(filename.c_str());
    if (!infile) {
		cout << "error: unable to open input file" << endl;
        return -1;
	}
	string casen;
	getline(infile,casen);
	caseNum = StringToInt (casen);
	caseArray = new caseStruct[caseNum];
	for(int i=0;i!=caseNum;i++)
	{
		string engineN;
		int engineNum;
		getline (infile,engineN);
		engineNum = StringToInt (engineN);
		caseArray[i].engineNum = engineNum;
		while (engineNum!=0)
		{
			engineNum --;
			string temp;
			getline(infile,temp);
			caseArray[i].engineName.push_back(temp);
		}
		string searchN;
		int searchNum;
		getline (infile,searchN);
		searchNum = StringToInt (searchN);
		caseArray[i].searchNum = searchNum;
		while (searchNum!=0)
		{
			searchNum --;
			string temp;
			getline(infile,temp);
			caseArray[i].searchName.push_back(temp);
		}
	}
	//PrintCase(caseArray);
	for(int i=0;i<caseNum;i++)
		DoSingleCase(i);
	WriteToFile();
	getchar();
	delete []caseArray;
}
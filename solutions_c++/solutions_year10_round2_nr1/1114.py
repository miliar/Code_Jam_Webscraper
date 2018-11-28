#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <string>
#include <vector>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("A-large.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("sample.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	int exist_folders,new_folders;

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//²Ù×÷Çø
		vector<string> path_list;
		int make_dir_count = 0;
		inFile >> exist_folders >> new_folders;
		for (int j=0; j<exist_folders; j++)
		{
			string tStr;
			inFile >> tStr;
			int sIndex = tStr.find('/',1);
			while (sIndex >= 0)
			{
				string tSubStr = tStr.substr(0,sIndex);
				bool find_path=false;
				for (int k=0; k<path_list.size(); k++)
				{
					if (path_list[k] == tSubStr)
					{
						find_path=true;
					}
				}
				if (!find_path)
				{
					path_list.push_back(tSubStr);
				}
				sIndex = tStr.find('/',sIndex+1);
			}
			bool find_path2=false;
			for (int k=0; k<path_list.size(); k++)
			{
				if (path_list[k] == tStr)
				{
					find_path2=true;
				}
			}
			if (!find_path2)
			{
				path_list.push_back(tStr);
			}
		}
		//new
		for (int j=0; j<new_folders; j++)
		{
			string tStr;
			inFile >> tStr;
			int sIndex = tStr.find('/',1);
			while (sIndex >= 0)
			{
				string tSubStr = tStr.substr(0,sIndex);
				bool find_path=false;
				for (int k=0; k<path_list.size(); k++)
				{
					if (path_list[k] == tSubStr)
					{
						find_path=true;
					}
				}
				if (!find_path)
				{
					path_list.push_back(tSubStr);
					make_dir_count++;
				}
				sIndex = tStr.find('/',sIndex+1);
			}
			bool find_path2=false;
			for (int k=0; k<path_list.size(); k++)
			{
				if (path_list[k] == tStr)
				{
					find_path2=true;
				}
			}
			if (!find_path2)
			{
				path_list.push_back(tStr);
				make_dir_count++;
			}
		}
		outFile << "Case #" << i+1 << ": " << make_dir_count << endl;
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}

class folder_operation
{
public:
	void parshFolder(string ipath){
		ipath.find('/',0);
	}
	string folder_name;
	string path;
};


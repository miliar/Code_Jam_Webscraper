#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

typedef struct DIRECTORY
{
	string name;
	string parent;	
}DIRECTORY;

int findIndex(vector<DIRECTORY> paths, DIRECTORY dir)
{
	if(paths.size()<1)
		return 0;
	for(int i=0; i<paths.size(); i++)
		if(paths[i].parent == dir.parent && paths[i].name==dir.name)
			return 1;
	return 0;
}

void  process(vector<DIRECTORY> &a, string str)
{	
	size_t index=1;
	size_t oldIndex=1;				
	vector<string> tmp;
	tmp.push_back(".");
	while(index != str.npos)
	{
		string subStr;		

		index = str.find("/", oldIndex);
		subStr = str.substr(oldIndex, index-oldIndex);					
		oldIndex = index+1;
		tmp.push_back(subStr);
	}
	string strTmp="";
	for(int i=0; i<tmp.size()-1; i++)
	{
		DIRECTORY dir;
		strTmp+="/"+tmp[i];
		
		dir.parent = strTmp;
		
		dir.name = tmp[i+1];
		if(findIndex(a,dir)==0)
			a.push_back(dir);	
	}
}


int findDir(vector<DIRECTORY> dirs, DIRECTORY dir)
{
	for(int i=0; i<dirs.size(); i++)
		if(dir.parent==dirs[i].parent && dir.name==dirs[i].name)
			return 1;
	return 0;
}

int createDirectories(vector<DIRECTORY> existDirs, vector<DIRECTORY> createDirs)
{
	int count=0;
	for(int i=0; i<createDirs.size(); i++)
	{
		DIRECTORY dir = createDirs[i];
		if(!findDir(existDirs,dir))
		{
			count++;
			existDirs.push_back(dir);
		}		
	}
	return count;
}
void main()
{
	ifstream fin;
	ofstream fout;
	int T,M,N;
	vector<string> pathsExist;
	vector<string> pathsCreate;
	

	fin.open("A-small-attempt2.in", ios_base::in);
	fout.open("A-small-attempt2.out", ios_base::out);

	fin>>T;

	for(int i=1; i<=T; i++)
	{
		string path;
		fin>>N>>M;
		pathsCreate.clear();
		pathsExist.clear();
		fout<<"Case #"<<i<<": ";

		for(int j=0; j<N; j++)
		{
			fin>>path;
			pathsExist.push_back(path);
		}		

		for(int j=0; j<M; j++)
		{
			fin>>path;
			pathsCreate.push_back(path);
		}

		//process create
		vector<DIRECTORY> existDir;
		vector<DIRECTORY> createDir;
		DIRECTORY root;
		root.parent = "";
		root.name = ".";		
		existDir.push_back(root);
		createDir.push_back(root);
		for(int j=0; j<N; j++)
		{
			process(existDir,pathsExist[j]);
		}
		for(int j=0; j<M; j++)
		{
			process(createDir,pathsCreate[j]);
		}

		int result = createDirectories(existDir, createDir);
		fout<<result;

		if(i<T)
			fout<<endl;
	}

	fin.close();
	fout.close();	
}
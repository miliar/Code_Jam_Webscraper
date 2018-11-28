#include <iostream>
using namespace std;
#include <fstream>
#include <string>
#include <vector>

void LoadDictionary(vector<string> &tbl, vector<string> &ml){
	ifstream fin("A-large.in");
	string temp;
	getline(fin, temp, ' ');
	int l = atoi(temp.c_str());
	getline(fin, temp, ' ');
	int d = atoi(temp.c_str());
	getline(fin, temp, '\n');
	int n = atoi(temp.c_str());

	for(int i=0;i<d;++i){
		getline(fin, temp, '\n');
		tbl.push_back(temp);
	}

	for(int i=0;i<n;++i){
		getline(fin, temp, '\n');
		ml.push_back(temp);
	}
}

int main(void)
{
	vector<string> messageList;
	vector<string> dictionary;
	LoadDictionary(dictionary, messageList);

	ofstream fout("A-large.out");
	for(unsigned int i=0;i<messageList.size();++i)
	{
		int numInterp=0;

		vector<string> tokens;
		for(unsigned int j=0;j<messageList[i].size();++j)
		{
			if(messageList[i][j] != '(')
			{
				string newTok ="";
				newTok+=messageList[i][j];
				tokens.push_back(newTok);
			}
			else
			{
				string newTok="";
				++j;
				while(messageList[i][j]!=')')
				{
					newTok+=messageList[i][j++];
				}
				tokens.push_back(newTok);
			
			}
		}
		numInterp=dictionary.size();
		for(int j=0;j<dictionary.size();++j)
		{
			for(int k=0;k<dictionary[j].size();++k)
			{
				bool matched=false;
				for(int l=0;l<tokens[k].size();++l)
				{
					if(dictionary[j][k] == tokens[k][l])
						matched=true;
				}

				if(matched==false)
				{
					numInterp--;
					break;
				}
			}
		}

		fout << "Case #"<<i+1<<": "<< numInterp <<'\n';
		
	}

	return 0;
}

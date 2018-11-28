#include<iostream>
#include<vector>
#include<string>
//#include "tree.hh"
#include<map>

using namespace std;

string SplitFilename (const string& str)
{
  size_t found;
  found=str.find_last_of("/\\");
  return str.substr(0,found);
}


int main()
{
	int T, N, M;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		map<string,bool> hash;
		int count = 0;
		cin >> N >> M;
		for(int j = 0; j < N; j++)
		{
			string line;
			cin >> line;
			string temp;
			hash[line] = true;
			temp = SplitFilename(line);
			while(temp!="")
			{
				hash[temp] = true;
				temp = SplitFilename(temp);
			}
		}
		for(int j = 0; j < M; j++)
		{
			string line;
			cin >> line;
			string temp;
			if(hash[line])
				continue;
			count++;
			hash[line] = true;
			temp = SplitFilename(line);
			while(temp!="")
			{
				if(hash[temp])
					break;
				count++;
				hash[temp] = true;
				temp = SplitFilename(temp);
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
}
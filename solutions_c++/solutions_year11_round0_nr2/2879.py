#include <iostream>
#include <memory>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream fin("file\\input.txt");
ofstream fout("file\\output.txt");

int main()
{
	int nCases = 0;
	fin >> nCases;
	for(int i = 0; i < nCases; ++ i)
	{
		int c, d, n;
		fin >> c;
		map<string, char> transformer;
		string str;
		for(int j = 0; j < c; ++ j)
		{
			fin >> str;
			transformer[str.substr(0, 2)] = str[2];
			swap(str[0], str[1]);
			transformer[str.substr(0, 2)] = str[2];
		}
		
		fin >> d;
		map<char, char> oppositor;
		for(int j = 0; j < d; ++ j)
		{
			fin >> str;
			oppositor[str[0]] = str[1];
			oppositor[str[1]] = str[0];
		}

		fin >> n;
		string ans(""); char cur;
		for(int j = 0; j < n; ++ j)
		{
			fin >> cur;
			if(ans.length() == 0){
				ans += cur;
			}
			else{
				string test("");
				test += cur; test += ans[ans.length()-1];
				if(transformer.find(test) != transformer.end()){
					ans[ans.length()-1] = transformer[test];
				}
				else if(oppositor.find(cur) != oppositor.end() && find(ans.begin(), ans.end(), oppositor[cur]) != ans.end()){
					ans = "";
				}
				else{
					ans += cur;
				}
			}
		}
		fout << "Case #" << i+1 << ": [";
		if(ans != "")
		{
			fout << ans[0];
			for(int j = 1; j < ans.length(); ++ j){
				fout << ", " << ans[j];
			}
		}
		fout << "]" << endl;
	}
	system("pause");
	return 0;
}
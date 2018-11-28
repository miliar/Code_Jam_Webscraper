#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <istream>
#include <fstream>
#include <cmath>
#include <map>
using namespace std;

map<string, bool> label;
vector<string> vec;

int n, s, q;

int main()
{
	ifstream fin("A-large.in");  
	ofstream fout("results.txt", ios::app);
	string input;
	int num;
	int res;
	int caseNum = 1;
	fin >> n;
	while (n--)
	{
		vec.clear();
		label.clear();
		res = 0;
		fin >> s;
		fin.ignore();
		for(int i = 0; i < s; i ++)
		{			
			getline(fin, input);
			
			vec.push_back(input);
			label[input] = false;
		}
		fin >> q;
		fin.ignore();
		num = 0;
		while (q--)
		{
			getline(fin, input);			
			if(label[input] == false)
			{
				num++;
				if(num == s)
				{
					res++;
					for (int i = 0; i < s; i ++)
					{
						label[vec[i]] = false; 
					}
					num = 1;
				}
				label[input] = true;
			}
		}
		fout << "Case #" << caseNum << ": " << res << endl;
		caseNum ++;

	}
	fin.close();
	fout.close();
	return 0;
}
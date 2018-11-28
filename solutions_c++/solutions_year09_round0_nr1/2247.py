#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

int l,d,n;
vector<string> data;

int find_count(vector<string> &str)
{
	int count = 0;
	for (int i=0;i<data.size();i++)
	{
		string tempData = data[i];
		bool flag = true;
		for (int j=0;j<l;j++)
		{
			string temp = str[j];
			if (find(temp.begin(), temp.end(), tempData[j]) == temp.end()) {
				flag = false;
				break;
			}
		}
		if (flag) count++;
	}

	return count;
}

void main()
{
	string str;

	fstream fin("C:\\Projects\\codejam\\Release\\input.txt",std::ios::in);
	fstream fout("C:\\Projects\\codejam\\Release\\output.txt",std::ios::out);

	fin >> l >> d >> n;
	getline(fin, str, '\n');

	for (int z=0;z<d;z++) {
		string str;
		getline(fin, str, '\n');
		data.push_back(str);
	}

	for (int z=0;z<n;z++)
	{
		vector<string> temp;
		string str;
		getline(fin, str, '\n');
		for (int i=0;i<str.size();i++) {
			if (str[i] == '(') {
				i++;
				int j;
				for (j=0;i+j<str.size();j++) {
					if (str[i+j] == ')')
					{
						break;
					}
				}
				temp.push_back(str.substr(i, j));
				i += j;
			}
			else
				temp.push_back(str.substr(i, 1));
		}
		int count = find_count(temp);
		fout << "Case #" << (z+1) << ": " << count << "\n";
	}
	fin.close();
	fout.close();
}
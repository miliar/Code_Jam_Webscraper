#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
	string dic = "yhesocvxduiglbkrztnwjpfmaq",temp;
	ifstream fin("input");
	ofstream fout("output");
	vector <string> a;
	int n;
	fin>>n;
	getline(fin,temp);
	for(int i =0;i<n;i++)
	{
		getline(fin,temp);
		for(int j = 0;j<temp.size();j++)
		{
			if(temp[j] == ' ')
				continue;
			else if(islower(temp[j]))
				temp[j] = dic[temp[j] - 'a'];
			else 
				temp[j] = dic[temp[j] - 'A'] - 'a' + 'A';
		}
		if(i<9)
		{
			temp = "Case # : "+temp;
			temp[6] = (i+1)+48;
		}
		else
		{
			temp = "Case #  : "+temp;
			temp[6] = ((i+1)/10)+48;
			temp[7] = ((i+1)%10)+48;
		}
		fout<<temp<<endl;
	}

	system("pause");
}
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <fstream>
using namespace std;

int n;
vector<string> data;
string word="welcome to code jam";

void get_data(ifstream &inp);
void make_mat(vector<vector<int>> &m, int i);

int main()
{	
	string st;
	ifstream indata;
	vector<vector<int>> mat;
	cout << "Name of the file with the data: " << endl;
	cin >> st;
	indata.open(st.c_str());
	if (!indata.is_open())
	{
	cout << "Wrong file!" << endl;
	return 1;
	}
	get_data(indata);
	cout << "Name the file with the output: " << endl;
	cin >> st;
	ofstream out(st.c_str());
	if(!out) {
	cout << "Cannot open file.\n";
	return 1;
	}
	for (int i=0; i<n ;i++)
	{
		make_mat(mat, i);
		//cout << "d " << data[i].size()<< endl;
		//cout << "w " << word.size()<< endl;
		if (word[0]==data[i][0])
			mat[0][0]=1;
		for(int j=1; j<data[i].size(); j++)
		{
			mat[0][j]=mat[0][j-1];
			if (word[0]==data[i][j])
			{
				mat[0][j]+=1;
				if (mat[0][j]>9999)
					mat[0][j]=mat[0][j]%10000;
			}
		}
		for (int x=1; x<word.size(); x++)
		{
			for(int j=1; j<data[i].size(); j++)
			{
				mat[x][j]=mat[x][j-1];
				if (word[x]==data[i][j])
				{
					mat[x][j]+=mat[x-1][j-1];
					if (mat[x][j]>9999)
						mat[x][j]=mat[x][j]%10000;
				}
			}
		}
		//for (int u=0; u<word.size(); u++)
		//{
		//	for(int y=0; y<data[i].size(); y++)
		//		cout << mat[u][y];
		//	cout << endl;
		//}
		out << "Case #" << i+1 << ": ";
		if (mat[word.size()-1][data[i].size()-1]<10)
			out << "000";
		else if (mat[word.size()-1][data[i].size()-1]<100)
			out << "00";
		else if (mat[word.size()-1][data[i].size()-1]<1000)
			out << "0";
		out << mat[word.size()-1][data[i].size()-1] << endl;
	}
}

void get_data(ifstream &inp)
{
	string st;
	inp >> n;
	getline(inp,st);
	for (int i=0; i< n; i++)
	{
		getline(inp,st);
		data.push_back(st);
	}
}

void make_mat(vector<vector<int>> &m, int i)
{
	vector<int> aa;
	m.clear();
	for(int x=0; x<word.size(); x++)
	{
		m.push_back(aa);
		for(int j=0; j<data[i].size(); j++)
			m[x].push_back(0);
	}
}
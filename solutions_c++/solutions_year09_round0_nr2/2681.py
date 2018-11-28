#include<iostream>
#include<stdlib.h>
#include<string>
#include<fstream>
using namespace std;
int map[100][100] = {10001};
char basin[100][100] = {'-'};
int min[100][100];
int row, col;
char cur_id = 'a';

char getbasin(int i, int j)
{
	//cout<<"called getbasin("<<i<<", "<<j<<")";
	if(basin[i][j] != '-')
		return basin[i][j];

	int mini=i, minj=j, minval=map[i][j];
	
	if ((i>0) && (map[i-1][j] < minval))
	{
		mini = i-1; minj = j; minval = map[i-1][j];
	}
	if((j>0) && (map[i][j-1] < minval))
	{
		mini = i; minj = j-1; minval = map[i][j-1];
	}
	if((j<col-1) && (map[i][j+1] < minval))
	{
		mini = i; minj = j+1; minval = map[i][j+1];
	}
	if((i<row-1) && (map[i+1][j] < minval))
	{
		mini = i+1; minj = j; minval = map[i+1][j];
	}
	if(minval == map[i][j])	
	{
		basin[i][j] = cur_id;
		//cout<<"assigining id "<<cur_id<<endl;
		cur_id++;
	//	cout <<"new id is "<<cur_id<<endl;
	}
	else
	{
		basin[i][j] = getbasin(mini,minj);
		//cout<<"calling getbasin("<<mini<<","<<minj<<")";
	}
	return basin[i][j];
}

int main()
{
	ifstream infile("/root/B-large.in");
	ofstream outfile("/root/B-large.out");
	int testcaseNo;
	if(!infile)
	{
		cout << "couldn't open input file";
		//cout << endl;
		return 1;
	}
	if(!outfile)
	{
		cout << "couldn't open output file";
		//cout << endl;
		return 1;
	}
	infile >> testcaseNo;
	//cout << "number of testcases is " << testcaseNo;		
	//cout << endl;
	
	for(int count = 1; count<= testcaseNo; count++)
	{
		cur_id = 'a';
		int m, n;
		infile >> m >> n;
		row = m;
		col = n;
		for(int i=0; i<m; i++)
		{
			for(int j=0; j<n; j++)
			{
				int num;
				infile >> num;
				map[i][j] = num;
				basin[i][j] = '-';
	//			cout << "map["<<i<<"]["<<j<<"] = "<<map[i][j]<<basin[i][j];
			}
	//		cout << endl;
		}

		for(int i=0; i<m; i++)
		{
			for(int j=0; j<n; j++)
			{
				if(basin[i][j] == '-')
					basin[i][j] = getbasin(i, j);
	//			cout << "basin["<<i<<"]["<<j<<"] = "<<basin[i][j];
			}
			//cout << endl;
		}
		outfile << "Case #"<<count<<" :\n";
		for(int i=0; i<m; i++)
		{
			std::string out = "";
			for(int j=0; j<n; j++)
			{
				out += basin[i][j];
				if(j+1 != n)
					out += " ";
			}
			out += "\n";
			outfile << out;
		}
	}
}

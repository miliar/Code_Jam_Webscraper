#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>

using namespace std;

vector<pair<string,char>> combine;
vector<pair<char,char>> opposite;

int main()
{
	ifstream fin("B-large.in");
	ofstream out("outfile.out");

	int numOfTest;
	fin>>numOfTest;
	for (int i =0 ; i< numOfTest ; i++)
	{
		combine.clear();
		opposite.clear();
		int C;
		int D;
		fin>>C;
		string temp;
		for (int k =0 ; k < C; k++)
		{
			fin>>temp;
			string x ="";
			x+=temp[0];
			x+=temp[1];
			combine.push_back(make_pair(x,temp[2]));
		}
		fin>>D;
		for (int k =0; k< D; k++)
		{
			fin>>temp;
			opposite.push_back(make_pair(temp[0],temp[1]));
		}
		fin>>C;
		fin>>temp;
		//loop on the buffer char by char
		string currentString = "";
		currentString+=temp[0];
		bool check = true;
		for (int k =1; k< temp.size(); k++)
		{
			currentString+=temp[k];
			for (int z =0; z< combine.size()&&currentString.size()>1; z++)
			{
				string rev = "";
				rev += combine[z].first[1];
				rev += combine[z].first[0];
				size_t found1 = currentString.find(combine[z].first);
				size_t found2 = currentString.find(rev);
				if (found1 != -1 && found2 != -1)
				{
					if (found1<found2)
					{
						found1 = found2;
					}
				}
				else if (found2 != -1 )
				{
					found1 = found2;
				}
				if (found1 != string::npos)
				{
					if ((int)found1 == currentString.size()-2)
					{
						string t ="";
						for (int w =0; w<currentString.size()-2;w++)
						{
							t+=currentString[w];
						}
						t+=combine[z].second;
						currentString = t;
					}
				}
			}

			for (int z =0 ; z < opposite.size()&&currentString.size()>0;z++)
			{
				string x = "";
				x+=opposite[z].first;
				size_t found = currentString.find(x);
				if (found != string::npos)
				{
					x ="";
					x+=opposite[z].second;
					found = currentString.find(x);
					if(found!= string::npos)
					{
						currentString = "";
						check = false;
						break;
					}
				}
			}
				
		}
		/*for (int z =0 ; z < opposite.size()&&currentString.size()>0;z++)
		{
			string x = "";
			x+=opposite[z].first;
			size_t found = currentString.find(x);
			if (found != string::npos)
			{
				x ="";
				x+=opposite[z].second;
				found = currentString.find(x);
				if(found!= string::npos)
				{
					currentString = "";
					check = false;
					break;
				}
			}
		}*/
		out<<"Case #"<<i+1<<": "<<"[";
		
		int f =0;

		if (currentString.size()>0)
		{

			for (; f<currentString.size()-1;f++)
			{
				out<<currentString[f]<<", ";
			}
			out<<currentString[f];

		}
		out<<"]\n";

	}

	return 0;
}
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <map>
#include <ctime>
#include <cmath>
using namespace std;

int main(int argc,char *argv[])
{
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");

	if (!in)
	{
		cerr<<"file open error!";
		return EXIT_FAILURE;
	}
	
	int L,D,N;
	in>>L>>D>>N;

	
	vector<string> vs;
	for (int i=0;i<D;++i)
	{
		string str;
		in>>str;
		vs.push_back(str);
	}
	
	for (int j=0;j<N;j++)
	{
		string pattern;
		in>>pattern;
		int count=0;

		vector<char> vc;
		
		for (int m=0;m<vs.size();++m)
		{
			string str=vs[m];
			string::size_type pos=0;
			string::size_type backpos=pos;
			int com=0;
			int j=0;
			if (pos=pattern.find_first_of("()")==string::npos)
			{
				if (pattern==str)
				{
					com=L;
				}
			}
			else
			{
				for (int i=0;i<L;++i)
				{

					if (pattern[j]=='(')
					{
						pos=pattern.find_first_of(")",j);
						if (pos!=string::npos)
						{
							string getstr=pattern.substr(j+1,pos-j-1);
							if (getstr.find(str[i])!=string::npos)
							{
								com++;
								j=pos+1;
							}
							else
								break;
						}
						else
							break;

					}
					else
					{
						if (pattern[j]==str[i])
						{
							com++;
							j++;
						}
						else
							break;
					}
				}	
			}

			if (com==L)
			{
				count++;
			}

		}
		out<<"Case #"<<j+1<<":"<<" "<<count<<endl;	
	}

	
	in.close();
	out.close();

	return 0;
}
#include <algorithm>
#include <vector>
#include <bitset>
#include <map>
#include <math.h>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <queue>
#include <string>
#include <stack>
#include <sstream>
#include <string.h>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
	ifstream myfile_in ("input.in");
	ofstream myfile_out;
	myfile_out.open ("output.txt");
	int cases = 0, first = 0, second = 0, num = 0, len = 0;
	char first_str[7];
	string line = "";
	bool start = true;
	map<string, int> m;
	if (myfile_in.is_open() && myfile_out.is_open())
	{
		while ( myfile_in.good() )
		{
			getline (myfile_in,line);
			if(start)
			{
				start = false;
			}
			else
			{
				first = second = len = 0;
				char * pch = strtok((char *)line.c_str()," ");
				while (pch != NULL)
				{
					string str = pch;
					if(first == 0)
					{
						first = atoi(str.c_str());
						len = str.length();
					}
					else
					{
						second = atoi(str.c_str());
					}
					pch = strtok(NULL, " ");
				}
				num = 0;
				m.clear();
				if(len > 0)
				{
					for(int j = first; j <= second; j++)
					{
						itoa(j, first_str, 10);
						for(int i = len - 1; i > 0; i--)
						{
							char result_str [7];
							strcpy(result_str, first_str);
							rotate(result_str, result_str + i, result_str + len);
							if(result_str[0] != '0')
							{
								int result = atoi(result_str);
								if(first <= result && result <= second && strcmp(first_str,result_str) != 0)
								{
									stringstream ss1, ss2;
									ss1 << first_str << "," << result_str;
									ss2 << result_str << "," << first_str;
									map<string,int>::iterator it1 = m.begin(), it2 = m.begin();
									it1 = m.find(ss1.str());
									it2 = m.find(ss2.str()); 
									if(it1 == m.end() && it2 == m.end())
									{
										num++;	
										m[ss1.str()] = 0;
										m[ss2.str()] = 0;
									}
									ss1.str("");
									ss2.str("");
								}
							}
						}
					}
					myfile_out << "Case #" << ++cases << ": " << num << "\n";
				}
			}
		}
		myfile_in.close();
		myfile_out.close();
	}
	return 0;
}
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

void printList(vector<char> outputList)
{
	for(int j = 0; j < outputList.size()-1; j++)
	{
		cout << outputList[j] << ", ";
	}		
	cout << outputList[outputList.size() - 1];
		
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int C, D, N;
		cin >> C;
		vector<string> combinedQ(C);
		vector<char> combinedA(C);
		for(int j = 0; j < C; j++)
		{
			string s;
			cin >> s;
			combinedQ[j] = s.substr(0, s.size() - 1);
			combinedA[j] = s[s.size() - 1];
		}
		cin >> D;
		vector<string> opposed(D);
		for(int j = 0; j < D; j++)
		{
			cin >> opposed[j];
		}
		cin >> N;
		vector<char> outputList;
		
		for(int j = 0; j < N; j++)
		{
			char c;
			cin >> c;
			if(outputList.size() > 0)
			{
				string s = "";
				s += c;
				s += outputList[outputList.size() - 1];
				vector<string>::iterator it;
				it = find(combinedQ.begin(), combinedQ.end(), s);
				if(it != combinedQ.end())
				{
					outputList.pop_back();
					outputList.push_back(combinedA[it - combinedQ.begin()]);
					
				}
				else
				{
					reverse(s.begin(), s.end());
					it = find(combinedQ.begin(), combinedQ.end(), s);
					if(it != combinedQ.end())
					{
						outputList.pop_back();
						outputList.push_back(combinedA[it - combinedQ.begin()]);
					
					}
					else
					{
						bool clear = false;
						bool push = false;
						for(int k = 0; k < outputList.size(); k++)
						{
							s = "";
							s += c;					
							s += outputList[k];
							it = find(opposed.begin(), opposed.end(), s);
							if(it != opposed.end())
							{
								clear = true;
								break;
								
							}
							else
							{
								reverse(s.begin(), s.end());
								it = find(opposed.begin(), opposed.end(), s);
								if(it != opposed.end())
								{
									clear = true;
									break;
									
								}
								
							}
							
						}
						if(clear)
							outputList.clear();
						else
							outputList.push_back(c);		
					}
				}
			}
			else
			{
				outputList.push_back(c);
			}			
		}
	
		cout << "Case #" << i << ": [";
		if(outputList.size() > 0)
			printList(outputList);	
		cout << "]" << endl;
	}
	
	return 0;
}

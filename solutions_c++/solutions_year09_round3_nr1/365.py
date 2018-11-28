#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int test;
	in >> test;
	for(int k=0; k<test; k++)
	{
		string line;
		in >> line;
		vector<int> arr(line.size());
		set<int> count;
		for(int i=0; i<line.size();i++)
		{
			count.insert(line[i]);
		}
		long long base = count.size();
		if( base == 1 )
			base ++;
		map<char, int> alias;
		alias[ line[0] ] = 1;
		arr[0] = 1;
		int counter =0;
		for(int i=1; i < arr.size(); i++)
		{
			if( alias.find( line[i] ) != alias.end())
			{
				arr[i] = alias[ line[i] ];
			}
			else{
				if( counter == 1)
					counter++;
				arr[i] = counter;
				alias[ line[i] ] = counter;
				counter++;
			}
		}

		long long answer=0;
		long long tmp = 1;
		for(int i=arr.size()-1; i >= 0 ; i--)
		{
			answer += tmp * arr[i];
			tmp*= base;
		}
		out << "Case #" << k+1 << ": "<< answer << endl;
		

	}

	return 0;
}
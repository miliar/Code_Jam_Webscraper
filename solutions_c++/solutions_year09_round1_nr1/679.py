#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <deque>
#include <vector>
#include <math.h>
using namespace std;

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1a_1\\A-small-attempt0.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Round1a_1\\out.txt";

int getBaseFromStr(string str, int* bases)
{
	int i = 0;
	int p = 0;
	int base = 0;
	while(p < str.length())
	{
		if(str[p] != ' ')
		{
			base = base * 10 + str[p] - 48;
		}else
		{
			bases[i++] = base;
			base = 0;
		}
		p++;
	}
	bases[i++] = base;

	return i;
}

int getNumberList(int num, int base, deque<int>& de)
{
	int list_len = 0;
	int t = 0;
	while(num != 0)
	{
		t = num % base;
		num /= base;
		de.push_back(t);
		list_len++;
	}

	return list_len;
}

int isHappyNumber(int num, int base)
{
	deque<int> de;
	vector<int> visited;
	int squar_sum;
	int number = num;
	visited.push_back(number);
	while(1)
	{
		int list_len = getNumberList(number, base, de);
		squar_sum = 0;
		for(int i = 0; i < list_len; i++)
		{
			squar_sum += de.front() * de.front();
			de.pop_front();
		}
		number = squar_sum;
		if(number == 1)
		{
			return 1;
		}
		for(i = 0; i < visited.size(); i++)
		{
			if(visited[i] == number)
			{
				return 0;
			}
		}
		visited.push_back(number);
	}
	return 0;
}

void main()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}

	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	
	int T;
	infile>>T;
	string buffer;
	getline(infile,buffer);
	for(int i = 0; i < T; i++)
	{
		getline(infile,buffer);
		int *bases = new int[buffer.length()];
		int base_num = getBaseFromStr(buffer, bases);
		int min_happy = 2;
		while(1)
		{
			int flag = 1;
			for(int k = 0; k < base_num; k++)
			{
				if(isHappyNumber(min_happy, bases[k]) != 1)
				{
					flag = 0;
					break;
				}
			}
			if(flag == 1)
			{
				break;
			}else
			{
				min_happy++;
			}
		}
		outfile<<"Case #"<<i + 1<<": "<<min_happy<<endl;
		delete[] bases;
	}

	infile.close();
	outfile.close();
}

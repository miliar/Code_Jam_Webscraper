/***************************************************

Name:			Justin McCandless
Compiler Name:	g++
Filename:		qb.cpp
Problem:		Google Code Jam 2012 Qualification Question B

****************************************************/

#include<iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

struct limit
{
	int regular;
	int surprising;
};

class limits
{
	public:
		limits();
		~limits();
		int getRegular (int);
		int getSurprising (int);

	private:
		limit data[31];
		void fill (int);
};

int main(void)
{
	int cases;

	string line;
	getline (cin, line);
	stringstream(line) >> cases;

	limits scoreLimits;
	for (int i = 0; i < cases; i++)
	{
		int N; // # Googlers
		int S; // # surprising scores (difference of 2)
		int p; // # best result of at least p

		getline (cin, line);

		stringstream(line.substr(0,line.find(" "))) >> N;
		line = line.substr((line.find(" ") + 1), line.length());

		stringstream(line.substr(0,line.find(" "))) >> S;
		line = line.substr((line.find(" ") + 1), line.length());

		stringstream(line.substr(0,line.find(" "))) >> p;
		line = line.substr((line.find(" ") + 1), line.length());

		vector<int> t;
		line = line + ' ';
		while (line != "")
		{
			int ti;
			stringstream(line.substr(0,line.find(" "))) >> ti;
			line = line.substr((line.find(" ") + 1), line.length());
			t.push_back(ti);
		}

		// count scores that pass the test with their regular limit
		int count = 0;
		int size = t.size();
		for (int j = 0; j < size; j++)
		{
			if (scoreLimits.getRegular(t.front()) >= p)
			{
				count++;
				t.erase(t.begin());
			}
			else
			{
				int tmp = t[0];
				t.erase(t.begin());
				t.push_back(tmp);
			}
		}

		// count as many scores that pass the test with surprising limits as we can
		int j = 0;
		size = t.size();
		while (S && (j < size))
		{
			if (scoreLimits.getSurprising(t.front()) >= p)
			{
				count++;
				S--;
				t.erase(t.begin());
			}
			else
			{
				int tmp = t[0];
				t.erase(t.begin());
				t.push_back(tmp);
			}

			j++;
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}
	
    return 1;
}

// Constructor
limits::limits(void)
{
	for (int i = 0; i < 31; i++)
	{
		data[i].regular = -1;
		data[i].surprising = -1;
	}
}

// Destructor
limits::~limits(void)
{

}

int limits::getRegular (int tin)
{
	if (data[tin].regular != -1)
		return data[tin].regular;
	else
	{
		fill(tin);
		return data[tin].regular;
	}
}

int  limits::getSurprising (int tin)
{
	if (data[tin].surprising != -1)
		return data[tin].surprising;
	else
	{
		fill(tin);
		return data[tin].surprising;
	}
}

void limits::fill (int tin)
{
	limit tmp;
	tmp.surprising = -1;
	tmp.regular = -1;
	int i = 10;
	while ((tmp.surprising == -1) || (tmp.regular == -1))
	{
		int lowestS = 0;
		int lowestR = 0;

		if (i == 1)
		{
			lowestS = 1;
			lowestR = 1;
		}
		else
		{
			lowestS = i + 2 * (i - 2);
			lowestR = i + 2 * (i - 1);
		}

		if ((lowestS <= tin) && (tmp.surprising == -1))
			tmp.surprising = i;
		if ((lowestR <= tin) && (tmp.regular == -1))
			tmp.regular = i;

		i--;
	}

	data[tin] = tmp;
	return;
}



#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct vector2d
{
	string name;
	bool seen;
	vector2d() { name = ""; seen = false; }
} tmpv2d;

bool isFull(vector<vector2d> &selist)
{
	int i;
	for (i=0; i<selist.size(); i++)
		if (selist[i].seen == false)
			return false;
	return true;
}

void makeClear(vector<vector2d> &selist)
{
	int i;
	for (i=0; i<selist.size(); i++)
		selist[i].seen = false;	
}

bool check4change(vector<string> &query,vector<vector2d> &selist, string &current_se, int pos)
{
	int i,j;
	bool initial = false;
	if (query[pos] == current_se || current_se == "")
	{
		if (current_se == "")
			initial = true;

		makeClear(selist);
		for (i=pos; i<query.size(); i++)
		{
			if (!isFull(selist))
				for (j=0; j<selist.size();j++)
					if (selist[j].name == query[i])
					{
						selist[j].seen = true;
						break;
					}
		}
		if (isFull(selist))
			current_se = selist[j].name;
		else
			for (i=0; i<selist.size();i++)
				if (selist[i].seen == false)
				{
					current_se = selist[i].name;
					break;
				}
		if (!initial)
			return true;
	}
	return false;
}

int main()
{
	vector<vector2d> selist;
	vector<string> qlist;
	int res;
	string current_se;
	
	int count,z,y,x;
	ifstream infile("A-large.in");
	ofstream outfile("universe-large.out");
	
	infile >> count;
	for (z=0; z<count; z++)
	{
		selist.clear();
		qlist.clear();
		res = 0;
		current_se = "";
		
		infile >> x;
		infile.ignore(8,'\n');
		for (y=0; y<x; y++)
		{
			selist.push_back(tmpv2d);
			getline(infile,selist[y].name);
		}

		infile >> x;
		infile.ignore(8,'\n');
		for (y=0; y<x; y++)
		{
			qlist.push_back("");
			getline(infile,qlist[y]);
		}

		outfile << "Case #" << z+1 << ": ";
		for (y=0; y<qlist.size(); y++)
			if (check4change(qlist,selist,current_se,y))
				res++;
		outfile << res << endl;
	}

	infile.close();
	outfile.close();
}


#include "iostream"
#include "fstream"
#include "string"
#include "vector"
using namespace std;

bool differ(string s1, string s2)
{
	return s1 != s2;
}
int search(vector <string> v1, vector <string> v2, int differ = 0)
{
	switch(differ)
	{
	case 0:
		for(int i = 0; i < (int)v1.size(); i++)
		{
			for(int j = 0; j < (int)v2.size(); j++)
				if(v1[i] == v2[j])
					return i;
		}
		break;
	case 1:
		int flag = false;
		for(int i = 0; i < (int)v1.size(); i++)
		{
			int j = 0;
			for(j = 0; j < (int)v2.size(); j++)
			{
				if(v1[i] == v2[j])
				{
					flag = true;
					break;
				}
			}
			if(flag == true)
			{
				flag = false;
				continue;
			}
			return i;
		}
		break;
	}
	return -1;
}

int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("OutputLarge.out");
	int n = 0, s = 0, q = 0;
	int switch_count = 0; // Number of switch
	bool *Mark;
	infile >> n;
	vector <string> Engine, Query;
	for(int i = 0; i < n; i++)
	{
		Engine.clear();
		Query.clear();
		infile >> s;
		int count = 0; // Number of query
		switch_count = 0;
		infile.get();
		char temp[101];
		for(int j = 0; j < s; j++)
		{
			infile.getline(temp, 101);
			Engine.push_back(temp);
		}
		infile >> q;
		infile.get();
		for(int k = 0; k < q; k++)
		{
			infile.getline(temp, 101);
			Query.push_back(temp);
			int num_of_appear = 0;
			for(int l = 0; l < (int)Query.size(); l++)
			{
				if(Query[l] == temp)
					num_of_appear++;
				if(num_of_appear > 1)
					break;
			}
			if(num_of_appear == 1)
				count++;
			if(count == s)
			{
				string str = Query.back();
				Query.pop_back();
				switch_count ++;
				count = 1;
				Query.clear();
				Query.push_back(str);
			}
		}
		outfile << "Case #" << i+1 << ": ";
		outfile << switch_count << endl;
	}
	return 0;
}
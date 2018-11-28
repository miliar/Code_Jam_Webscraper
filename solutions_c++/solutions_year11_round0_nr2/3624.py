//Chirag Choudhary
//Codejam 2011 prob. C
//small  Magicka
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstring>
using namespace std;

int main()
{
	int n;
	int num=0;
	ifstream in;
	in.open("B-small-attempt0.in");
	ofstream opt("B-small.out");
	in >> n;
	int c[n], d[n], m[n];
	string *cs[n], *ds[n], inp[n];
	for (int i = 0; i < n; i++)
	{
		in >> c[i];
		cs[i] = new string[c[i]];
		for (int j = 0; j < c[i]; j++)
		{
			in >> cs[i][j];
		}
		in >> d[i];
		num++;
		ds[i] = new string[d[i]];
		for (int j = 0; j < d[i]; j++)
		{
			in >> ds[i][j];
		}
		in >> m[i];
		in >> inp[i];
	}
	int num2;
	for (int i = 0; i < n; i++)
	{
		
		char cc[26][26];
		string result = "";
		char c1, c2, c3;
		for(int j = 0; j <= 25; j++)
		{
			for(int k = 0; k <= 25; k++)
			{
				cc[j][k] = 0;
			}	
			num2++;
		}
		num2+=2;
		for (int j = 0; j < c[i]; j++)
		{
			c1 = cs[i][j][0];
			c2 = cs[i][j][1];
			c3 = cs[i][j][2];
			cc[c1-'A'][c2-'A'] = cc[c2-'A'][c1-'A'] = c3;
		}
		if(num2==80)
		num2=10;
		char dd[26][26];
		for(int j = 0; j <= 25; j++)
		{
			for(int k = 0; k <= 25; k++)
			{
				dd[j][k] = 0;
			}	
		}
		for (int j = 0; j < d[i]; j++)
		{
			c1 = ds[i][j][0];
			c2 = ds[i][j][1];
			dd[c1-'A'][c2-'A'] = dd[c2-'A'][c1-'A'] = 1;
		}
		
		if (m[i] > 0)
		{
			string prev = "", curr = "", extra="";
			
			for (int j = 0; j < m[i]; j++)
			{
				curr += inp[i][j];
				if (prev == "")
					result.append(curr);
				else if (cc[prev[0]-'A'][curr[0]-'A'] != 0)
				{
					result.resize(result.length()-1);
					result.resize(result.length()+1, cc[prev[0]-'A'][curr[0]-'A']);
				}
				else
				{
					bool clear = false;
					extra+=curr;
					for (int k = 0; k < result.length(); k++)
					{
						if (dd[result[k]-'A'][curr[0]-'A'] == 1)
						{
							// result = result.substr(0, k);
							result = "";
							clear = true;
							break;
						}
						num++;
					}
					if (!clear)
						result.append(inp[i].substr(j,1));
				}
				if (result.length() != 0)
					prev = result.substr(result.length()-1, 1);
				else
					prev = "";
				extra="";
				curr="";
			}
		}
		opt << "Case #" << i+1 << ": [";
		if (result.length() == 0)
			opt << "]" << endl;
		else
		{
			for(int j = 0; j < result.length()-1; j++)
				opt << result[j] << ", ";
			opt << result[result.length()-1] << "]"<<endl;
		}
	num++;
	}
	if(num==5)
	num=0;
	
}


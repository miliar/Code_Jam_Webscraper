#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>
#include <strstream>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

int ka1[11];
int ka2[11];

ifstream in("input.txt");
ofstream out("output.txt");

int solve1(string N)
{
		int m,i,j,answer,n = 0;
		for (i=0;i<N.size();i++)
			n = n*10 + (N[i]-'0');
		m = n;
		for (i=0;i<10;i++)
			ka1[i] = 0;
		while (m>0)
		{
			ka1[m%10]++;
			m /= 10;
		}
		i = n;
		bool f;
		while (1)
		{
			i++;
			f = true;
			m = i;
			for (j=0;j<10;j++)
				ka2[j] = 0;
			while (m>0)
			{
				ka2[m%10]++;
				m /= 10;
			}
			for (j=1;j<10 && f;j++)
				if (ka1[j] != ka2[j])
					f = false;
			if (f)
			{
				answer = i;
				break;
			}
		}
	return answer;
}

bool b[110];

int main()
{
	int test,t,i,j,answer,m;
	string n;
	in >> test;
	vector <int> v;
	for (t=1;t<=test;t++)
	{
		in >> n;
		v.clear();
		for (i=0;i<n.size();i++)
			v.push_back(n[i]-'0');
		int f = next_permutation(v.begin(),v.end());
		out << "Case #" << t << ": ";
		if (f)
		{
			for (i=0;i<v.size();i++)
				out << v[i];
		}
		else
		{
			v.push_back(0);
			sort(v.begin(),v.end());
			for (i=0;i<100;i++)
				b[i] = true;
			int start;
			for (i=0;i<v.size();i++)
				if (v[i] != 0)
				{
					b[i] = false;
					start = v[i];
					break;
				}
			out << start;
			for (i=0;i<v.size();i++)
				if (b[i])
					out << v[i];
		}
		out << endl;
	}
	return 0;
}
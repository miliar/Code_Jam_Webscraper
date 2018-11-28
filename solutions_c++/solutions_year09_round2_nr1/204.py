#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#pragma warning( disable : 4786 )

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

ifstream in("input.txt");
ofstream out("output.txt");

vector <char> s;
vector <char> ss;
set <string> st;

char c[1100];

double decim(string s)
{
	double d;
	istringstream kard(s);
	kard >> d;
	//cout << s << " "<< d << endl;
	return d;
}

double solve()
{
	double p = 1.0;
	int index = 0,bac;
	string pr,fe;

	while (index < s.size())
	{
		while (!(s[index] >='0' && s[index]<= '9'))
		{
			index ++;
			if (index > s.size())
				break;
		}
		if (index > s.size())
				break;
		pr = "";
		while ((s[index] >='0' && s[index]<= '9') || s[index] == '.')
		{
			pr = pr + s[index];
			index ++;
		}

		//cout <<" Must Multiply P = " << p << "  by " << pr << endl;

		p *= decim(pr);

		if (s[index] == ')')
			break;

		fe = "";
		while ((s[index] >='a' && s[index]<= 'z'))
		{
			fe = fe + s[index];
			index ++;
		}
		if (st.find(fe) == st.end())
		{
			bac = 1;
			index++;
			while (bac>0)
			{
				if (s[index] == '(')
					bac ++;
				if (s[index] == ')')
					bac --;
				index++;
			}
		}
	}
	
	return p;
}

int main()
{
	int t,test,i,j,k,number,qanak,L,y;
	string name,sr;
	in >> test;
	for (t=1;t<=test;t++)
	{
		in >> L;
		in.getline(c,100);
		ss.clear();
		s.clear();
		for (i=0;i<L;i++)
		{
			in.getline(c,100);
			k = strlen(c);
			for (j=0;j<k;j++)
				ss.push_back(c[j]);
		}
		for (i=0;i<ss.size();i++)
			if (ss[i]!=' ')
				s.push_back(ss[i]);
		/*for (i=0;i<s.size();i++)
			cout << s[i];
		cout << endl;*/
		in >> number;
		out << "Case #" << t << ":" << endl;
		for (y=0;y<number;y++)
		{
			st.clear();
			in >> name >> qanak;
			for (j=0;j<qanak;j++)
			{
				in >> sr;
				st.insert(sr);
			}
			double prob = solve();
			out << setiosflags(ios::fixed | ios::showpoint);
			out << setprecision(7) << prob << endl;
		}
	}
	return 0;
}
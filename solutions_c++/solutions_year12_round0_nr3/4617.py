#include <iostream>
#include <list>
#include <string>
#include <stdlib.h>
#include <sstream>
#include <fstream>

using namespace std;

typedef pair<int, int> par;

bool isti(string&);

string to_string(int& );
int to_number(string&);

void pomestuvanje(string&);

bool proveri(list<par>&, par& );

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");
	int n;
	fin >> n;
	for (int k=0; k<n; ++k)
	{
		int a, b;
		list<par> l;
		fin >> a >> b;
		for (int i=b; i>=a; --i)
		{
			string broj=to_string(i);
			for (int j=0; j<(int)broj.size()-1; ++j)
			{
				pomestuvanje(broj);
				if (broj[0]!='0')
					if (!isti(broj))
					{
						int tb=to_number(broj);
						if (tb>=a && tb< i)
							if (proveri(l, par(i,tb)))
								l.push_back(par(i,tb));
					}
			}
		}
		//cout << "Case #" << k+1 << ": " << l.size() << endl;
		fout << "Case #" << k+1 << ": " << l.size() << endl;
	}

	return 0;
}

bool isti(string& s)
{
	for (int i=1; i<(int)s.size(); ++i)
		if (s[0]!=s[i])
			return false;
	return true;
}

string to_string(int& n)
{
	stringstream s;
	s << n;
	return s.str();
}

int to_number(string& s)
{
	return atoi(s.c_str());
}


void pomestuvanje(string& s)
{
	string temp(s.begin()+1, s.end());
	temp.insert(temp.end(), *s.begin());
	s=temp;
}

bool proveri(list<par>& lis, par& n)
{
	for(list<par>::iterator it=lis.begin(); it!=lis.end(); ++it)
		if ((*it).first==n.first && (*it).second==n.second)
			return false;
	return true;


}
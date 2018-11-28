#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

string calc(vector<int> &depa, vector<int> &depb, vector<int> &arra, vector<int> &arrb)
{
	depa.push_back(INT_MAX);
	depb.push_back(INT_MAX);
	arra.push_back(INT_MAX);
	arrb.push_back(INT_MAX);

	sort(depa.begin(), depa.end());
	sort(depb.begin(), depb.end());
	sort(arra.begin(), arra.end());
	sort(arrb.begin(), arrb.end());
	/*cout << "En:\n";
	for (int i=0; i<engines.size(); ++i)
		cout << engines[i] << endl;
	cout << "Qu:\n";
	for (int i=0; i<queries.size(); ++i)
		cout << queries[i] << endl;*/

	int curA = 0, curB = 0;
	int numA = 0, numB = 0;
	vector<int>::iterator i = depa.begin();
	vector<int>::iterator j = depb.begin();
	vector<int>::iterator k = arra.begin();
	vector<int>::iterator l = arrb.begin();
	while (*i!=INT_MAX || *j!=INT_MAX || *k!=INT_MAX || *l!=INT_MAX)
	{
		if (*k<=*i && *k<=*j && *k<=*l && *k<INT_MAX)
		{
			curB++;
			k++;
		}
		else if (*l<=*i && *l<=*j && *l<=*k && *l<INT_MAX)
		{
			curA++;
			l++;
		}
		else if (*i<=*j && *i<=*k && *i<=*l && *i<INT_MAX)
		{
			if (curA>0) curA--;
			else numA++;
			i++;
		}
		else if (*j<=*i && *j<=*k && *j<=*l && *j<INT_MAX)
		{
			if (curB>0) curB--;
			else numB++;
			j++;
		}		
	}
	stringstream ss;
	ss << numA << " " << numB;
	return ss.str();
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream f(argv[1]);
	int numcases;
	f >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int t,na,nb;
		vector<int> depa, depb;
		vector<int> arra, arrb;
		f >> t >> na >> nb;
		for (int j=0; j<na; ++j)
		{
			char c;
			int a,b;
			f >> a >> c >> b;
			//cout << a << " " << b << endl;
			depa.push_back(a*60+b);
			f >> a >> c >> b;
			//cout << a << " " << b << endl;
			arra.push_back(a*60+b+t);
		}
		for (int j=0; j<nb; ++j)
		{
			char c;
			int a,b;
			f >> a >> c >> b;
			depb.push_back(a*60+b);
			f >> a >> c >> b;
			arrb.push_back(a*60+b+t);
		}
		cout << "Case #" << i+1 << ": " << calc(depa, depb, arra, arrb) << endl;
	}
	f.close();
	return 0;
}

#include <iostream>
using std::cout;
using std::cin;
using std::endl;
#include <string>
using std::string;
#include <vector>
using std::vector;

int main()
{

	string goog = "ynficwlbkuomxsevzpdrjgthaq";
	string abc = "abcdefghijklmnopqrstuvwxyz";
	cout << goog.size();
	cout << '\n' << abc.size();
	int in = 0;
	cin >> in;
	string tmpstr;
	in++;
	vector<string> str;
	
	for (int ii = 0;ii<in;ii++)
	{
		getline(cin,tmpstr);
		str.push_back(tmpstr);
	}
	for (int ii = 0;ii<in;ii++)
	{
		string tmpstr;
		string solvstr;
		tmpstr = str.at(ii);
		solvstr = tmpstr;
		for (int bb = 0; bb < tmpstr.size(); bb ++)
		{
			int loc = -1;
			loc=goog.find(tmpstr[bb]);
			solvstr[bb]=abc[loc];
		}
		cout << "Case #" << ii << ": " <<solvstr <<'\n';
	}
return 0;
}
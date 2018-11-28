#include <tchar.h> 
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/join.hpp>
using namespace std;


namespace String
{
	vector<string> Split(const string& str, const string& sep)
	{
		vector<string> ret;
		boost::split(ret, str, boost::is_any_of(sep));
		return ret;
	}
	vector<string> Split(const string& str, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators = separray;
		return Split(str, sepators);
	}

	string Unsplit(const vector<string>& vals, const string& sep)
	{
		string str = boost::algorithm::join(vals, sep);
		return str;
	}
	string Unsplit(const vector<string>& vals, const char sep)
	{
		char separray[2] = {sep, '\0'};
		string sepators(separray);
		return Unsplit(vals, sepators);
	}
}

template<class T>
void splitstr(const string& s, vector<T>& out)
{
	stringstream in(s);
	out.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int str2int(const string& str) 
{
	stringstream ss(str);
	int num;
	if ((ss >> num).fail())
	{ 
		//ERROR 
	}
	return num;
}



string TestCase(ifstream& input)
{
	char board[4][4];

	bool notcompleted = false;

	string line;
	vector<char> v;
	getline(input, line);
	splitstr(line, v);
	int Xrow1 = 0, Orow1 = 0;
	for (int i=0;i<4; i++)
	{
		board[0][i] = v[i];
		if (v[i] == '.') notcompleted = true;
		if (v[i] == 'X') Xrow1++;
		if (v[i] == 'O') Orow1++;
		if (v[i] == 'T') {Xrow1++; Orow1++;}
	}
	getline(input, line);
	splitstr(line, v);
	int Xrow2 = 0, Orow2 = 0;
	for (int i=0;i<4; i++)
	{
		board[1][i] = v[i];
		if (v[i] == '.') notcompleted = true;
		if (v[i] == 'X') Xrow2++;
		if (v[i] == 'O') Orow2++;
		if (v[i] == 'T') {Xrow2++; Orow2++;}
	}
	getline(input, line);
	splitstr(line, v);
	int Xrow3 = 0, Orow3 = 0;
	for (int i=0;i<4; i++)
	{
		board[2][i] = v[i];
		if (v[i] == '.') notcompleted = true;
		if (v[i] == 'X') Xrow3++;
		if (v[i] == 'O') Orow3++;
		if (v[i] == 'T') {Xrow3++; Orow3++;}
	}
	getline(input, line);
	splitstr(line, v);
	int Xrow4 = 0, Orow4 = 0;
	for (int i=0;i<4; i++)
	{
		board[3][i] = v[i];
		if (v[i] == '.') notcompleted = true;
		if (v[i] == 'X') Xrow4++;
		if (v[i] == 'O') Orow4++;
		if (v[i] == 'T') {Xrow4++; Orow4++;}
	}
	// empty line !!!
	getline(input, line);

	int Xcol1 = 0, Ocol1 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][0];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xcol1++;
		if (val == 'O') Ocol1++;
		if (val == 'T') {Xcol1++; Ocol1++;}
	}

	int Xcol2 = 0, Ocol2 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][1];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xcol2++;
		if (val == 'O') Ocol2++;
		if (val == 'T') {Xcol2++; Ocol2++;}
	}

	int Xcol3 = 0, Ocol3 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][2];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xcol3++;
		if (val == 'O') Ocol3++;
		if (val == 'T') {Xcol3++; Ocol3++;}
	}

	int Xcol4 = 0, Ocol4 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][3];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xcol4++;
		if (val == 'O') Ocol4++;
		if (val == 'T') {Xcol4++; Ocol4++;}
	}

	int Xdiag1 = 0, Odiag1 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][i];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xdiag1++;
		if (val == 'O') Odiag1++;
		if (val == 'T') {Xdiag1++; Odiag1++;}
	}

	int Xdiag2 = 0, Odiag2 = 0;
	for (int i=0;i<4; i++)
	{
		char val = board[i][4-i-1];
		if (val == '.') notcompleted = true;
		if (val == 'X') Xdiag2++;
		if (val == 'O') Odiag2++;
		if (val == 'T') {Xdiag2++; Odiag2++;}
	}
	if (Xrow1==4 || Xrow2==4 || Xrow3==4 || Xrow4==4 || Xcol1==4 || Xcol2==4 || Xcol3==4 || Xcol4==4 || Xdiag1==4 || Xdiag2==4)
		return "X won";
	if (Orow1==4 || Orow2==4 || Orow3==4 || Orow4==4 || Ocol1==4 || Ocol2==4 || Ocol3==4 || Ocol4==4 || Odiag1==4 || Odiag2==4)
		return "O won";
	if (notcompleted)
		return "Game has not completed";
	return "Draw";
}


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream input("A-large.in");
	//ifstream input("A-small-attempt0.in");
	//ifstream input("test.in");

	ofstream myfile("result.txt");

	string line;
	getline(input, line);
	int T = str2int(line);
	cout << "number of cases : " << T << endl;

	for (int i = 0; i<T; i++)
	{
		string res = TestCase(input);
		cout << "Case #" << i+1 << ": "  << res << endl;
		myfile << "Case #" << i+1 << ": "  << res << endl;
	}
	myfile.close();

	return 0;
}

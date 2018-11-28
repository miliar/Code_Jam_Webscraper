#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>

using namespace std;

vector<string> tionary;
int getwords(vector<vector<char>>&poss)
{
	int rv = 0;
	for(int i = 0; i < tionary.size();i++)
	{// every word in dic
		int k = 0;
		for(int j = 0; j < tionary[i].length();j++)
		{//every car in word
			if(binary_search(poss[j].begin(), poss[j].end(), tionary[i][j]))
				k++;
		}
		if(k == tionary[i].length())
			rv++;
	}
	return rv;
}
int process_testcase(string s)
{
	int rv = 0;
	vector< vector<char> > poss;
	int bra = 0; // 0=not within bracket// 1= within bracket
	vector<char> vc;
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == '(')
		{
			bra = 1;
			continue;
		}
		if(s[i] == ')')
		{
			bra = 0;
			poss.push_back(vc);
			vc.clear();
			continue;
		}
		vc.push_back(s[i]);
		if(0 == bra)
		{
			poss.push_back(vc);
			vc.clear();
		}
	}
	for(int i = 0; i < poss.size();i++)
	{
		sort(poss[i].begin(), poss[i].end());
		for(int j = 0; j < poss[i].size();j++)
		{
			;//cout << poss[i][j];
		}
		//cout <<endl;
	}
	rv = getwords(poss);
	return rv;
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("C:\\Users\\viv.NORTHAMERICA\\Downloads\\alien.prac.txt");
	else
		is.open(argv[1]);


	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	int numchars,dic;
	iss >> numchars >> dic >> tc;
	//printf("num tc == %d\n", tc);
	for(int i = 1; i <= dic; i++)
	{
		getline(is,s);
		tionary.push_back(s);
	}

	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		// find number of lines for this testcase
		getline(is,s); 
		cout << process_testcase(s) << endl;
	}
	is.close();
	return 0;
}
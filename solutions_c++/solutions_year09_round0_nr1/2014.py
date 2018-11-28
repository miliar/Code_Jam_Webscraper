
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>

using namespace std;

vector<string> tionary;

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("C:\\Users\\viv.NORTHAMERICA\\Downloads\\asmall.in");
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
		vector< string > poss;
		int bra = 0; // 0=not within bracket// 1= within bracket
		string vc = "";
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
				vc="";
				continue;
			}
			vc+=s[i];
			if(0 == bra)
			{
				poss.push_back(vc);
				vc = "";
			}
		}

		int rv = 0;
		for(int i = 0; i < dic ;i++)
		{// every word in dic
			int k = 0;
			for(int j = 0; j < numchars;j++)
			{//every car in word
				if(poss[j].end() != (find(poss[j].begin(), poss[j].end(), tionary[i][j])))
					k++;
				else
					break;
			}
			if(k == tionary[i].length())
				rv++;
		}


		//cout << process_testcase(s) << endl;
		cout << rv << endl;
	}
	is.close();
	return 0;
}

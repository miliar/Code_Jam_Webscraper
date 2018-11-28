#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>
#include<strstream>
#include<sstream>

using namespace std;

void solve(int k,int a, int b, int * total)
{
	if (k <= 10) return;

	strstream ss;
    string s;
    ss << k;
    ss >> s;

	string ans(s);
	int n = s.length();

	int past[10];
	int numP = 0;

	for (int i = 1; i < n; i++)
	{
		
		for (int j = 0; j < n; j++)
		{
			ans[(j+i)%n] = s[j];
		}
		istringstream   iStr(ans); 
		int tmpAns;
		iStr>>tmpAns;
		if (tmpAns <= b && tmpAns >= a && tmpAns != k)
		{
			bool notFind = true;
			for ( int kkk = 1; kkk <= numP; kkk++)
			{
				if (past[kkk] == tmpAns )
				{
					notFind = false;
					break;
				}
			}

			if (notFind)
			{
				(*total)++;
				numP++;
				past[numP] = tmpAns;
			}
			
		}

	}
}


int main()
{
	ifstream in("large.in");
	ofstream out("large.out");

	

	int T;
	in>>T;

	
	for ( int i = 1; i <= T; i++)
	{
		int a,  b;
		in>>a>>b;

		int total = 0;

		for ( int j = a; j <= b; j++)
		{
			solve(j,a,b,&total);
		}

		out<<"Case #"<<i<<": "<<total / 2<<endl;
	}

	
}
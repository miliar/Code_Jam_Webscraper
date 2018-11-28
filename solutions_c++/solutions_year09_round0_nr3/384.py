#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

#define MOD 10000

ifstream fin;
ofstream fout;

string inp,S = "welcome to code jam";
int dp[20][500];

string getResult(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	while(s.size() < 4)
		s = "0" + s;
	return s;
}

int main()
{
	int N,i,j;
	fin.open("c.in");
	fout.open("c.out");
	
	fin >> N;
	getline(fin, inp);
	for(int t = 1; t <= N; t++)
	{
		getline(fin,inp);
		fout << "Case #" << t << ": ";
		if(inp.size() == 0)
		{
			fout << "0000" << endl;
			continue;
		}
		for(i = 0; i < S.size(); i++)
			dp[0][i] = 0;
		
		if(inp[0] == S[0])
			dp[0][0] = 1;
		
		for(i = 1; i < inp.size(); i++)
			if(S[0] == inp[i])
				dp[0][i] = dp[0][i-1] + 1;
			else
				dp[0][i] = dp[0][i-1];
		
		
		for(i = 1; i < S.size(); i++)
			for(j = 1; j < inp.size(); j++)
				if(S[i] == inp[j])
					dp[i][j] = (dp[i-1][j-1] + dp[i][j-1])%MOD;
				else
					dp[i][j] = dp[i][j-1];
		fout << getResult(dp[S.size()-1][inp.size()-1]) << endl;
	}
	fout.close();
	fin.close();
	return 0;
}

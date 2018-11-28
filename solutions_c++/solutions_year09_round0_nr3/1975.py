#include <string>
#include <fstream>
#include <vector>
#include <cstdio>

using namespace std;

char top[] = "welcome to code jam";
int L = 19;
int M = 10000;

int gogo(const string &s)
{
	vector<vector<int> > dp = vector<vector<int> >(19, vector<int>(s.size(), 0));
	if(s[0] == top[0])
		dp[0][0] = 1;
	for(int i = 1; i < s.size(); i++)
	{
		dp[0][i] = dp[0][i-1];
		if(s[i] == top[0])
			dp[0][i] = (dp[0][i] + 1) % M;
	}
	for(int j = 1; j < L; j++)
	{
		for(int i = 1; i < s.size(); i++)
		{
			dp[j][i] = dp[j][i-1];
			if(s[i] == top[j])
				dp[j][i] = (dp[j][i] + dp[j-1][i-1]) % M;
		}
	}
	return dp[L - 1][s.size() - 1];
}

int main()
{
	ifstream f;
	f.open("Clarge.txt");
	int N;
	f >> N;
	f.ignore();
	FILE *o;
	o = fopen("Coutlarge.txt","w");
	for(int i = 0; i < N; i++)
	{
		string s;
		getline(f, s);
		fprintf(o, "Case #%d: %04d \n", i+1, gogo(s));
	}
	fclose(o);
	f.close();
	return 0;
}
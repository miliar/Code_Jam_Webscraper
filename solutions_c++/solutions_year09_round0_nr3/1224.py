#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

string toString(int x)
{
	stringstream ss;
	ss << x;
	string s;
	ss >> s;
	while(s.size() < 4){
        s = "0" + s;
	}
	return s;
}

#define MOD 10000

int N, dp[2][20];
string welcome = "welcome to code jam", text;

int get()
{
    memset(dp, 0, sizeof(dp));
    int res = 0;
    for(int i = 0; i < text.size(); i++){
        dp[1][0] = 0;
        if(text[i] == welcome[0]){
            dp[1][0]++;
        }
        for(int j = 1; j < welcome.size(); j++){
            dp[1][j] = 0;
            if(text[i] == welcome[j]){
                dp[1][j] = dp[0][j - 1];
            }
        }
        for(int j = 0; j < welcome.size(); j++){
            dp[0][j] += dp[1][j];
            dp[0][j] %= MOD;
        }
    }
    return dp[0][welcome.size() - 1];
}

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    fin >> N;
    getline(fin, text);
    for(int test = 1; test <= N; test++){
        getline(fin, text);
        fout << "Case #" << test << ": " << toString(get()) << endl;
    }
}

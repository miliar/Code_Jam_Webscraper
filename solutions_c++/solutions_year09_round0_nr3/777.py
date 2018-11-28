#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <ios>

using namespace std;

typedef vector<vector<int> > vvi_t;
typedef vector<vector<char> > vvc_t;
typedef map<int, int> mii_t;


const string test = "welcome to code jam";
const int test_size = 19;

string in = "";

int dp[test_size+1][501];

int ans = 0;

void
initialize_dp()
{
    for (int i = 0; i < test_size+1; ++i)
    {
	for (int j = 0; j < 501; ++j)
	{
	    dp[i][j] = -1;
	}
    }
}


/* Returns how many times a string of size 'n' from the back of 'test' occurs
 * in 'in' after(and including) index 'pos'
 */
int
f(int n, int pos)
{
    if (n == 0)
	return 1;

    if (pos >= in.size())
	return 0;

    cerr<<"f("<<n<<", "<<pos<<") == "<<dp[n][pos]<<"\n";

    if (dp[n][pos] != -1)
	return dp[n][pos];

    int ti = test_size - n;
    char tc = test[ti];
    // cerr<<"ti, tc: "<<ti<<", "<<tc<<endl;

    if (in[pos] == tc)
    {
	int i1 = f(n, pos+1);
	int i2 = f(n-1, pos+1);
	dp[n][pos] = (i1 + i2) % 10000;
    }
    else
    {
	dp[n][pos] = f(n, pos+1);
    }

    return dp[n][pos];
}


int
main()
{
    int t = 0;
    cin>>t;
    char ch = cin.get();
    while (isspace(ch))
    {
	ch = cin.get();
    }
    cin.putback(ch);

    for (int i = 0; i < t; ++i)
    {
	initialize_dp();
	in.clear();
	getline(cin, in);
	// cout<<in<<endl;
	cout<<"Case #"<<i+1<<": ";
	cout.width(4);
	cout.fill('0');
	cout<<f(test_size, 0)<<endl;
    }

}

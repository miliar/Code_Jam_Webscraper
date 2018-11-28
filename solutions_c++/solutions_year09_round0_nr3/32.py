#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

#define mod 10000

using namespace std;

int main()
{
	string s = "welcome to code jam";
	int n=s.size();
	int T;
	cin >> T;
	cin.ignore();
	for (int caso=1;caso<=T;caso++)
	{
		string t;
		getline (cin,t);
		int m =t.size();
		vector <vector <int> > din (m+1, vector <int> (n+1,0));
		din[0][0]=1;
		for (int i=1;i<=m;i++)
		{
			din[i][0]=1;
			for (int j=1;j<=n;j++)
			{
				din[i][j]=din[i-1][j];
				if (s[j-1]==t[i-1])
					din[i][j]+=din[i-1][j-1];
				din[i][j]%=mod;
			}
		}
		cout << "Case #" << caso << ": " << setw (4) << setfill('0') << din[m][n] << endl;
	}
}
